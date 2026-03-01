"""
Скрипт для создания .exe файла редактора KHX
Использование: python build_exe.py
"""

import PyInstaller.__main__
import os
import sys

print("=" * 60)
print("  Сборка KHX Editor в .exe файл")
print("=" * 60)
print()

# Проверяем наличие файлов
required_files = ['editor.py']
src_files = [
    'khx.py', 'khx_v5.py', 'khx_gui.py', 'khx_database.py',
    'khx_network.py', 'khx_ml.py', 'khx_game.py', 'khx_crypto.py',
    'khx_datascience.py', 'khx_testing.py', 'khx_async.py',
    'khx_canvas.py', 'khx_cli.py', 'khx_audio.py', 'khx_mobile.py',
    'khx_package.py', 'khx_i18n.py', 'khx_plugin.py', 'khx_template.py',
    'khx_watcher.py', 'khx_events.py', 'khx_debug.py',
    'khx_server.py', 'khx_os.py'
]

# Проверяем файлы
for file in required_files:
    if not os.path.exists(file):
        print(f"✗ Ошибка: файл {file} не найден!")
        sys.exit(1)

# Собираем add-data параметры
add_data = []
for src_file in src_files:
    # Проверяем в src/ и в корне
    if os.path.exists(f'src/{src_file}'):
        add_data.append(f'--add-data=src/{src_file};src')
    elif os.path.exists(src_file):
        add_data.append(f'--add-data={src_file};.')

print(f"Найдено модулей: {len(add_data)}")
print()

# Параметры сборки
params = [
    'editor.py',
    '--onefile',
    '--windowed',
    '--name=KHX-Editor',
    '--hidden-import=PyQt5',
    '--hidden-import=PyQt5.Qsci',
    '--hidden-import=numpy',
    '--hidden-import=matplotlib',
    '--clean',
] + add_data

print("Запуск PyInstaller...")
print()

try:
    PyInstaller.__main__.run(params)
    print()
    print("=" * 60)
    print("  ✓ KHX-Editor.exe создан в папке dist/")
    print("=" * 60)
except Exception as e:
    print(f"✗ Ошибка при сборке: {e}")
    sys.exit(1)
