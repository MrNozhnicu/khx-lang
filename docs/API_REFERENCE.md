# KHX API Reference v5.1

Полный справочник по всем функциям KHX v5.1

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

## 3. Game Engine (25+ функций)

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

### 🆕 game_pause(game_id)
Поставить игру на паузу
```khx
game_pause(game)
```

### 🆕 game_resume(game_id)
Возобновить игру
```khx
game_resume(game)
```

### 🆕 game_add_score(game_id, points)
Добавить очки
```khx
game_add_score(game, 100)
```

### 🆕 game_next_level(game_id)
Перейти на следующий уровень
```khx
game_next_level(game)
```

### 🆕 game_reset(game_id)
Сбросить игру
```khx
game_reset(game)
```

### 🆕 game_spawn_enemy(game_id, x, y, type)
Создать врага
```khx
game_spawn_enemy(game, 400, 100, "boss")
```

### 🆕 game_spawn_powerup(game_id, x, y, type)
Создать бонус
```khx
game_spawn_powerup(game, 200, 300, "health")
```

### 🆕 game_set_gravity(game_id, gravity)
Установить гравитацию
```khx
game_set_gravity(game, 0.5)
```

### 🆕 sprite_rotate(sprite_id, angle)
Повернуть спрайт
```khx
sprite_rotate(sprite, 45)
```

### 🆕 sprite_scale(sprite_id, scale)
Масштабировать спрайт
```khx
sprite_scale(sprite, 1.5)
```

### 🆕 sprite_damage(sprite_id, damage)
Нанести урон спрайту
```khx
sprite_damage(sprite, 25)
```

### 🆕 sprite_heal(sprite_id, amount)
Вылечить спрайт
```khx
sprite_heal(sprite, 50)
```

---

## 4. Machine Learning (30+ функций)

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

### 🆕 nlp_extract_keywords(nlp_id, text, top_n)
Извлечь ключевые слова
```khx
let keywords = nlp_extract_keywords(nlp, text, 5)
```

### 🆕 nlp_text_similarity(nlp_id, text1, text2)
Схожесть текстов
```khx
let similarity = nlp_text_similarity(nlp, text1, text2)
```

### 🆕 nlp_find_entities(nlp_id, text)
Найти именованные сущности
```khx
let entities = nlp_find_entities(nlp, text)
```

### 🆕 nlp_remove_stopwords(nlp_id, text)
Удалить стоп-слова
```khx
let clean = nlp_remove_stopwords(nlp, text)
```

### 🆕 nlp_word_frequency(nlp_id, text)
Частота слов
```khx
let freq = nlp_word_frequency(nlp, text)
```

### 🆕 nlp_sentence_count(nlp_id, text)
Подсчет предложений
```khx
let count = nlp_sentence_count(nlp, text)
```

### 🆕 nlp_avg_word_length(nlp_id, text)
Средняя длина слова
```khx
let avg = nlp_avg_word_length(nlp, text)
```

### 🆕 nn_save_model(model_id, filename)
Сохранить модель
```khx
nn_save_model(model, "model.khx")
```

### 🆕 nn_load_model(model_id, filename)
Загрузить модель
```khx
nn_load_model(model, "model.khx")
```

### 🆕 nn_get_accuracy(model_id, test_data)
Получить точность модели
```khx
let accuracy = nn_get_accuracy(model, test_data)
```

---

## 5. Data Science (22+ функций)

### create_dataframe()
Создать DataFrame
```khx
let df = create_dataframe()
```

### 🆕 df_sort_by(df_id, column, ascending)
Сортировать по столбцу
```khx
df = df_sort_by(df, "age", true)
```

### 🆕 df_drop_column(df_id, column)
Удалить столбец
```khx
df = df_drop_column(df, "old_column")
```

### 🆕 df_rename_column(df_id, old_name, new_name)
Переименовать столбец
```khx
df = df_rename_column(df, "old", "new")
```

### 🆕 df_add_column(df_id, name, values)
Добавить столбец
```khx
df_add_column(df, "score", [10, 20, 30])
```

### 🆕 df_unique(df_id, column)
Уникальные значения
```khx
let unique = df_unique(df, "category")
```

### 🆕 df_value_counts(df_id, column)
Подсчет значений
```khx
let counts = df_value_counts(df, "status")
```

### 🆕 df_merge(df1_id, df2_id, on_column)
Объединить DataFrame
```khx
let merged = df_merge(df1, df2, "id")
```

### 🆕 df_fillna(df_id, value)
Заполнить пропуски
```khx
df = df_fillna(df, 0)
```

### 🆕 df_dropna(df_id)
Удалить строки с пропусками
```khx
df = df_dropna(df)
```

### 🆕 df_std(df_id, column)
Стандартное отклонение
```khx
let std = df_std(df, "values")
```

### 🆕 df_corr(df_id, col1, col2)
Корреляция между столбцами
```khx
let corr = df_corr(df, "height", "weight")
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

## 6. Audio/Video (20+ функций)

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

### 🆕 audio_pause(audio_id)
Пауза
```khx
audio_pause(audio)
```

### 🆕 audio_stop(audio_id)
Остановить
```khx
audio_stop(audio)
```

### 🆕 audio_seek(audio_id, position)
Перемотать на позицию (секунды)
```khx
audio_seek(audio, 30)
```

### 🆕 audio_set_loop(audio_id, loop)
Установить зацикливание
```khx
audio_set_loop(audio, true)
```

### 🆕 audio_fade_in(audio_id, duration)
Плавное появление
```khx
audio_fade_in(audio, 2.0)
```

### 🆕 audio_fade_out(audio_id, duration)
Плавное затухание
```khx
audio_fade_out(audio, 2.0)
```

### 🆕 audio_set_speed(audio_id, speed)
Установить скорость
```khx
audio_set_speed(audio, 1.5)
```

### 🆕 audio_normalize(audio_id)
Нормализовать громкость
```khx
audio_normalize(audio)
```

### 🆕 audio_trim(audio_id, start, end)
Обрезать аудио
```khx
audio_trim(audio, 10, 60)
```

### 🆕 audio_export(audio_id, filename, format)
Экспортировать аудио
```khx
audio_export(audio, "output", "wav")
```

### audio_effect(audio_id, effect, intensity)
Применить эффект
```khx
audio_effect(audio, "reverb", 0.7)
```

### 🆕 create_mixer()
Создать аудио микшер
```khx
let mixer = create_mixer()
```

### 🆕 mixer_add_track(mixer_id, audio_id)
Добавить трек в микшер
```khx
mixer_add_track(mixer, audio)
```

### 🆕 mixer_set_volume(mixer_id, volume)
Установить общую громкость
```khx
mixer_set_volume(mixer, 0.8)
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

## 8. Mobile Development (25+ функций)

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

### 🆕 app_save_data(app_id, key, value)
Сохранить данные локально
```khx
app_save_data(app, "user_id", "12345")
```

### 🆕 app_load_data(app_id, key)
Загрузить данные
```khx
let data = app_load_data(app, "user_id")
```

### 🆕 app_clear_storage(app_id)
Очистить хранилище
```khx
app_clear_storage(app)
```

### 🆕 app_request_permission(app_id, permission)
Запросить разрешение
```khx
app_request_permission(app, "CAMERA")
```

### 🆕 app_vibrate(app_id, duration)
Вибрация устройства
```khx
app_vibrate(app, 200)
```

### 🆕 app_share_content(app_id, content, platform)
Поделиться контентом
```khx
app_share_content(app, "Check this out!", "twitter")
```

### 🆕 app_open_url(app_id, url)
Открыть URL в браузере
```khx
app_open_url(app, "https://example.com")
```

### 🆕 app_get_device_info(app_id)
Получить информацию об устройстве
```khx
let info = app_get_device_info(app)
```

### 🆕 app_set_orientation(app_id, orientation)
Установить ориентацию экрана
```khx
app_set_orientation(app, "landscape")
```

### 🆕 camera_set_resolution(camera_id, width, height)
Установить разрешение камеры
```khx
camera_set_resolution(camera, 1920, 1080)
```

### 🆕 camera_toggle_flash(camera_id)
Переключить вспышку
```khx
camera_toggle_flash(camera)
```

### 🆕 camera_switch(camera_id)
Переключить камеру (фронтальная/основная)
```khx
camera_switch(camera)
```

### 🆕 camera_apply_filter(camera_id, filter_name)
Применить фильтр к фото
```khx
camera_apply_filter(camera, "sepia")
```

### 🆕 gps_stop_tracking(gps_id)
Остановить отслеживание GPS
```khx
gps_stop_tracking(gps)
```

### 🆕 gps_get_distance(gps_id, lat1, lon1, lat2, lon2)
Вычислить расстояние между точками
```khx
let distance = gps_get_distance(gps, 55.75, 37.61, 59.93, 30.31)
```

### 🆕 gps_set_accuracy(gps_id, mode)
Установить точность GPS
```khx
gps_set_accuracy(gps, "high")
```

### 🆕 gps_get_address(gps_id, lat, lon)
Получить адрес по координатам
```khx
let address = gps_get_address(gps, 55.7558, 37.6173)
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


---

## 🆕 Новое в v5.1

### Добавлено 100+ новых функций:

- **Data Science**: +12 функций (sort_by, merge, corr, fillna, dropna и др.)
- **Mobile**: +15 функций (storage, permissions, vibrate, share и др.)
- **Game Engine**: +13 функций (pause, score, spawn_enemy, gravity и др.)
- **Machine Learning**: +18 функций (NLP keywords, similarity, entities и др.)
- **Audio**: +16 функций (mixer, fade, export, normalize и др.)

### Полный список изменений:
См. [CHANGELOG_v5.1.md](../CHANGELOG_v5.1.md)

---

**Версия**: 5.1.0  
**Функций**: 300+  
**Модулей**: 22

Полный список функций и примеры смотрите в папке `examples/`
