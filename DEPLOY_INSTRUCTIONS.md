# 🚀 Инструкция по публикации .exe файла

## ❌ Проблема: GitHub лимит 25 MB

GitHub Releases не принимает файлы больше 25 MB.
Наш файл: `KHX-Editor-v5.0.0-Windows.zip` (49 MB)

## ✅ Решения

### Вариант 1: Облачное хранилище (Самый простой)

#### Google Drive
1. Загрузите `dist/KHX-Editor-v5.0.0-Windows.zip` на Google Drive
2. Правый клик → "Получить ссылку" → "Доступ для всех, у кого есть ссылка"
3. Скопируйте ссылку
4. Добавьте в Release description:
   ```markdown
   ### Windows Download
   📥 [Download KHX-Editor-v5.0.0-Windows.zip (49 MB)](ВАША_ССЫЛКА)
   ```

#### Яндекс.Диск
1. Загрузите файл на Яндекс.Диск
2. Нажмите "Поделиться" → "Скопировать публичную ссылку"
3. Добавьте ссылку в Release

#### Dropbox
1. Загрузите файл
2. "Share" → "Create link"
3. Добавьте ссылку в Release

---

### Вариант 2: Git LFS (Large File Storage)

```bash
# Установить Git LFS
git lfs install

# Отслеживать большие файлы
git lfs track "*.zip"
git lfs track "*.exe"

# Добавить .gitattributes
git add .gitattributes

# Добавить файлы
git add dist/KHX-Editor-v5.0.0-Windows.zip
git commit -m "Add Windows build with Git LFS"
git push
```

**Лимиты Git LFS:**
- Бесплатно: 1 GB хранилище, 1 GB bandwidth/месяц
- Платно: $5/месяц за 50 GB

---

### Вариант 3: Разделить на части (Split)

```bash
# Разделить на части по 20 MB
cd dist
split -b 20M KHX-Editor-v5.0.0-Windows.zip KHX-Editor-part-

# Получится:
# KHX-Editor-part-aa (20 MB)
# KHX-Editor-part-ab (20 MB)
# KHX-Editor-part-ac (9 MB)
```

Загрузить все части в Release, пользователи объединят:
```bash
cat KHX-Editor-part-* > KHX-Editor-v5.0.0-Windows.zip
```

---

### Вариант 4: Уменьшить размер .exe

Оптимизировать сборку PyInstaller:

```python
# В build_exe.py добавить:
excludes = [
    'matplotlib',  # Если не используется
    'scipy',       # Если не используется
    'pandas',      # Если не используется
]

a = Analysis(
    # ...
    excludes=excludes,
)
```

Или использовать UPX компрессию:
```bash
pip install pyinstaller[encryption]
pyinstaller --upx-dir=/path/to/upx build_exe.py
```

---

### Вариант 5: Только исходники (Рекомендуется для Open Source)

Не загружать .exe вообще, только инструкция по сборке:

```markdown
## 📦 Installation

### Build from Source
```bash
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang
pip install -r requirements.txt
pip install pyinstaller
python build_exe.py
```

Result: `dist/KHX-Editor.exe`
```

---

## 🎯 Рекомендация

**Для Open Source проекта лучше всего:**

1. **Не загружать .exe в Release** - пользователи соберут сами
2. **Добавить подробную инструкцию** по сборке в README
3. **Опционально**: Разместить .exe на Google Drive/Яндекс.Диск для тех, кто не хочет собирать

**Преимущества:**
- ✅ Нет проблем с лимитами GitHub
- ✅ Пользователи видят, что внутри (безопасность)
- ✅ Работает на любой платформе (не только Windows)
- ✅ Всегда актуальная версия

---

## 📝 Обновленный Release Description

```markdown
# KHX v5.0 - Complete Release 🎉

First stable release of KHX Programming Language!

## 📦 Installation

### Windows (Build from Source)
```bash
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang
pip install -r requirements.txt
pip install pyinstaller
python build_exe.py
```
Result: `dist/KHX-Editor.exe` (49 MB) - Standalone editor with all features!

### Linux / macOS
```bash
git clone https://github.com/MrNozhnicu/khx-lang.git
cd khx-lang
pip install -r requirements.txt
python editor.py
```

### Quick Test (No build needed)
```bash
python src/khx_v5.py examples/hello.khx
```

## ✨ Features
[... остальное без изменений ...]
```

---

## ✅ Что делать сейчас

1. **Создайте Release БЕЗ .exe файла**
2. **Добавьте инструкцию по сборке** (см. выше)
3. **Опционально**: Загрузите .exe на облако и добавьте ссылку

Это стандартная практика для Open Source проектов!
