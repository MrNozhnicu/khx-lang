# KHX Programming Language

<div align="center">

![KHX Logo](https://img.shields.io/badge/KHX-v5.0-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Современный язык программирования с 20+ встроенными модулями**

[Возможности](#-возможности) • [Установка](#-установка) • [Примеры](#-примеры) • [Документация](#-документация)

</div>

---

## 🚀 О проекте

KHX - это полнофункциональный язык программирования, созданный для быстрой разработки приложений любой сложности. От простых скриптов до сложных GUI приложений, игр, ML моделей и мобильных приложений.

### ✨ Ключевые особенности

- 🎨 **GUI Framework** - Создание графических интерфейсов
- 🗄️ **Database** - Работа с SQLite базами данных
- 🎮 **Game Engine** - 2D игровой движок
- 🤖 **Machine Learning** - Нейронные сети и NLP
- 📊 **Data Science** - DataFrame и визуализация
- 🔐 **Cryptography** - Шифрование и безопасность
- 📱 **Mobile Dev** - Android/iOS приложения
- 🧪 **Testing** - Unit тесты и бенчмарки
- 🔄 **Async/Await** - Асинхронное программирование
- 📦 **Package Manager** - Управление зависимостями
- 🎨 **Canvas** - 2D графика
- 🌍 **i18n** - Интернационализация
- 🔌 **Plugins** - Система плагинов
- 📝 **Templates** - HTML шаблонизатор
- 🗂️ **File Watcher** - Мониторинг файлов
- 🎯 **Events** - Система событий
- 🔍 **Debugging** - Отладка и профилирование
- 🌈 **CLI Tools** - Цветной вывод
- 🎵 **Audio/Video** - Обработка медиа
- 🌐 **Networking** - REST API и WebSocket

## 📦 Установка

### Из исходников

```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/khx-lang.git
cd khx-lang

# Установить зависимости
pip install -r requirements.txt

# Запустить редактор
python editor.py

# Или запустить программу
python khx_v5.py examples/hello.khx
```

### Скомпилированный редактор

Скачайте `KHX-Editor.exe` из [Releases](https://github.com/yourusername/khx-lang/releases) и запустите.

## 🎯 Быстрый старт

### Hello World

```khx
print("Hello, World!")
```

### Переменные и функции

```khx
let name = "KHX"
let version = 5.0

func greet(name: string) -> string {
    return "Hello, " + name + "!"
}

print(greet(name))
```

### GUI приложение

```khx
let win = create_window("My App", 800, 600)
add_label(win, "Welcome to KHX!")
add_button(win, "Click me")
show_window(win)
run_app(win)
```

### База данных

```khx
let db = connect_database("sqlite", "data.db")
db_execute(db, "CREATE TABLE users (id, name)")
db_execute(db, "INSERT INTO users VALUES (1, 'John')")
```

### Machine Learning

```khx
let model = create_neural_network()
let nlp = create_nlp()
let sentiment = nlp_sentiment(nlp, "I love KHX!")
print(sentiment)
```

## 📚 Документация

### Синтаксис

```khx
// Комментарии
let x = 10              // Переменные
let name = "John"       // Строки

// Функции с типами
func add(a: int, b: int) -> int {
    return a + b
}

// Условия
if (x > 5) {
    print("Больше 5")
} else {
    print("Меньше или равно 5")
}

// Циклы
while (x > 0) {
    print(x)
    x = x - 1
}

// Рекурсия
func factorial(n: int) -> int {
    if (n <= 1) {
        return 1
    }
    return n * factorial(n - 1)
}
```

### Модули

Полный список модулей и функций смотрите в [API Reference](docs/API_REFERENCE.md)

## 🎨 Редактор кода

KHX поставляется с полнофункциональным редактором кода:

- ✅ Подсветка синтаксиса
- ✅ Автодополнение
- ✅ Нумерация строк
- ✅ Файловый менеджер
- ✅ Вкладки
- ✅ Темная тема Dracula
- ✅ Встроенный терминал
- ✅ Запуск программ

```bash
python editor.py
```

## 📁 Структура проекта

```
khx-lang/
├── src/                    # Исходный код
│   ├── khx.py             # Базовый интерпретатор
│   ├── khx_v5.py          # v5.0 интерпретатор
│   └── modules/           # Все модули
├── examples/              # Примеры программ
├── docs/                  # Документация
├── editor.py              # Редактор кода
├── requirements.txt       # Зависимости
└── README.md             # Этот файл
```

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие KHX! 

1. Fork репозитория
2. Создайте ветку (`git checkout -b feature/amazing`)
3. Commit изменения (`git commit -m 'Add amazing feature'`)
4. Push в ветку (`git push origin feature/amazing`)
5. Откройте Pull Request

## 📊 Статус

| Модуль | Статус | Версия |
|--------|--------|--------|
| Core Interpreter | ✅ | 5.0 |
| GUI Framework | ✅ | 5.0 |
| Database | ✅ | 5.0 |
| Game Engine | ✅ | 5.0 |
| ML & NLP | ✅ | 5.0 |
| Data Science | ✅ | 5.0 |
| Cryptography | ✅ | 5.0 |
| Mobile Dev | ✅ | 5.0 |
| Testing | ✅ | 5.0 |
| Async/Await | ✅ | 5.0 |
| Package Manager | ✅ | 5.0 |
| Canvas | ✅ | 5.0 |
| i18n | ✅ | 5.0 |
| Plugins | ✅ | 5.0 |
| Templates | ✅ | 5.0 |
| File Watcher | ✅ | 5.0 |
| Events | ✅ | 5.0 |
| Debugging | ✅ | 5.0 |
| CLI Tools | ✅ | 5.0 |
| Audio/Video | ✅ | 5.0 |

**21/22 модулей загружены** (Network требует `pip install requests`)

## 📝 Лицензия

MIT License - смотрите [LICENSE](LICENSE) для деталей

## 🙏 Благодарности

- Python за отличный язык
- PyQt5 за GUI фреймворк
- Все контрибьюторы проекта

## 📞 Контакты

- GitHub: [@yourusername](https://github.com/MrNozhnicu)
- Issues: [GitHub Issues](https://github.com/MrNozhnicu/khx-lang/issues)

---

<div align="center">

**Сделано с ❤️ для разработчиков**

[⬆ Наверх](#khx-programming-language)

</div>
