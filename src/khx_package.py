"""
KHX Package Manager Module
Менеджер пакетов для установки библиотек
"""

import json
import os

# Storage
installed_packages = {}
package_registry = {
    "http": {"version": "1.0.0", "description": "HTTP client library"},
    "json": {"version": "2.3.1", "description": "JSON parser"},
    "math": {"version": "1.5.0", "description": "Math utilities"},
    "crypto": {"version": "3.0.0", "description": "Cryptography tools"},
    "database": {"version": "2.1.0", "description": "Database connectors"},
}


class Package:
    """Пакет"""
    def __init__(self, name, version, description=""):
        self.name = name
        self.version = version
        self.description = description
        self.dependencies = []
        self.installed = False
    
    def add_dependency(self, dep_name, dep_version):
        """Добавить зависимость"""
        self.dependencies.append({"name": dep_name, "version": dep_version})
    
    def install(self):
        """Установить пакет"""
        print(f"[Package] Установка {self.name}@{self.version}...")
        
        # Установка зависимостей
        for dep in self.dependencies:
            print(f"[Package]   └─ Зависимость: {dep['name']}@{dep['version']}")
        
        self.installed = True
        installed_packages[self.name] = self
        print(f"[Package] ✓ {self.name}@{self.version} установлен")
        return True
    
    def uninstall(self):
        """Удалить пакет"""
        print(f"[Package] Удаление {self.name}@{self.version}...")
        self.installed = False
        if self.name in installed_packages:
            del installed_packages[self.name]
        print(f"[Package] ✓ {self.name} удален")
        return True


def install_package(name, version=None):
    """Установить пакет"""
    if name in package_registry:
        pkg_info = package_registry[name]
        version = version or pkg_info["version"]
        
        pkg = Package(name, version, pkg_info["description"])
        pkg.install()
        return True
    else:
        print(f"[Package] ✗ Пакет '{name}' не найден в реестре")
        return False


def uninstall_package(name):
    """Удалить пакет"""
    if name in installed_packages:
        pkg = installed_packages[name]
        pkg.uninstall()
        return True
    else:
        print(f"[Package] ✗ Пакет '{name}' не установлен")
        return False


def list_packages():
    """Список установленных пакетов"""
    print(f"\n[Package] Установленные пакеты ({len(installed_packages)}):")
    for name, pkg in installed_packages.items():
        print(f"  • {name}@{pkg.version} - {pkg.description}")
    return list(installed_packages.keys())


def search_packages(query):
    """Поиск пакетов"""
    print(f"\n[Package] Поиск: '{query}'")
    results = []
    for name, info in package_registry.items():
        if query.lower() in name.lower() or query.lower() in info["description"].lower():
            results.append(name)
            print(f"  • {name}@{info['version']} - {info['description']}")
    return results


def update_package(name):
    """Обновить пакет"""
    if name in installed_packages:
        pkg = installed_packages[name]
        print(f"[Package] Обновление {name}...")
        print(f"[Package] {pkg.version} → {package_registry[name]['version']}")
        pkg.version = package_registry[name]['version']
        print(f"[Package] ✓ {name} обновлен")
        return True
    else:
        print(f"[Package] ✗ Пакет '{name}' не установлен")
        return False


def publish_package(name, version, description, files):
    """Опубликовать пакет в реестр"""
    print(f"\n[Package] Публикация пакета...")
    print(f"[Package] Имя: {name}")
    print(f"[Package] Версия: {version}")
    print(f"[Package] Файлов: {len(files)}")
    
    package_registry[name] = {
        "version": version,
        "description": description
    }
    
    print(f"[Package] ✓ Пакет опубликован в реестре")
    return True


def init_project(project_name):
    """Инициализировать проект"""
    print(f"\n[Package] Инициализация проекта: {project_name}")
    
    config = {
        "name": project_name,
        "version": "1.0.0",
        "dependencies": {}
    }
    
    config_file = "khx.json"
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print(f"[Package] ✓ Создан {config_file}")
    return config_file


def load_dependencies(config_file="khx.json"):
    """Загрузить зависимости из конфига"""
    if not os.path.exists(config_file):
        print(f"[Package] ✗ Файл {config_file} не найден")
        return False
    
    with open(config_file, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    print(f"\n[Package] Установка зависимостей для {config['name']}...")
    
    deps = config.get('dependencies', {})
    for name, version in deps.items():
        install_package(name, version)
    
    print(f"[Package] ✓ Все зависимости установлены")
    return True


if __name__ == "__main__":
    print("=== KHX Package Manager Test ===\n")
    
    # Поиск пакетов
    search_packages("http")
    
    # Установка
    install_package("http")
    install_package("json")
    install_package("crypto")
    
    # Список
    list_packages()
    
    # Обновление
    update_package("http")
    
    # Инициализация проекта
    init_project("my-khx-project")
