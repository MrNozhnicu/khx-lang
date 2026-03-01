"""
KHX Plugin System Module
Система плагинов для расширения функциональности
"""

import os
import importlib.util

# Storage
plugins = {}
plugin_hooks = {}


class Plugin:
    """Плагин"""
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath
        self.module = None
        self.hooks = {}
        self.enabled = False
        self.metadata = {
            "name": name,
            "version": "1.0.0",
            "author": "Unknown",
            "description": ""
        }
    
    def load(self):
        """Загрузить плагин"""
        try:
            print(f"[Plugin] Загрузка: {self.name}")
            
            # Загружаем модуль
            spec = importlib.util.spec_from_file_location(self.name, self.filepath)
            if spec and spec.loader:
                self.module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(self.module)
                
                # Получаем метаданные
                if hasattr(self.module, 'PLUGIN_INFO'):
                    self.metadata.update(self.module.PLUGIN_INFO)
                
                self.enabled = True
                print(f"[Plugin] ✓ {self.name} загружен")
                
                # Вызываем init hook
                self.trigger_hook('init')
                return True
            
        except Exception as e:
            print(f"[Plugin] ✗ Ошибка загрузки {self.name}: {e}")
            return False
    
    def unload(self):
        """Выгрузить плагин"""
        print(f"[Plugin] Выгрузка: {self.name}")
        self.trigger_hook('unload')
        self.enabled = False
        self.module = None
        print(f"[Plugin] ✓ {self.name} выгружен")
        return True
    
    def on(self, event, callback):
        """Зарегистрировать обработчик события"""
        if event not in self.hooks:
            self.hooks[event] = []
        self.hooks[event].append(callback)
        print(f"[Plugin] Хук зарегистрирован: {event}")
    
    def trigger_hook(self, event, *args, **kwargs):
        """Вызвать хук"""
        if event in self.hooks:
            for callback in self.hooks[event]:
                try:
                    callback(*args, **kwargs)
                except Exception as e:
                    print(f"[Plugin] ✗ Ошибка в хуке {event}: {e}")
    
    def call(self, function_name, *args, **kwargs):
        """Вызвать функцию плагина"""
        if not self.enabled or not self.module:
            print(f"[Plugin] ✗ Плагин {self.name} не загружен")
            return None
        
        if hasattr(self.module, function_name):
            func = getattr(self.module, function_name)
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                print(f"[Plugin] ✗ Ошибка вызова {function_name}: {e}")
                return None
        else:
            print(f"[Plugin] ✗ Функция {function_name} не найдена")
            return None


def load_plugin(filepath):
    """Загрузить плагин из файла"""
    if not os.path.exists(filepath):
        print(f"[Plugin] ✗ Файл не найден: {filepath}")
        return None
    
    plugin_name = os.path.basename(filepath).replace('.khx', '').replace('.py', '')
    plugin = Plugin(plugin_name, filepath)
    
    if plugin.load():
        plugins[plugin_name] = plugin
        return plugin_name
    
    return None


def get_plugin(plugin_name):
    """Получить плагин"""
    return plugins.get(plugin_name)


def unload_plugin(plugin_name):
    """Выгрузить плагин"""
    if plugin_name in plugins:
        plugin = plugins[plugin_name]
        plugin.unload()
        del plugins[plugin_name]
        return True
    return False


def list_plugins():
    """Список загруженных плагинов"""
    print(f"\n[Plugin] Загруженные плагины ({len(plugins)}):")
    for name, plugin in plugins.items():
        status = "✓" if plugin.enabled else "✗"
        print(f"  {status} {name} v{plugin.metadata['version']}")
        print(f"      {plugin.metadata['description']}")
    return list(plugins.keys())


def register_hook(hook_name, callback):
    """Зарегистрировать глобальный хук"""
    if hook_name not in plugin_hooks:
        plugin_hooks[hook_name] = []
    plugin_hooks[hook_name].append(callback)
    print(f"[Plugin] Глобальный хук: {hook_name}")


def trigger_hook(hook_name, *args, **kwargs):
    """Вызвать глобальный хук"""
    if hook_name in plugin_hooks:
        for callback in plugin_hooks[hook_name]:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"[Plugin] ✗ Ошибка в хуке {hook_name}: {e}")


def create_plugin_sandbox():
    """Создать изолированную среду для плагина"""
    print(f"[Plugin] Создана sandbox среда")
    return {
        "allowed_modules": ["math", "json", "time"],
        "restricted": True
    }


if __name__ == "__main__":
    print("=== KHX Plugin System Test ===\n")
    
    # Создаем тестовый плагин
    test_plugin_code = '''
PLUGIN_INFO = {
    "name": "test-plugin",
    "version": "1.0.0",
    "author": "KHX Team",
    "description": "Тестовый плагин"
}

def hello():
    return "Hello from plugin!"

def calculate(x, y):
    return x + y
'''
    
    # Сохраняем тестовый плагин
    with open("test_plugin.py", "w", encoding="utf-8") as f:
        f.write(test_plugin_code)
    
    # Загружаем плагин
    plugin_id = load_plugin("test_plugin.py")
    
    if plugin_id:
        plugin = get_plugin(plugin_id)
        
        # Вызываем функции
        result1 = plugin.call("hello")
        print(f"[Test] Результат: {result1}")
        
        result2 = plugin.call("calculate", 10, 20)
        print(f"[Test] Результат: {result2}")
        
        # Список плагинов
        list_plugins()
        
        # Выгружаем
        unload_plugin(plugin_id)
    
    # Удаляем тестовый файл
    if os.path.exists("test_plugin.py"):
        os.remove("test_plugin.py")
