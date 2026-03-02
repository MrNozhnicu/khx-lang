# 💻 KHX CLI Guide

Полное руководство по командной строке KHX

## Установка

### Автоматическая установка

```bash
python khx_cli_installer.py
```

Это установит команду `khx` в вашу систему.

### Проверка установки

```bash
khx --version
```

Вывод:
```
KHX Programming Language v5.2
Copyright (c) 2026 KHX Developer
MIT License
```

---

## Основные команды

### Запуск программы

```bash
khx script.khx
```

Или:

```bash
khx --run script.khx
```

### Показать версию

```bash
khx --version
khx -v
```

### Показать справку

```bash
khx --help
khx -h
```

---

## Интерактивный режим (REPL)

### Запуск REPL

```bash
khx --repl
khx -r
```

### Использование REPL

```
KHX REPL v5.2
Введите 'exit' для выхода
----------------------------------------
khx> print("Hello!")
Hello!

khx> let x = 10
khx> print(x * 2)
20

khx> let name = "Alice"
khx> print("Hello,", name)
Hello, Alice

khx> exit
До свидания!
```

### Команды REPL

- `exit` или `quit` - Выход
- `Ctrl+C` - Прервать текущую команду
- `Ctrl+D` - Выход (Unix)

---

## Управление проектами

### Создать новый проект

```bash
khx --new my_project
```

Создаст структуру:
```
my_project/
├── src/
│   └── main.khx
├── examples/
└── README.md
```

### Запустить проект

```bash
cd my_project
khx src/main.khx
```

---

## Проверка и форматирование

### Проверить синтаксис

```bash
khx --check script.khx
```

Вывод:
```
Проверка синтаксиса: script.khx
✅ Синтаксис корректен
```

### Форматировать код

```bash
khx --format script.khx
```

---

## Примеры

### Показать список примеров

```bash
khx --examples
```

Вывод:
```
KHX Examples

1. Hello World:
   khx examples/hello.khx

2. Calculator:
   khx examples/calculator.khx

3. Database:
   khx examples/database.khx

...
```

### Запустить пример

```bash
khx examples/hello.khx
khx examples/calculator.khx
khx examples/game.khx
```

---

## Документация

### Открыть документацию

```bash
khx --docs
```

Откроет документацию в браузере.

---

## Расширенные возможности

### Передача аргументов

```bash
khx script.khx arg1 arg2 arg3
```

В скрипте:
```khx
// Доступ к аргументам
let args = get_args()
print("Аргументы:", args)
```

### Переменные окружения

```bash
# Windows
set KHX_DEBUG=1
khx script.khx

# Linux/macOS
KHX_DEBUG=1 khx script.khx
```

### Перенаправление вывода

```bash
# Сохранить вывод в файл
khx script.khx > output.txt

# Добавить к файлу
khx script.khx >> output.txt

# Перенаправить ошибки
khx script.khx 2> errors.txt
```

---

## Конфигурация

### Файл конфигурации

Создайте `.khxrc` в домашней директории:

```ini
[khx]
version = 5.2
debug = false
color = true

[paths]
modules = ~/.khx/modules
plugins = ~/.khx/plugins
```

### Переменные окружения

- `KHX_HOME` - Домашняя директория KHX
- `KHX_DEBUG` - Режим отладки (0/1)
- `KHX_COLOR` - Цветной вывод (0/1)
- `KHX_PATH` - Дополнительные пути для модулей

---

## Советы и трюки

### Алиасы (Linux/macOS)

Добавьте в `~/.bashrc` или `~/.zshrc`:

```bash
alias khxr='khx --repl'
alias khxn='khx --new'
alias khxe='khx --examples'
```

### Автодополнение (Bash)

Создайте `~/.khx_completion.bash`:

```bash
_khx_completion() {
    local cur prev opts
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--version --help --repl --new --run --check --format --docs --examples"
    
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
}

complete -F _khx_completion khx
```

Добавьте в `~/.bashrc`:
```bash
source ~/.khx_completion.bash
```

### Быстрый запуск (Windows)

Создайте `run.bat`:

```batch
@echo off
khx %1
pause
```

Теперь можно перетаскивать `.khx` файлы на `run.bat`.

---

## Примеры использования

### Разработка

```bash
# Создать проект
khx --new todo_app
cd todo_app

# Редактировать
nano src/main.khx

# Проверить
khx --check src/main.khx

# Запустить
khx src/main.khx

# Отладка
KHX_DEBUG=1 khx src/main.khx
```

### Быстрое тестирование

```bash
# REPL для экспериментов
khx --repl

# Или создать временный файл
echo 'print("Test")' > test.khx
khx test.khx
rm test.khx
```

### Автоматизация

```bash
# Скрипт для обработки файлов
for file in *.txt; do
    khx process.khx "$file"
done
```

---

## Устранение проблем

### Команда khx не найдена

**Проблема**: `command not found: khx`

**Решение**:
1. Проверьте установку: `python khx_cli_installer.py`
2. Добавьте в PATH (см. вывод установщика)
3. Перезапустите терминал

### Ошибка импорта модулей

**Проблема**: `ModuleNotFoundError`

**Решение**:
```bash
pip install -r requirements.txt
```

### Проблемы с правами (Linux/macOS)

**Проблема**: `Permission denied`

**Решение**:
```bash
chmod +x ~/.local/bin/khx
```

---

## Удаление

### Удалить KHX CLI

```bash
python khx_cli_installer.py uninstall
```

### Полное удаление

```bash
# Удалить CLI
python khx_cli_installer.py uninstall

# Удалить конфигурацию
rm -rf ~/.khx
rm ~/.khxrc

# Удалить проект
cd ..
rm -rf khx-lang
```

---

## Дополнительные ресурсы

- [Getting Started](GETTING_STARTED.md) - Начало работы
- [Tutorials](TUTORIALS.md) - Подробные туториалы
- [API Reference](API_REFERENCE.md) - Справочник функций
- [FAQ](FAQ.md) - Частые вопросы

---

**Готовы начать? Попробуйте: `khx --repl`**
