# KHX API Reference

Полный справочник по всем функциям KHX v5.0

## Базовые функции

### print(text)
Вывод текста в консоль
```khx
print("Hello, World!")
```

### sleep(seconds)
Пауза выполнения
```khx
sleep(1.0)  // Пауза 1 секунда
```

### random()
Случайное число от 0 до 1
```khx
let r = random()
```

### time()
Текущее время (Unix timestamp)
```khx
let t = time()
```

---

## 1. GUI Framework

### create_window(title, width, height)
Создать окно
```khx
let win = create_window("My App", 800, 600)
```

### add_label(window_id, text)
Добавить текст
```khx
add_label(win, "Hello!")
```

### add_button(window_id, text)
Добавить кнопку
```khx
add_button(win, "Click me")
```

### add_input(window_id, placeholder)
Добавить поле ввода
```khx
add_input(win, "Enter text")
```

### show_window(window_id)
Показать окно
```khx
show_window(win)
```

### run_app(window_id)
Запустить приложение
```khx
run_app(win)
```

---

## 2. Database

### connect_database(type, connection)
Подключиться к БД
```khx
let db = connect_database("sqlite", "data.db")
```

### db_execute(db_id, sql)
Выполнить SQL
```khx
db_execute(db, "CREATE TABLE users (id, name)")
```

---

## 3. Game Engine

### create_game(width, height, title)
Создать игру
```khx
let game = create_game(800, 600, "My Game")
```

### add_sprite(game_id, image, x, y)
Добавить спрайт
```khx
add_sprite(game, "player.png", 100, 100)
```

### run_game(game_id)
Запустить игру
```khx
run_game(game)
```

---

## 4. Machine Learning

### create_neural_network()
Создать нейросеть
```khx
let model = create_neural_network()
```

### create_nlp()
Создать NLP модель
```khx
let nlp = create_nlp()
```

### nlp_sentiment(nlp_id, text)
Анализ тональности
```khx
let sentiment = nlp_sentiment(nlp, "I love KHX!")
```

---

## 5. Data Science

### create_dataframe()
Создать DataFrame
```khx
let df = create_dataframe()
```

### plot_bar()
Столбчатая диаграмма
```khx
plot_bar()
```

### plot_line()
Линейный график
```khx
plot_line()
```

---

## 6. Audio/Video

### load_audio(filename)
Загрузить аудио
```khx
let audio = load_audio("song.mp3")
```

### audio_play(audio_id)
Воспроизвести
```khx
audio_play(audio)
```

### audio_effect(audio_id, effect, intensity)
Применить эффект
```khx
audio_effect(audio, "reverb", 0.7)
```

### load_video(filename)
Загрузить видео
```khx
let video = load_video("movie.mp4")
```

### video_subtitle(video_id, text, start, duration)
Добавить субтитры
```khx
video_subtitle(video, "Hello", 5, 3)
```

### video_export(video_id, filename)
Экспортировать видео
```khx
video_export(video, "output.mp4")
```

---

## 7. Cryptography

### sha256(text)
SHA256 хеш
```khx
let hash = sha256("password")
```

### md5(text)
MD5 хеш
```khx
let hash = md5("data")
```

### generate_token(length)
Генерация токена
```khx
let token = generate_token(32)
```

### create_jwt(secret)
Создать JWT
```khx
let jwt = create_jwt("secret_key")
```

### hash_password(password)
Хеш пароля
```khx
let hashed = hash_password("mypassword")
```

---

## 8. Mobile Development

### create_mobile_app(name)
Создать приложение
```khx
let app = create_mobile_app("MyApp")
```

### add_screen(app_id, name)
Добавить экран
```khx
let screen = add_screen(app, "home")
```

### build_android(app_id)
Собрать для Android
```khx
build_android(app)
```

---

## 9. Testing

### create_test_suite(name)
Создать набор тестов
```khx
let tests = create_test_suite("MyTests")
```

### assert_equal(actual, expected)
Проверка равенства
```khx
assert_equal(5, 5)
```

---

## 10. Async/Await

### create_channel()
Создать канал
```khx
let channel = create_channel()
```

### async_sleep(seconds)
Асинхронная пауза
```khx
async_sleep(1.0)
```

---

## 11. Package Manager

### install_package(name)
Установить пакет
```khx
install_package("http")
```

### uninstall_package(name)
Удалить пакет
```khx
uninstall_package("old-lib")
```

### list_packages()
Список пакетов
```khx
list_packages()
```

### search_packages(query)
Поиск пакетов
```khx
search_packages("json")
```

---

## 12. Canvas

### create_canvas(width, height)
Создать холст
```khx
let canvas = create_canvas(800, 600)
```

### draw_circle(canvas_id, x, y, radius)
Нарисовать круг
```khx
draw_circle(canvas, 100, 100, 50)
```

### canvas_save(canvas_id, filename)
Сохранить изображение
```khx
canvas_save(canvas, "output.png")
```

---

## 13. i18n

### create_i18n()
Создать систему локализации
```khx
let i18n = create_i18n()
```

### i18n_set_locale(i18n_id, locale)
Установить язык
```khx
i18n_set_locale(i18n, "ru")
```

---

## 14. Debugging

### debug_log(message)
Отладочный лог
```khx
debug_log("Debug info")
```

### debug_breakpoint()
Точка останова
```khx
debug_breakpoint()
```

### profile_start(name)
Начать профилирование
```khx
profile_start("calculation")
```

### profile_end(name)
Закончить профилирование
```khx
profile_end("calculation")
```

### profile_report()
Отчет профилирования
```khx
profile_report()
```

---

## 15. CLI Tools

### print_colored(text, color)
Цветной вывод
```khx
print_colored("Success!", "green")
```

### print_success(text)
Вывод успеха
```khx
print_success("Done!")
```

### print_error(text)
Вывод ошибки
```khx
print_error("Failed!")
```

### progress_bar(current, total)
Прогресс-бар
```khx
progress_bar(50, 100)
```

---

Полный список функций и примеры смотрите в папке `examples/`
