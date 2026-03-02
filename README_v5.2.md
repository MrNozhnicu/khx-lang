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

## 🎯 Примеры

### Hello World

```khx
print("Hello, World!")
print("Добро пожаловать в KHX!")
```

### GUI приложение

```khx
// Создать окно
let win = create_window("Калькулятор", 400, 300)

// Добавить элементы
add_label(win, "Простой калькулятор")
add_input(win, "Число 1")
add_input(win, "Число 2")
add_button(win, "Сложить")

// Показать
show_window(win)
run_app(win)
```

### База данных

```khx
// Подключиться
let db = connect_database("sqlite", "users.db")

// Создать таблицу
db_execute(db, "CREATE TABLE users (id, name, age)")

// Вставить данные
db_execute(db, "INSERT INTO users VALUES (1, 'Alice', 25)")

// Запрос
let users = db_query(db, "SELECT * FROM users")
print(users)
```

### Игра

```khx
// Создать игру
let game = create_game(800, 600, "Space Shooter")

// Игрок
let player = add_sprite(game, "player.png", 400, 500)

// Враги
game_spawn_enemy(game, 100, 50, "basic")
game_spawn_enemy(game, 300, 50, "basic")

// Управление
game_on_key_press(game, "left", function() {
    sprite_move(player, -10, 0)
})

game_on_key_press(game, "right", function() {
    sprite_move(player, 10, 0)
})

// Запустить
run_game(game)
```

### Machine Learning

```khx
// NLP анализ
let nlp = create_nlp()

let text = "I love KHX! It's amazing and wonderful!"

// Тональность
let sentiment = nlp_sentiment(nlp, text)
print("Тональность:", sentiment)  // positive

// Ключевые слова
let keywords = nlp_extract_keywords(nlp, text, 3)
print("Ключевые слова:", keywords)

// Схожесть текстов
let text2 = "KHX is great and awesome!"
let similarity = nlp_text_similarity(nlp, text, text2)
print("Схожесть:", similarity)
```

### Data Science

```khx
// Создать DataFrame
let data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000}
]

let df = create_dataframe(data)

// Анализ
print("Средний возраст:", df_mean(df, "age"))
print("Средняя зарплата:", df_mean(df, "salary"))

// Сортировка
df = df_sort_by(df, "salary", ascending=false)

// Корреляция
let corr = df_corr(df, "age", "salary")
print("Корреляция:", corr)

// Визуализация
plot_bar([50000, 60000, 70000], ["Alice", "Bob", "Charlie"])
```

### Мобильное приложение

```khx
// Создать приложение
let app = create_mobile_app("PhotoApp")

// Разрешения
app_request_permission(app, "CAMERA")
app_request_permission(app, "STORAGE")

// Экран
let home = app_add_screen(app, "home")
screen_add_button(home, "Сделать фото")

// Камера
let photo = camera_take_photo(app.camera)
camera_apply_filter(app.camera, "sepia")

// GPS
let location = gps_get_location(app.gps)
print("Координаты:", location.lat, location.lon)

// Собрать
app_build_android(app)
```

### Аудио обработка

```khx
// Загрузить аудио
let audio = load_audio("song.mp3")

// Эффекты
audio_apply_effect(audio, "reverb", 0.7)
audio_fade_in(audio, 2.0)

// Воспроизведение
audio_set_loop(audio, true)
audio_play(audio)

// Микшер
let mixer = create_mixer()
mixer_add_track(mixer, audio)
mixer_set_volume(mixer, 0.8)
mixer_play_all(mixer)

// Экспорт
audio_export(audio, "output", "wav")
```

Больше примеров: [examples/](examples/)

---

## 📚 Документация

### Для начинающих

- 🚀 [Getting Started](docs/GETTING_STARTED.md) - Начало работы
- 📖 [Tutorials](docs/TUTORIALS.md) - Подробные туториалы
- ❓ [FAQ](docs/FAQ.md) - Частые вопросы
- 💻 [CLI Guide](docs/CLI_GUIDE.md) - Руководство по CLI

### Справочники

- 📘 [API Reference](docs/API_REFERENCE.md) - Все функции (300+)
- 📦 [Installation Guide](docs/INSTALLATION.md) - Установка
- 🔧 [Configuration](docs/CONFIGURATION.md) - Настройка

### Для разработчиков

- 🤝 [Contributing](CONTRIBUTING.md) - Как внести вклад
- 🏗️ [Architecture](docs/ARCHITECTURE.md) - Архитектура
- 🔌 [Plugin Development](docs/PLUGINS.md) - Создание плагинов

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

## 🎓 Обучение

### Быстрый старт (5 минут)

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

### Учебные материалы

1. [Getting Started](docs/GETTING_STARTED.md) - Основы (30 мин)
2. [Tutorials](docs/TUTORIALS.md) - 8 подробных туториалов (2-3 часа)
3. [Examples](examples/) - 17 рабочих примеров
4. [API Reference](docs/API_REFERENCE.md) - Полный справочник

---

## 🛠️ Разработка

### Структура проекта

```
khx-lang/
├── src/                    # Исходный код интерпретатора
│   ├── khx_v5.py          # Главный интерпретатор
│   ├── khx_gui.py         # GUI модуль
│   ├── khx_database.py    # Database модуль
│   ├── khx_ml.py          # Machine Learning
│   └── ...                # Остальные модули (22 всего)
├── examples/              # Примеры программ (17 файлов)
├── docs/                  # Документация (20+ файлов)
├── editor.py              # GUI редактор
├── khx                    # CLI скрипт (Unix)
├── khx.bat                # CLI скрипт (Windows)
├── khx_cli_installer.py   # Установщик CLI
├── build_exe.py           # Сборка .exe
└── README.md              # Этот файл
```

### Запуск тестов

```bash
python src/khx_v5.py examples/hello.khx
python src/khx_v5.py examples/calculator.khx
python src/khx_v5.py examples/database.khx
```

### Сборка .exe

```bash
pip install pyinstaller
python build_exe.py
```

---

## 🤝 Вклад в проект

Мы приветствуем вклад! См. [CONTRIBUTING.md](CONTRIBUTING.md)

### Как помочь

- 🐛 Сообщить об ошибке
- 💡 Предложить новую функцию
- 📝 Улучшить документацию
- 🔧 Исправить баг
- ✨ Добавить новый модуль

### Создать Issue

https://github.com/MrNozhnicu/khx-lang/issues

---

## 📝 Лицензия

MIT License - см. [LICENSE](LICENSE)

Вы можете:
- ✅ Использовать в коммерческих проектах
- ✅ Модифицировать код
- ✅ Распространять
- ✅ Использовать в частных проектах

---

## 🌟 Поддержка проекта

Если вам нравится KHX:

- ⭐ Поставьте звезду на GitHub
- 🐦 Расскажите в соцсетях
- 📝 Напишите статью/туториал
- 🤝 Внесите вклад в код

---

## 📞 Контакты

- **GitHub**: https://github.com/MrNozhnicu/khx-lang
- **Issues**: https://github.com/MrNozhnicu/khx-lang/issues
- **Документация**: [docs/](docs/)

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

<div align="center">

**Сделано с ❤️ для разработчиков**

[⬆ Наверх](#khx-programming-language-v52)

</div>
