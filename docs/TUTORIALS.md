# 📚 KHX Tutorials

Подробные туториалы по всем возможностям KHX

## Содержание

1. [Создание GUI приложения](#1-создание-gui-приложения)
2. [Работа с базами данных](#2-работа-с-базами-данных)
3. [Разработка игры](#3-разработка-игры)
4. [Machine Learning](#4-machine-learning)
5. [Мобильное приложение](#5-мобильное-приложение)
6. [Data Science](#6-data-science)
7. [Работа с аудио](#7-работа-с-аудио)
8. [Криптография](#8-криптография)

---

## 1. Создание GUI приложения

### Простое окно

```khx
// Создать окно
let win = create_window("Калькулятор", 400, 300)

// Добавить элементы
add_label(win, "Простой калькулятор")
add_input(win, "Число 1")
add_input(win, "Число 2")
add_button(win, "Сложить")
add_label(win, "Результат: 0")

// Показать
show_window(win)
run_app(win)
```

### Калькулятор с логикой

```khx
let win = create_window("Калькулятор", 400, 300)

// Поля ввода
let input1 = add_input(win, "Число 1")
let input2 = add_input(win, "Число 2")

// Кнопки операций
add_button(win, "+")
add_button(win, "-")
add_button(win, "*")
add_button(win, "/")

// Результат
let result_label = add_label(win, "Результат: ")

show_window(win)
run_app(win)
```

---

## 2. Работа с базами данных

### Создание таблицы

```khx
// Подключение
let db = connect_database("sqlite", "myapp.db")

// Создать таблицу пользователей
db_execute(db, "CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)")

print("Таблица создана!")
```

### CRUD операции

```khx
// CREATE - Создание
db_execute(db, "INSERT INTO users (name, email, age) VALUES ('Alice', 'alice@example.com', 25)")
db_execute(db, "INSERT INTO users (name, email, age) VALUES ('Bob', 'bob@example.com', 30)")

// READ - Чтение
let all_users = db_query(db, "SELECT * FROM users")
print("Все пользователи:", all_users)

let alice = db_query(db, "SELECT * FROM users WHERE name = 'Alice'")
print("Alice:", alice)

// UPDATE - Обновление
db_execute(db, "UPDATE users SET age = 26 WHERE name = 'Alice'")

// DELETE - Удаление
db_execute(db, "DELETE FROM users WHERE name = 'Bob'")
```

### Транзакции

```khx
// Начать транзакцию
db_begin_transaction(db)

try {
    db_execute(db, "INSERT INTO users (name, email) VALUES ('Charlie', 'charlie@example.com')")
    db_execute(db, "INSERT INTO users (name, email) VALUES ('David', 'david@example.com')")
    
    // Подтвердить
    db_commit(db)
    print("Транзакция успешна!")
} catch {
    // Откатить при ошибке
    db_rollback(db)
    print("Ошибка! Откат транзакции")
}
```

---

## 3. Разработка игры

### Простая игра

```khx
// Создать игру
let game = create_game(800, 600, "Space Shooter")

// Игрок
let player = add_sprite(game, "player.png", 400, 500)

// Враги
let enemy1 = game_spawn_enemy(game, 100, 50, "basic")
let enemy2 = game_spawn_enemy(game, 300, 50, "basic")
let enemy3 = game_spawn_enemy(game, 500, 50, "basic")

// Настройки
game_set_background(game, "black")
game_set_gravity(game, 0)

// Обработка клавиш
game_on_key_press(game, "left", function() {
    sprite_move(player, -10, 0)
})

game_on_key_press(game, "right", function() {
    sprite_move(player, 10, 0)
})

game_on_key_press(game, "space", function() {
    // Выстрел
    let bullet = add_sprite(game, "bullet.png", player.x, player.y)
    sprite_set_velocity(bullet, 0, -10)
})

// Запустить
run_game(game)
```

### Система очков и уровней

```khx
let game = create_game(800, 600, "My Game")
let score = 0
let level = 1

// Добавить очки
function add_points(points) {
    score = score + points
    game_add_score(game, points)
    
    // Проверка уровня
    if score >= level * 100 {
        level = level + 1
        game_next_level(game)
        print("Уровень", level, "!")
    }
}

// При уничтожении врага
function on_enemy_destroyed() {
    add_points(10)
}
```

---

## 4. Machine Learning

### Анализ тональности

```khx
let nlp = create_nlp()

// Анализ отзывов
let reviews = [
    "This product is amazing! I love it!",
    "Terrible quality, waste of money",
    "It's okay, nothing special",
    "Excellent! Highly recommended!",
    "Worst purchase ever"
]

for review in reviews {
    let sentiment = nlp_sentiment(nlp, review)
    print(review, "->", sentiment)
}
```

### Извлечение ключевых слов

```khx
let nlp = create_nlp()

let article = "Machine learning is a subset of artificial intelligence. 
It focuses on teaching computers to learn from data. 
Deep learning is a type of machine learning using neural networks."

// Топ-5 ключевых слов
let keywords = nlp_extract_keywords(nlp, article, 5)
print("Ключевые слова:", keywords)

// Частота слов
let frequency = nlp_word_frequency(nlp, article)
print("Частота:", frequency)
```

### Нейронная сеть

```khx
// Создать сеть: 2 входа, 3 скрытых, 1 выход
let nn = create_neural_network([2, 3, 1])

// Обучающие данные
let training_data = [
    [[0, 0], [0]],
    [[0, 1], [1]],
    [[1, 0], [1]],
    [[1, 1], [0]]
]

// Обучить
nn_train(nn, training_data, epochs=1000, learning_rate=0.1)

// Предсказание
let result = nn_predict(nn, [1, 0])
print("Предсказание:", result)

// Сохранить модель
nn_save_model(nn, "xor_model.khx")
```

---

## 5. Мобильное приложение

### Простое приложение

```khx
// Создать приложение
let app = create_mobile_app("MyPhotoApp")

// Запросить разрешения
app_request_permission(app, "CAMERA")
app_request_permission(app, "STORAGE")

// Главный экран
let home = app_add_screen(app, "home")
screen_add_text(home, "Фото приложение", size=24)
screen_add_button(home, "Сделать фото")
screen_add_button(home, "Галерея")

// Сделать фото
function take_photo() {
    let photo = camera_take_photo(app.camera)
    screen_show_image(home, photo)
    
    // Уведомление
    app_send_notification(app, "Фото", "Фото сохранено!")
    
    // Вибрация
    app_vibrate(app, 100)
}

// Собрать
app_build_android(app)
app_build_ios(app)
```

### GPS и карты

```khx
let app = create_mobile_app("MapApp")

// Получить координаты
let location = gps_get_location(app.gps)
print("Координаты:", location.lat, location.lon)

// Адрес
let address = gps_get_address(app.gps, location.lat, location.lon)
print("Адрес:", address)

// Расстояние между точками
let moscow = [55.7558, 37.6173]
let spb = [59.9343, 30.3351]
let distance = gps_get_distance(app.gps, moscow[0], moscow[1], spb[0], spb[1])
print("Расстояние Москва-СПб:", distance, "км")
```

---

## 6. Data Science

### Анализ данных

```khx
// Создать DataFrame
let data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
    {"name": "David", "age": 28, "salary": 55000}
]

let df = create_dataframe(data)

// Статистика
print("Средний возраст:", df_mean(df, "age"))
print("Средняя зарплата:", df_mean(df, "salary"))
print("Макс зарплата:", df_max(df, "salary"))

// Сортировка
df = df_sort_by(df, "salary", ascending=false)
print("Топ по зарплате:", df_head(df, 3))

// Корреляция
let corr = df_corr(df, "age", "salary")
print("Корреляция возраст-зарплата:", corr)
```

### Визуализация

```khx
// Данные продаж
let sales = [100, 150, 120, 180, 200, 170, 190]
let days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

// Столбчатая диаграмма
plot_bar(sales, days)

// Линейный график
plot_line(sales)

// Гистограмма
let ages = [25, 30, 35, 28, 32, 29, 31, 27, 33, 26]
plot_histogram(ages, bins=5)
```

---

## 7. Работа с аудио

### Воспроизведение

```khx
// Загрузить аудио
let music = load_audio("song.mp3")

// Настройки
audio_set_volume(music, 0.8)
audio_set_loop(music, true)

// Воспроизведение
audio_play(music)

// Пауза через 10 секунд
sleep(10)
audio_pause(music)

// Возобновить
audio_play(music)
```

### Эффекты и обработка

```khx
let audio = load_audio("voice.mp3")

// Применить эффекты
audio_apply_effect(audio, "reverb", 0.7)
audio_apply_effect(audio, "echo", 0.5)

// Fade эффекты
audio_fade_in(audio, 2.0)
sleep(30)
audio_fade_out(audio, 3.0)

// Обрезать
audio_trim(audio, 10, 60)  // С 10 по 60 секунду

// Нормализовать громкость
audio_normalize(audio)

// Экспорт
audio_export(audio, "processed", "wav")
```

### Микшер

```khx
// Создать микшер
let mixer = create_mixer()

// Добавить треки
let track1 = load_audio("drums.mp3")
let track2 = load_audio("bass.mp3")
let track3 = load_audio("guitar.mp3")

mixer_add_track(mixer, track1)
mixer_add_track(mixer, track2)
mixer_add_track(mixer, track3)

// Общая громкость
mixer_set_volume(mixer, 0.9)

// Воспроизвести все
mixer_play_all(mixer)
```

---

## 8. Криптография

### Хеширование

```khx
let password = "mySecretPassword123"

// Различные хеши
let sha256_hash = sha256(password)
let md5_hash = md5(password)
let sha512_hash = sha512(password)

print("SHA-256:", sha256_hash)
print("MD5:", md5_hash)
print("SHA-512:", sha512_hash)
```

### JWT токены

```khx
// Создать токен
let payload = {
    "user_id": 123,
    "username": "alice",
    "role": "admin"
}

let secret = "my_secret_key"
let token = create_jwt(payload, secret, expiry_hours=24)
print("Token:", token)

// Проверить токен
let is_valid = verify_jwt(token, secret)
print("Valid:", is_valid)

// Декодировать
let decoded = decode_jwt(token)
print("Payload:", decoded)
```

### Пароли

```khx
// Хешировать пароль
let password = "userPassword123"
let hashed = hash_password(password)
print("Hashed:", hashed)

// Проверить пароль
let is_correct = verify_password("userPassword123", hashed)
print("Correct:", is_correct)  // true

let is_wrong = verify_password("wrongPassword", hashed)
print("Wrong:", is_wrong)  // false
```

---

## Следующие шаги

- Изучите [API Reference](API_REFERENCE.md) для полного списка функций
- Посмотрите [примеры](../examples/) для вдохновения
- Создайте свой проект: `khx --new my_project`

**Удачи в разработке на KHX! 🚀**
