# 🚀 Гайд по выпуску KHX v5.1

## ✅ Что уже готово

- ✅ Код обновлен (100+ новых функций)
- ✅ Все изменения закоммичены
- ✅ Код отправлен на GitHub
- ✅ Документация обновлена:
  - `CHANGELOG_v5.1.md` - полный список изменений
  - `API_REFERENCE.md` - обновлен с новыми функциями
  - `README.md` - обновлена версия
  - `UPDATE_SUMMARY.md` - сводка обновления

---

## 📝 Шаг 1: Создать Release на GitHub

### 1.1 Откройте страницу создания Release

Перейдите по ссылке:
```
https://github.com/MrNozhnicu/khx-lang/releases/new
```

### 1.2 Заполните форму

#### Tag version
В поле "Choose a tag" введите:
```
v5.1.0
```

#### Release title
```
KHX v5.1 - Extended Modules (300+ Functions) 🎉
```

#### Description
Скопируйте и вставьте текст ниже:

```markdown
# KHX v5.1 - Extended Modules 🎉

Major update with 100+ new functions across all modules!

## ✨ What's New

### 📊 Data Science Module (+12 functions)
- `sort_by()` - Sort DataFrame by column
- `merge()` - Merge DataFrames
- `corr()` - Calculate correlation
- `fillna()` / `dropna()` - Handle missing values
- `unique()`, `value_counts()` - Data analysis
- And more!

### 📱 Mobile Development (+15 functions)
- `save_data()` / `load_data()` - Local storage
- `request_permission()` - Permission management
- `vibrate()` - Device vibration
- `share_content()` - Share functionality
- `get_device_info()` - Device information
- GPS: `get_distance()`, `get_address()` - Geolocation
- Camera: `toggle_flash()`, `apply_filter()` - Camera controls

### 🎮 Game Engine (+13 functions)
- `pause()` / `resume()` - Game state control
- `add_score()`, `next_level()` - Scoring system
- `spawn_enemy()`, `spawn_powerup()` - Entity spawning
- `set_gravity()` - Physics
- Sprite: `rotate()`, `take_damage()`, `heal()` - Sprite controls

### 🤖 Machine Learning (+18 functions)
- NLP: `extract_keywords()` - Keyword extraction
- `text_similarity()` - Text comparison
- `find_entities()` - Named entity recognition
- `remove_stopwords()` - Text preprocessing
- Neural Network: `relu()`, `tanh()` - Activation functions
- `save_model()` / `load_model()` - Model persistence

### 🎵 Audio Module (+16 functions)
- `pause()`, `stop()`, `seek()` - Playback control
- `fade_in()`, `fade_out()` - Fade effects
- `set_loop()` - Loop control
- `normalize()`, `trim()` - Audio editing
- `export()` - Export to MP3/WAV/OGG
- AudioMixer class - Multi-track mixing

## 📦 Installation

### From Source
```bash
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang
pip install -r requirements.txt
python editor.py
```

### Build Executable (Windows)
```bash
pip install pyinstaller
python build_exe.py
```
Result: `dist/KHX-Editor.exe`

## 📈 Statistics

- **Modules**: 22 (21 working)
- **Functions**: 300+ (was 200+)
- **Lines of code**: 12,000+ (was 9,226)
- **Examples**: 17 programs
- **Documentation**: 14 files

## 🎯 Example Code

```khx
// Data Science
let df = create_dataframe(data)
df = df.sort_by("age", true).fillna(0)
let corr = df.corr("height", "weight")

// Mobile App
let app = create_mobile_app("MyApp")
app.save_data("score", "1000")
app.vibrate(200)

// Game
let game = create_game(800, 600, "Space")
game.spawn_enemy(400, 100, "boss")
game.add_score(100)

// Machine Learning
let nlp = create_nlp()
let keywords = nlp.extract_keywords(text, 5)

// Audio
let audio = load_audio("music.mp3")
audio.fade_in(2.0)
audio.export("output", "wav")
```

## 📚 Documentation

- [README](https://github.com/MrNozhnicu/khx-lang#readme)
- [CHANGELOG v5.1](https://github.com/MrNozhnicu/khx-lang/blob/main/CHANGELOG_v5.1.md)
- [API Reference](https://github.com/MrNozhnicu/khx-lang/blob/main/docs/API_REFERENCE.md)
- [Examples](https://github.com/MrNozhnicu/khx-lang/tree/main/examples)

## 🐛 Known Issues

- Network module requires `requests` library: `pip install requests`

## 🤝 Contributing

See [CONTRIBUTING.md](https://github.com/MrNozhnicu/khx-lang/blob/main/CONTRIBUTING.md)

## 📝 License

MIT License - see [LICENSE](https://github.com/MrNozhnicu/khx-lang/blob/main/LICENSE)

---

**Full Changelog**: https://github.com/MrNozhnicu/khx-lang/compare/v5.0.0...v5.1.0

**Star ⭐ this repo if you like it!**
```

### 1.3 НЕ прикрепляйте файлы

GitHub имеет лимит 25 MB для файлов в Release. Наш .exe файл 49 MB, поэтому:
- ❌ НЕ прикрепляйте `KHX-Editor.exe` или ZIP
- ✅ Пользователи соберут .exe сами из исходников

### 1.4 Нажмите "Publish release"

Зеленая кнопка внизу страницы.

---

## 🎉 Шаг 2: Проверить Release

После публикации:

1. Release появится на: https://github.com/MrNozhnicu/khx-lang/releases
2. Будет создан тег `v5.1.0`
3. Пользователи смогут:
   - Скачать исходный код (Source code.zip / Source code.tar.gz)
   - Собрать .exe командой `python build_exe.py`

---

## 📢 Шаг 3 (Опционально): Добавить Topics

Это поможет людям найти ваш проект на GitHub.

1. Перейдите на главную страницу репозитория
2. Нажмите на шестеренку рядом с "About"
3. Добавьте topics:
   - `programming-language`
   - `interpreter`
   - `python`
   - `gui`
   - `machine-learning`
   - `game-engine`
   - `mobile-development`
   - `data-science`
   - `audio-processing`
   - `cryptography`

4. Нажмите "Save changes"

---

## 📊 Шаг 4 (Опционально): Обновить описание репозитория

В разделе "About":
- **Description**: `Modern programming language with 22 modules and 300+ functions for rapid development`
- **Website**: (если есть)
- **Topics**: (добавлены в Шаге 3)

---

## ✅ Готово!

После выполнения всех шагов:

- ✅ Release v5.1.0 опубликован
- ✅ Пользователи могут скачать код
- ✅ Проект легко найти через поиск GitHub
- ✅ Все изменения задокументированы

---

## 🚀 Что дальше?

### Для пользователей:

Обновить локальную копию:
```bash
git pull origin main
```

Пересобрать .exe:
```bash
python build_exe.py
```

### Для разработки:

- ✅ v5.1 - Расширены основные модули (ГОТОВО)
- 🔄 v5.2 - Расширить остальные модули (Canvas, CLI, Events и др.)
- 🔄 v5.3 - Оптимизация производительности
- 🔄 v6.0 - Компилятор в нативный код

---

**Проект готов к использованию! 🎉**

**Ссылка на Release**: https://github.com/MrNozhnicu/khx-lang/releases/tag/v5.1.0
