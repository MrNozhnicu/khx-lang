# ❓ FAQ - Frequently Asked Questions

Часто задаваемые вопросы о KHX

## Общие вопросы

### Что такое KHX?

KHX - это современный язык программирования с 22 встроенными модулями и 300+ функциями. Он создан для быстрой разработки приложений любой сложности: от простых скриптов до GUI приложений, игр, ML моделей и мобильных приложений.

### Зачем использовать KHX?

- ✅ **Все в одном**: 22 модуля из коробки (GUI, Database, ML, Games и др.)
- ✅ **Простой синтаксис**: Легко учить и использовать
- ✅ **Быстрая разработка**: Меньше кода, больше результата
- ✅ **Кросс-платформенность**: Windows, Linux, macOS
- ✅ **Open Source**: MIT License

### Какая версия Python нужна?

Python 3.8 или выше.

### Как установить KHX?

```bash
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang
pip install -r requirements.txt
python khx_cli_installer.py
```

---

## Установка и настройка

### Как установить KHX CLI?

```bash
python khx_cli_installer.py
```

После установки команда `khx` будет доступна в терминале.

### Как удалить KHX CLI?

```bash
python khx_cli_installer.py uninstall
```

### KHX CLI не работает после установки

**Windows**: Добавьте путь в PATH:
1. Система → Дополнительные параметры → Переменные среды
2. Path → Изменить → Добавить путь из вывода установщика

**Linux/macOS**: Перезапустите терминал или выполните:
```bash
source ~/.bashrc  # или ~/.zshrc
```

### Можно ли использовать KHX без установки?

Да! Запускайте напрямую:
```bash
python src/khx_v5.py your_script.khx
```

---

## Использование

### Как запустить программу?

```bash
khx your_script.khx
```

### Как создать новый проект?

```bash
khx --new my_project
cd my_project
khx src/main.khx
```

### Как открыть интерактивный режим?

```bash
khx --repl
```

### Как проверить синтаксис без запуска?

```bash
khx --check script.khx
```

### Где найти примеры?

В папке `examples/`:
```bash
khx --examples
khx examples/hello.khx
```

---

## Модули и функции

### Какие модули доступны?

22 модуля:
- GUI Framework
- Database (SQLite)
- Machine Learning & NLP
- 2D Game Engine
- Mobile Development
- Cryptography
- Data Science
- Testing Framework
- Async/Await
- Canvas API
- CLI Tools
- Audio/Video
- Package Manager
- i18n
- Plugin System
- Template Engine
- File Watcher
- Event System
- Debugging Tools
- Network (HTTP)
- OS Integration
- Web Server

### Как узнать все функции модуля?

См. [API Reference](API_REFERENCE.md)

### Модуль Network не работает

Установите библиотеку `requests`:
```bash
pip install requests
```

### Как импортировать внешние библиотеки Python?

KHX работает поверх Python, поэтому можно использовать любые Python библиотеки через интерпретатор.

---

## GUI приложения

### Как создать окно?

```khx
let win = create_window("My App", 800, 600)
add_label(win, "Hello!")
show_window(win)
run_app(win)
```

### Какие элементы GUI доступны?

- Окна (windows)
- Кнопки (buttons)
- Текстовые поля (labels)
- Поля ввода (inputs)
- Списки (lists)
- Меню (menus)

### Как обработать нажатие кнопки?

```khx
let btn = add_button(win, "Click me")
on_button_click(btn, function() {
    print("Button clicked!")
})
```

---

## База данных

### Какие БД поддерживаются?

Сейчас только SQLite. Поддержка MySQL/PostgreSQL планируется в v6.0.

### Как создать таблицу?

```khx
let db = connect_database("sqlite", "mydb.db")
db_execute(db, "CREATE TABLE users (id, name, email)")
```

### Как сделать запрос?

```khx
let results = db_query(db, "SELECT * FROM users WHERE age > 18")
print(results)
```

### Поддерживаются ли транзакции?

Да:
```khx
db_begin_transaction(db)
// ... операции ...
db_commit(db)  // или db_rollback(db)
```

---

## Machine Learning

### Какие ML модели доступны?

- Нейронные сети (Neural Networks)
- Линейная регрессия (Linear Regression)
- NLP (Natural Language Processing)

### Как обучить нейросеть?

```khx
let nn = create_neural_network([2, 3, 1])
nn_train(nn, training_data, epochs=1000)
let prediction = nn_predict(nn, [1, 0])
```

### Как анализировать текст?

```khx
let nlp = create_nlp()
let sentiment = nlp_sentiment(nlp, "I love this!")
let keywords = nlp_extract_keywords(nlp, text, 5)
```

---

## Игры

### Как создать игру?

```khx
let game = create_game(800, 600, "My Game")
let player = add_sprite(game, "player.png", 100, 100)
run_game(game)
```

### Как обрабатывать клавиши?

```khx
game_on_key_press(game, "space", function() {
    print("Space pressed!")
})
```

### Как проверить столкновения?

```khx
let collisions = game_check_collisions(game)
for collision in collisions {
    print("Collision detected!")
}
```

---

## Мобильные приложения

### Для каких платформ можно разрабатывать?

Android и iOS.

### Как собрать APK?

```khx
let app = create_mobile_app("MyApp")
// ... добавить экраны ...
app_build_android(app)
```

### Нужен ли Android Studio?

Нет, KHX генерирует готовый APK/IPA.

---

## Производительность

### Насколько быстр KHX?

KHX работает поверх Python, поэтому производительность сравнима с Python. Для критичных участков планируется JIT-компиляция в v6.0.

### Можно ли скомпилировать в нативный код?

Пока нет, но планируется в v6.0.

### Как оптимизировать код?

- Используйте встроенные функции (они оптимизированы)
- Избегайте вложенных циклов
- Кешируйте результаты
- Используйте async для I/O операций

---

## Ошибки и отладка

### Как отладить программу?

```khx
debug_log("Debug message")
debug_breakpoint()  // Точка останова
```

### Как профилировать код?

```khx
profile_start("my_function")
// ... код ...
profile_end("my_function")
profile_report()
```

### Где посмотреть логи?

Логи выводятся в консоль. Используйте `debug_log()` для отладочных сообщений.

---

## Разработка

### Как внести вклад в проект?

См. [CONTRIBUTING.md](../CONTRIBUTING.md)

### Где сообщить об ошибке?

GitHub Issues: https://github.com/MrNozhnicu/khx-lang/issues

### Можно ли создать свой модуль?

Да! См. документацию по Plugin System.

---

## Лицензия

### Какая лицензия у KHX?

MIT License - можно использовать в коммерческих проектах.

### Можно ли продавать приложения на KHX?

Да, без ограничений.

---

## Дополнительные ресурсы

- **Документация**: [docs/](.)
- **Примеры**: [examples/](../examples/)
- **GitHub**: https://github.com/MrNozhnicu/khx-lang
- **API Reference**: [API_REFERENCE.md](API_REFERENCE.md)
- **Tutorials**: [TUTORIALS.md](TUTORIALS.md)

---

**Не нашли ответ? Создайте Issue на GitHub!**
