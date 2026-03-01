# Инструкция по публикации на GitHub

## Шаг 1: Инициализация Git

```bash
git init
```

## Шаг 2: Добавить файлы

```bash
git add .
```

## Шаг 3: Первый коммит

```bash
git commit -m "Initial commit: KHX Programming Language v5.0"
```

## Шаг 4: Создать репозиторий на GitHub

1. Перейдите на https://github.com
2. Нажмите "New repository"
3. Название: `khx-lang` (или любое другое)
4. Описание: "Modern programming language with 20+ built-in modules"
5. Выберите Public
6. НЕ добавляйте README, .gitignore, LICENSE (они уже есть)
7. Нажмите "Create repository"

## Шаг 5: Подключить удаленный репозиторий

```bash
git remote add origin https://github.com/YOUR_USERNAME/khx-lang.git
```

Замените `YOUR_USERNAME` на ваше имя пользователя GitHub.

## Шаг 6: Отправить код

```bash
git branch -M main
git push -u origin main
```

## Шаг 7: Настроить GitHub

### Добавить темы (Topics)

В настройках репозитория добавьте темы:
- programming-language
- interpreter
- python
- gui
- machine-learning
- game-engine
- database

### Добавить описание

```
Modern programming language with 20+ built-in modules: GUI, Database, ML, Games, Mobile, and more!
```

### Добавить Website

Если есть, добавьте ссылку на документацию или сайт.

## Шаг 8: Создать Release

1. Перейдите в "Releases"
2. Нажмите "Create a new release"
3. Tag: `v5.0.0`
4. Title: `KHX v5.0 - Complete Release`
5. Описание:
```markdown
# KHX v5.0 - Complete Release

First stable release of KHX Programming Language!

## Features
- ✅ 20+ built-in modules
- ✅ GUI Framework
- ✅ Database support
- ✅ Machine Learning
- ✅ Game Engine
- ✅ Mobile Development
- ✅ And much more!

## Downloads
- Source code (zip/tar.gz)
- KHX-Editor.exe (Windows) - Coming soon

## Installation
```bash
pip install -r requirements.txt
python editor.py
```

See [README.md](README.md) for full documentation.
```

6. Если есть .exe файл, прикрепите его
7. Нажмите "Publish release"

## Шаг 9: Настроить GitHub Pages (опционально)

Для документации:

1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: main, folder: /docs
4. Save

## Шаг 10: Добавить бейджи в README

Уже добавлены в README.md:
- Version badge
- Python version
- License

## Дополнительные файлы для GitHub

Уже созданы:
- ✅ README.md - Главная страница
- ✅ LICENSE - MIT лицензия
- ✅ .gitignore - Игнорируемые файлы
- ✅ CONTRIBUTING.md - Руководство для контрибьюторов
- ✅ requirements.txt - Зависимости

## Сборка .exe для Release

```bash
# Установить PyInstaller
pip install pyinstaller

# Собрать .exe
python build_exe.py

# Файл будет в dist/KHX-Editor.exe
```

## Структура репозитория

```
khx-lang/
├── .gitignore
├── LICENSE
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── editor.py
├── build_exe.py
├── src/
│   ├── khx.py
│   ├── khx_v5.py
│   └── [все модули]
├── examples/
│   ├── hello.khx
│   ├── calculator.khx
│   └── [другие примеры]
└── docs/
    ├── INSTALLATION.md
    └── API_REFERENCE.md
```

## Полезные команды Git

```bash
# Проверить статус
git status

# Добавить изменения
git add .

# Коммит
git commit -m "Update: описание изменений"

# Отправить на GitHub
git push

# Создать ветку
git checkout -b feature-name

# Переключиться на main
git checkout main

# Слить ветку
git merge feature-name
```

## Готово!

Ваш проект теперь на GitHub! 🎉

Поделитесь ссылкой:
```
https://github.com/YOUR_USERNAME/khx-lang
```
