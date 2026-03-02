#!/usr/bin/env python3
"""
KHX CLI Installer
Устанавливает команду 'khx' в систему
"""

import os
import sys
import shutil
import platform
from pathlib import Path


def get_install_path():
    """Получить путь для установки"""
    system = platform.system()
    
    if system == "Windows":
        # Windows: C:\Users\Username\AppData\Local\Programs\KHX
        appdata = os.getenv('LOCALAPPDATA')
        return os.path.join(appdata, 'Programs', 'KHX')
    elif system == "Linux":
        # Linux: ~/.local/bin
        return os.path.expanduser('~/.local/bin')
    elif system == "Darwin":
        # macOS: /usr/local/bin
        return '/usr/local/bin'
    else:
        return os.path.expanduser('~/.local/bin')


def create_khx_script(install_dir, khx_root):
    """Создать скрипт khx"""
    system = platform.system()
    
    if system == "Windows":
        # Windows batch script
        script_path = os.path.join(install_dir, 'khx.bat')
        content = f'''@echo off
python "{khx_root}\\src\\khx_v5.py" %*
'''
    else:
        # Unix shell script
        script_path = os.path.join(install_dir, 'khx')
        content = f'''#!/bin/bash
python3 "{khx_root}/src/khx_v5.py" "$@"
'''
    
    with open(script_path, 'w') as f:
        f.write(content)
    
    # Сделать исполняемым на Unix
    if system != "Windows":
        os.chmod(script_path, 0o755)
    
    return script_path


def add_to_path(install_dir):
    """Добавить в PATH"""
    system = platform.system()
    
    if system == "Windows":
        print(f"\n[INFO] Добавьте в PATH:")
        print(f"       {install_dir}")
        print(f"\nИнструкция:")
        print(f"1. Откройте 'Система' -> 'Дополнительные параметры системы'")
        print(f"2. 'Переменные среды' -> 'Path' -> 'Изменить'")
        print(f"3. Добавьте: {install_dir}")
    else:
        shell_rc = os.path.expanduser('~/.bashrc')
        if os.path.exists(os.path.expanduser('~/.zshrc')):
            shell_rc = os.path.expanduser('~/.zshrc')
        
        path_line = f'\nexport PATH="{install_dir}:$PATH"\n'
        
        with open(shell_rc, 'a') as f:
            f.write(path_line)
        
        print(f"\n[INFO] Добавлено в {shell_rc}")
        print(f"       Перезапустите терминал или выполните: source {shell_rc}")


def install_cli():
    """Установить KHX CLI"""
    print("=" * 60)
    print("KHX CLI Installer v5.2")
    print("=" * 60)
    
    # Текущая директория (корень проекта)
    khx_root = os.path.dirname(os.path.abspath(__file__))
    print(f"\n[1/4] KHX Root: {khx_root}")
    
    # Проверка наличия интерпретатора
    interpreter = os.path.join(khx_root, 'src', 'khx_v5.py')
    if not os.path.exists(interpreter):
        print(f"\n[ERROR] Интерпретатор не найден: {interpreter}")
        return False
    
    print(f"[2/4] Интерпретатор найден: {interpreter}")
    
    # Путь установки
    install_dir = get_install_path()
    os.makedirs(install_dir, exist_ok=True)
    print(f"[3/4] Директория установки: {install_dir}")
    
    # Создать скрипт
    script_path = create_khx_script(install_dir, khx_root)
    print(f"[4/4] Скрипт создан: {script_path}")
    
    # Добавить в PATH
    add_to_path(install_dir)
    
    print("\n" + "=" * 60)
    print("✅ KHX CLI установлен успешно!")
    print("=" * 60)
    print("\nИспользование:")
    print("  khx <file.khx>           - Запустить программу")
    print("  khx --version            - Показать версию")
    print("  khx --help               - Показать справку")
    print("  khx --repl               - Интерактивный режим")
    print("  khx --new <name>         - Создать новый проект")
    print("\nПримеры:")
    print("  khx hello.khx")
    print("  khx --repl")
    print("  khx --new my_project")
    
    return True


def uninstall_cli():
    """Удалить KHX CLI"""
    print("=" * 60)
    print("KHX CLI Uninstaller")
    print("=" * 60)
    
    install_dir = get_install_path()
    system = platform.system()
    
    if system == "Windows":
        script_path = os.path.join(install_dir, 'khx.bat')
    else:
        script_path = os.path.join(install_dir, 'khx')
    
    if os.path.exists(script_path):
        os.remove(script_path)
        print(f"\n✅ Удалено: {script_path}")
    else:
        print(f"\n⚠️  Скрипт не найден: {script_path}")
    
    print("\n[INFO] Не забудьте удалить из PATH вручную")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "uninstall":
        uninstall_cli()
    else:
        install_cli()
