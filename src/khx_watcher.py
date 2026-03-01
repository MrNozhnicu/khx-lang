"""
KHX File System Watcher Module
Мониторинг изменений файловой системы
"""

import os
import time
from pathlib import Path

# Storage
watchers = {}
watcher_counter = 0


class FileWatcher:
    """Наблюдатель за файлами"""
    def __init__(self, path):
        self.path = path
        self.running = False
        self.callbacks = {
            'change': [],
            'create': [],
            'delete': [],
            'any': []
        }
        self.file_states = {}
        self.scan_interval = 1.0  # секунды
        print(f"[Watcher] Создан для: {path}")
    
    def on_change(self, callback):
        """Обработчик изменения файла"""
        self.callbacks['change'].append(callback)
        print(f"[Watcher] Зарегистрирован обработчик: on_change")
    
    def on_create(self, callback):
        """Обработчик создания файла"""
        self.callbacks['create'].append(callback)
        print(f"[Watcher] Зарегистрирован обработчик: on_create")
    
    def on_delete(self, callback):
        """Обработчик удаления файла"""
        self.callbacks['delete'].append(callback)
        print(f"[Watcher] Зарегистрирован обработчик: on_delete")
    
    def on_any(self, callback):
        """Обработчик любого события"""
        self.callbacks['any'].append(callback)
        print(f"[Watcher] Зарегистрирован обработчик: on_any")
    
    def start(self):
        """Запустить наблюдение"""
        self.running = True
        print(f"[Watcher] Запущен мониторинг: {self.path}")
        
        # Начальное сканирование
        self._scan_directory()
        
        return True
    
    def stop(self):
        """Остановить наблюдение"""
        self.running = False
        print(f"[Watcher] Остановлен мониторинг: {self.path}")
        return True
    
    def _scan_directory(self):
        """Сканировать директорию"""
        if not os.path.exists(self.path):
            print(f"[Watcher] ✗ Путь не существует: {self.path}")
            return
        
        current_files = {}
        
        # Сканируем все файлы
        if os.path.isfile(self.path):
            # Один файл
            current_files[self.path] = os.path.getmtime(self.path)
        else:
            # Директория
            for root, dirs, files in os.walk(self.path):
                for file in files:
                    filepath = os.path.join(root, file)
                    try:
                        current_files[filepath] = os.path.getmtime(filepath)
                    except:
                        pass
        
        # Проверяем изменения
        self._check_changes(current_files)
        
        # Обновляем состояние
        self.file_states = current_files
    
    def _check_changes(self, current_files):
        """Проверить изменения"""
        # Новые файлы
        for filepath in current_files:
            if filepath not in self.file_states:
                self._trigger_event('create', filepath)
        
        # Удаленные файлы
        for filepath in self.file_states:
            if filepath not in current_files:
                self._trigger_event('delete', filepath)
        
        # Измененные файлы
        for filepath in current_files:
            if filepath in self.file_states:
                if current_files[filepath] != self.file_states[filepath]:
                    self._trigger_event('change', filepath)
    
    def _trigger_event(self, event_type, filepath):
        """Вызвать событие"""
        print(f"[Watcher] Событие: {event_type} - {filepath}")
        
        # Вызываем специфичные обработчики
        for callback in self.callbacks.get(event_type, []):
            try:
                callback(filepath)
            except Exception as e:
                print(f"[Watcher] ✗ Ошибка в обработчике: {e}")
        
        # Вызываем общие обработчики
        for callback in self.callbacks.get('any', []):
            try:
                callback(event_type, filepath)
            except Exception as e:
                print(f"[Watcher] ✗ Ошибка в обработчике: {e}")
    
    def set_interval(self, seconds):
        """Установить интервал сканирования"""
        self.scan_interval = seconds
        print(f"[Watcher] Интервал сканирования: {seconds}s")


def create_watcher(path):
    """Создать наблюдателя"""
    global watcher_counter
    watcher_id = f"watcher_{watcher_counter}"
    watcher_counter += 1
    watchers[watcher_id] = FileWatcher(path)
    return watcher_id


def get_watcher(watcher_id):
    """Получить наблюдателя"""
    return watchers.get(watcher_id)


def watch_file(filepath, callback):
    """Быстрое наблюдение за файлом"""
    watcher_id = create_watcher(filepath)
    watcher = get_watcher(watcher_id)
    watcher.on_change(callback)
    watcher.start()
    return watcher_id


def watch_directory(dirpath, callback, recursive=True):
    """Быстрое наблюдение за директорией"""
    watcher_id = create_watcher(dirpath)
    watcher = get_watcher(watcher_id)
    watcher.on_any(callback)
    watcher.start()
    return watcher_id


if __name__ == "__main__":
    print("=== KHX File Watcher Module Test ===\n")
    
    # Создаем тестовую директорию
    test_dir = "test_watch"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Создаем наблюдателя
    watcher_id = create_watcher(test_dir)
    watcher = get_watcher(watcher_id)
    
    # Регистрируем обработчики
    def on_file_change(filepath):
        print(f"[Handler] Файл изменен: {filepath}")
    
    def on_file_create(filepath):
        print(f"[Handler] Файл создан: {filepath}")
    
    def on_file_delete(filepath):
        print(f"[Handler] Файл удален: {filepath}")
    
    watcher.on_change(on_file_change)
    watcher.on_create(on_file_create)
    watcher.on_delete(on_file_delete)
    
    # Запускаем
    watcher.start()
    
    # Симулируем изменения
    print("\n[Test] Создание файла...")
    test_file = os.path.join(test_dir, "test.txt")
    with open(test_file, 'w') as f:
        f.write("Hello")
    
    time.sleep(0.5)
    watcher._scan_directory()
    
    print("\n[Test] Изменение файла...")
    time.sleep(0.5)
    with open(test_file, 'w') as f:
        f.write("Hello World")
    
    time.sleep(0.5)
    watcher._scan_directory()
    
    print("\n[Test] Удаление файла...")
    os.remove(test_file)
    
    time.sleep(0.5)
    watcher._scan_directory()
    
    # Останавливаем
    watcher.stop()
    
    # Удаляем тестовую директорию
    if os.path.exists(test_dir):
        os.rmdir(test_dir)
