# Быстрый старт KHX

## За 5 минут до первой программы!

### Шаг 1: Установка (1 минута)

```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/khx-lang.git
cd khx-lang

# Установить зависимости
pip install -r requirements.txt
```

### Шаг 2: Hello World (1 минута)

Создайте файл `my_first.khx`:

```khx
print("Hello, KHX!")
print("Мой первый код на KHX!")
```

Запустите:

```bash
python src/khx_v5.py my_first.khx
```

### Шаг 3: Калькулятор (2 минуты)

```khx
func add(a: int, b: int) -> int {
    return a + b
}

let x = 10
let y = 5

print("Результат:")
print(add(x, y))
```

### Шаг 4: GUI приложение (1 минута)

```khx
let win = create_window("Мое приложение", 800, 600)
add_label(win, "Привет из KHX!")
add_button(win, "Нажми меня")
show_window(win)
```

## Готово! 🎉

Теперь вы можете:

1. **Открыть редактор**
   ```bash
   python editor.py
   ```

2. **Изучить примеры**
   ```bash
   cd examples
   python ../src/khx_v5.py calculator.khx
   ```

3. **Читать документацию**
   - [README.md](README.md) - Полное руководство
   - [docs/API_REFERENCE.md](docs/API_REFERENCE.md) - Справочник API

## Что дальше?

- Попробуйте все примеры из `examples/`
- Изучите 20 модулей в документации
- Создайте свой проект
- Поделитесь с друзьями!

**Удачи в программировании на KHX! 🚀**
