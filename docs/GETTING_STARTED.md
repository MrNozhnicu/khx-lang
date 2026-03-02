# 🚀 Getting Started with KHX

Полное руководство для начинающих

## Содержание

1. [Установка](#установка)
2. [Первая программа](#первая-программа)
3. [Основы синтаксиса](#основы-синтаксиса)
4. [Работа с модулями](#работа-с-модулями)
5. [Следующие шаги](#следующие-шаги)

---

## Установка

### Вариант 1: Из исходников

```bash
# Клонировать репозиторий
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang

# Установить зависимости
pip install -r requirements.txt

# Установить KHX CLI
python khx_cli_installer.py
```

### Вариант 2: Только интерпретатор

```bash
# Запуск без установки
python src/khx_v5.py your_script.khx
```

### Вариант 3: GUI редактор

```bash
# Запустить визуальный редактор
python editor.py
```

---

## Первая программа

### Hello World

Создайте файл `hello.khx`:

```khx
// Мой первый KHX скрипт
print("Hello, World!")
print("Добро пожаловать в KHX!")
```

Запустите:

```bash
khx hello.khx
```

Вывод:
```
Hello, World!
Добро пожаловать в KHX!
```

### Переменные

```khx
// Объявление переменных
let name = "Alice"
let age = 25
let height = 1.75

print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)
```

### Математика

```khx
// Арифметические операции
let a = 10
let b = 5

print("Сумма:", a + b)        // 15
print("Разность:", a - b)     // 5
print("Произведение:", a * b) // 50
print("Частное:", a / b)      // 2
```

---

## Основы синтаксиса

### Комментарии

```khx
// Однострочный комментарий

/*
  Многострочный
  комментарий
*/
```

### Типы данных

```khx
// Числа
let integer = 42
let float_num = 3.14

// Строки
let text = "Hello"
let multiline = "Line 1
Line 2"

// Булевы значения
let is_true = true
let is_false = false

// Массивы
let numbers = [1, 2, 3, 4, 5]
let mixed = [1, "text", true]
```

### Условия

```khx
let age = 18

if age >= 18 {
    print("Взрослый")
} else {
    print("Ребенок")
}
```

### Циклы

```khx
// Цикл for
for i in range(5) {
    print("Итерация:", i)
}

// Цикл while
let count = 0
while count < 5 {
    print("Count:", count)
    count = count + 1
}
```

### Функции

```khx
// Объявление функции
function greet(name) {
    print("Привет,", name, "!")
}

// Вызов функции
greet("Alice")
greet("Bob")

// Функция с возвратом значения
function add(a, b) {
    return a + b
}

let result = add(5, 3)
print("Результат:", result)
```

---

## Работа с модулями

### GUI приложение

```khx
// Создать окно
let win = create_window("My App", 800, 600)

// Добавить элементы
add_label(win, "Добро пожаловать!")
add_button(win, "Нажми меня")
add_input(win, "Введите текст")

// Показать окно
show_window(win)
run_app(win)
```

### База данных

```khx
// Подключиться к БД
let db = connect_database("sqlite", "users.db")

// Создать таблицу
db_execute(db, "CREATE TABLE IF NOT EXISTS users (id, name, age)")

// Вставить данные
db_execute(db, "INSERT INTO users VALUES (1, 'Alice', 25)")
db_execute(db, "INSERT INTO users VALUES (2, 'Bob', 30)")

// Запрос
let results = db_query(db, "SELECT * FROM users")
print("Пользователи:", results)
```

### Игра

```khx
// Создать игру
let game = create_game(800, 600, "My Game")

// Добавить спрайты
let player = add_sprite(game, "player.png", 100, 100)
let enemy = add_sprite(game, "enemy.png", 400, 300)

// Установить фон
game_set_background(game, "blue")

// Запустить
run_game(game)
```

### Machine Learning

```khx
// NLP анализ
let nlp = create_nlp()

let text = "I love KHX! It's amazing and wonderful!"
let sentiment = nlp_sentiment(nlp, text)
print("Тональность:", sentiment)  // positive

let keywords = nlp_extract_keywords(nlp, text, 3)
print("Ключевые слова:", keywords)
```

---

## Следующие шаги

### Изучите примеры

```bash
# Посмотреть все примеры
khx --examples

# Запустить пример
khx examples/calculator.khx
khx examples/game.khx
khx examples/database.khx
```

### Создайте свой проект

```bash
# Создать новый проект
khx --new my_project

# Перейти в проект
cd my_project

# Запустить
khx src/main.khx
```

### Изучите документацию

- [API Reference](API_REFERENCE.md) - Все функции
- [Tutorials](TUTORIALS.md) - Подробные туториалы
- [Examples](../examples/) - Примеры кода
- [FAQ](FAQ.md) - Частые вопросы

### Интерактивный режим

```bash
# Запустить REPL
khx --repl

# Попробуйте:
khx> print("Hello!")
khx> let x = 10
khx> print(x * 2)
```

---

## Помощь

Нужна помощь? Вот ресурсы:

- **GitHub**: https://github.com/MrNozhnicu/khx-lang
- **Issues**: https://github.com/MrNozhnicu/khx-lang/issues
- **Документация**: [docs/](.)

---

**Готовы к большему? Переходите к [Tutorials](TUTORIALS.md)!**
