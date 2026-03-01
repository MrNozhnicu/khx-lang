# Установка KHX

## Системные требования

- Python 3.8 или выше
- Windows / Linux / macOS
- 100 MB свободного места

## Установка из исходников

### 1. Клонировать репозиторий

```bash
git clone https://github.com/yourusername/khx-lang.git
cd khx-lang
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Запустить редактор

```bash
python editor.py
```

### 4. Запустить программу

```bash
python src/khx_v5.py examples/hello.khx
```

## Установка скомпилированной версии

### Windows

1. Скачайте `KHX-Editor.exe` из [Releases](https://github.com/yourusername/khx-lang/releases)
2. Запустите файл
3. Готово!

## Сборка .exe самостоятельно

```bash
# Установить PyInstaller
pip install pyinstaller

# Собрать .exe
python build_exe.py

# Файл будет в папке dist/
```

## Проверка установки

```bash
# Запустить тестовый пример
python src/khx_v5.py examples/hello.khx
```

Должно вывести:
```
Hello, World!
Добро пожаловать в KHX v5.0!
```

## Возможные проблемы

### ModuleNotFoundError: No module named 'PyQt5'

```bash
pip install PyQt5 QScintilla
```

### ModuleNotFoundError: No module named 'numpy'

```bash
pip install numpy matplotlib
```

### Network модуль не загружается

```bash
pip install requests
```

## Обновление

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Удаление

Просто удалите папку с проектом.

## Поддержка

Если возникли проблемы:
- Проверьте [Issues](https://github.com/yourusername/khx-lang/issues)
- Создайте новый Issue с описанием проблемы
