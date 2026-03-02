# KHX Programming Language v5.2

<div align="center">

![KHX Logo](https://img.shields.io/badge/KHX-v5.2-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Modules](https://img.shields.io/badge/Modules-22-orange?style=for-the-badge)
![Functions](https://img.shields.io/badge/Functions-300+-red?style=for-the-badge)

**Современный язык программирования с 22 модулями и 300+ функциями**

[Возможности](#-возможности) • [Установка](#-установка) • [CLI](#-khx-cli) • [Примеры](#-примеры) • [Документация](#-документация)

</div>

---

## 🚀 О проекте

KHX - это полнофункциональный язык программирования, созданный для быстрой разработки приложений любой сложности. От простых скриптов до сложных GUI приложений, игр, ML моделей и мобильных приложений.

### 🎯 Почему KHX?

- ✅ **Все в одном**: 22 модуля из коробки - не нужно искать библиотеки
- ✅ **Простой синтаксис**: Легко учить, легко читать
- ✅ **Быстрая разработка**: Меньше кода, больше результата
- ✅ **Кросс-платформенность**: Windows, Linux, macOS
- ✅ **Open Source**: MIT License - используйте как хотите
- ✅ **CLI инструмент**: Работайте прямо в терминале
- ✅ **GUI редактор**: Визуальная среда разработки
- ✅ **Богатая документация**: Туториалы, примеры, FAQ

---

## ✨ Возможности

### 22 встроенных модуля

| Модуль | Функций | Описание |
|--------|---------|----------|
| 🎨 **GUI Framework** | 20+ | Создание графических интерфейсов |
| 🗄️ **Database** | 15+ | SQLite с ORM и транзакциями |
| 🎮 **Game Engine** | 25+ | 2D игры с физикой и коллизиями |
| 🤖 **Machine Learning** | 30+ | Нейросети, NLP, анализ текста |
| 📊 **Data Science** | 22+ | DataFrame, визуализация, статистика |
| 🔐 **Cryptography** | 20+ | Хеширование, JWT, шифрование |
| 📱 **Mobile Dev** | 25+ | Android/iOS приложения |
| 🧪 **Testing** | 15+ | Unit тесты, моки, бенчмарки |
| 🔄 **Async/Await** | 10+ | Асинхронное программирование |
| 📦 **Package Manager** | 10+ | Управление зависимостями |
| 🎨 **Canvas** | 15+ | 2D графика и анимации |
| 🌍 **i18n** | 8+ | Интернационализация |
| 🔌 **Plugins** | 10+ | Система плагинов |
| 📝 **Templates** | 8+ | HTML шаблонизатор |
| 🗂️ **File Watcher** | 6+ | Мониторинг файлов |
| 🎯 **Events** | 8+ | Система событий |
| 🔍 **Debugging** | 12+ | Отладка и профилирование |
| 🌈 **CLI Tools** | 12+ | Цветной вывод, прогресс-бары |
| 🎵 **Audio/Video** | 20+ | Обработка медиа, микшер |
| 🌐 **Network** | 10+ | REST API, WebSocket |
| 💻 **OS Integration** | 15+ | Файлы, процессы, система |
| 🌐 **Web Server** | 10+ | HTTP сервер с роутингом |

**Итого**: 300+ функций для любых задач!

---

## 📦 Установка

### Вариант 1: Полная установка с CLI

```bash
# Клонировать репозиторий
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang

# Установить зависимости
pip install -r requirements.txt

# Установить KHX CLI
python khx_cli_installer.py
```

После установки команда `khx` будет доступна везде!

### Вариант 2: Только интерпретатор

```bash
# Запуск без установки
python src/khx_v5.py your_script.khx
```

### Вариант 3: GUI редактор

```bash
# Визуальный редактор кода
python editor.py
```

### Вариант 4: Собрать .exe (Windows)

```bash
pip install pyinstaller
python build_exe.py
```

Результат: `dist/KHX-Editor.exe` (49 MB)

---

## 💻 KHX CLI

### Основные команды

```bash
# Запустить программу
khx script.khx

# Интерактивный режим
khx --repl

# Создать новый проект
khx --new my_project

# Проверить синтаксис
khx --check script.khx

# Показать примеры
khx --examples

# Открыть документацию
khx --docs

# Показать версию
khx --version

# Справка
khx --help
```

### Интерактивный режим (REPL)

```bash
$ khx --repl
KHX REPL v5.2
Введите 'exit' для выхода
----------------------------------------
khx> print("Hello, World!")
Hello, World!

khx> let x = 10
khx> print(x * 2)
20

khx> exit
До свидания!
```

### Создание проекта

```bash
$ khx --new my_app
Создание проекта: my_app
✅ Проект создан: my_app/
   - src/main.khx
   - README.md

Запуск:
  cd my_app
  khx src/main.khx
```

Подробнее: [CLI Guide](docs/CLI_GUIDE.md)

---

## 🎯 Быстрый старт

```bash
# 1. Установить
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang
pip install -r requirements.txt
python khx_cli_installer.py

# 2. Попробовать REPL
khx --repl

# 3. Создать проект
khx --new hello_app
cd hello_app

# 4. Запустить
khx src/main.khx
```

---

## 📚 Документация

### Для начинающих

- 🚀 [Getting Started](docs/GETTING_STARTED.md) - Начало работы (30 мин)
- 📖 [Tutorials](docs/TUTORIALS.md) - 8 подробных туториалов (2-3 часа)
- ❓ [FAQ](docs/FAQ.md) - 50+ частых вопросов
- 💻 [CLI Guide](docs/CLI_GUIDE.md) - Руководство по CLI

### Справочники

- 📘 [API Reference](docs/API_REFERENCE.md) - Все 300+ функций
- 📦 [Installation](docs/INSTALLATION.md) - Установка

### Для разработчиков

- 🤝 [Contributing](CONTRIBUTING.md) - Как внести вклад

---

## 📊 Статистика

- **Версия**: 5.2.0
- **Модулей**: 22 (21 работают, 1 требует `requests`)
- **Функций**: 300+
- **Примеров**: 17 программ
- **Строк кода**: 12,000+
- **Документов**: 20+ файлов
- **Тесты**: Все проходят ✅

---

## 🗺️ Roadmap

### v5.2 (Текущая) ✅
- ✅ KHX CLI инструмент
- ✅ 300+ функций
- ✅ 20+ документов
- ✅ Интерактивный REPL

### v5.3 (Планируется)
- 🔄 Оптимизация производительности
- 🔄 Больше примеров
- 🔄 Видео туториалы
- 🔄 Онлайн playground

### v6.0 (Будущее)
- 🔮 JIT компиляция
- 🔮 Нативный код
- 🔮 Поддержка MySQL/PostgreSQL
- 🔮 Веб-фреймворк
- 🔮 Package registry

---

## 📝 Лицензия

MIT License - см. [LICENSE](LICENSE)

---

## 📞 Контакты

- **GitHub**: https://github.com/MrNozhnicu/khx-lang
- **Issues**: https://github.com/MrNozhnicu/khx-lang/issues
- **Документация**: [docs/](docs/)

---

<div align="center">

**Сделано с ❤️ для разработчиков**

**Star ⭐ this repo if you like it!**

[⬆ Наверх](#khx-programming-language-v52)

</div>
