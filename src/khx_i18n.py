"""
KHX Internationalization (i18n) Module
Мультиязычность и локализация
"""

import re
from datetime import datetime

# Storage
i18n_instances = {}
i18n_counter = 0


class I18n:
    """Система интернационализации"""
    def __init__(self):
        self.translations = {}
        self.current_locale = "en"
        self.fallback_locale = "en"
        print(f"[i18n] Инициализирована (локаль: {self.current_locale})")
    
    def load(self, locale, translations):
        """Загрузить переводы"""
        if locale not in self.translations:
            self.translations[locale] = {}
        
        self.translations[locale].update(translations)
        count = len(translations)
        print(f"[i18n] Загружено {count} переводов для '{locale}'")
        return True
    
    def set_locale(self, locale):
        """Установить текущую локаль"""
        if locale in self.translations:
            self.current_locale = locale
            print(f"[i18n] Локаль изменена: {locale}")
            return True
        else:
            print(f"[i18n] ✗ Локаль '{locale}' не найдена")
            return False
    
    def get_locale(self):
        """Получить текущую локаль"""
        return self.current_locale
    
    def t(self, key, params=None):
        """Перевести ключ (translate)"""
        # Пробуем текущую локаль
        if self.current_locale in self.translations:
            if key in self.translations[self.current_locale]:
                text = self.translations[self.current_locale][key]
                return self._interpolate(text, params)
        
        # Fallback
        if self.fallback_locale in self.translations:
            if key in self.translations[self.fallback_locale]:
                text = self.translations[self.fallback_locale][key]
                return self._interpolate(text, params)
        
        # Ключ не найден
        return f"[{key}]"
    
    def _interpolate(self, text, params):
        """Подставить параметры в текст"""
        if not params:
            return text
        
        # Замена {{param}}
        for key, value in params.items():
            text = text.replace(f"{{{{{key}}}}}", str(value))
        
        return text
    
    def plural(self, key, count, params=None):
        """Множественные формы"""
        params = params or {}
        params['count'] = count
        
        # Правила для русского языка
        if self.current_locale == "ru":
            if count % 10 == 1 and count % 100 != 11:
                plural_key = f"{key}.one"
            elif count % 10 in [2, 3, 4] and count % 100 not in [12, 13, 14]:
                plural_key = f"{key}.few"
            else:
                plural_key = f"{key}.many"
        else:
            # Английский
            plural_key = f"{key}.one" if count == 1 else f"{key}.other"
        
        return self.t(plural_key, params)
    
    def format_date(self, date, format_type="short"):
        """Форматировать дату"""
        if self.current_locale == "ru":
            if format_type == "short":
                return date.strftime("%d.%m.%Y")
            elif format_type == "long":
                months = ["января", "февраля", "марта", "апреля", "мая", "июня",
                         "июля", "августа", "сентября", "октября", "ноября", "декабря"]
                return f"{date.day} {months[date.month-1]} {date.year}"
        else:
            if format_type == "short":
                return date.strftime("%m/%d/%Y")
            elif format_type == "long":
                return date.strftime("%B %d, %Y")
        
        return str(date)
    
    def format_number(self, number, decimals=2):
        """Форматировать число"""
        if self.current_locale == "ru":
            # Русский формат: 1 234,56
            formatted = f"{number:,.{decimals}f}"
            formatted = formatted.replace(",", " ").replace(".", ",")
            return formatted
        else:
            # Английский формат: 1,234.56
            return f"{number:,.{decimals}f}"
    
    def format_currency(self, amount, currency="USD"):
        """Форматировать валюту"""
        formatted = self.format_number(amount, 2)
        
        if self.current_locale == "ru":
            if currency == "RUB":
                return f"{formatted} ₽"
            elif currency == "USD":
                return f"${formatted}"
            elif currency == "EUR":
                return f"€{formatted}"
        else:
            if currency == "USD":
                return f"${formatted}"
            elif currency == "EUR":
                return f"€{formatted}"
            elif currency == "RUB":
                return f"{formatted} RUB"
        
        return f"{formatted} {currency}"


def create_i18n():
    """Создать экземпляр i18n"""
    global i18n_counter
    i18n_id = f"i18n_{i18n_counter}"
    i18n_counter += 1
    i18n_instances[i18n_id] = I18n()
    return i18n_id


def get_i18n(i18n_id):
    """Получить экземпляр i18n"""
    return i18n_instances.get(i18n_id)


def detect_locale():
    """Автоопределение локали"""
    import locale
    try:
        system_locale = locale.getdefaultlocale()[0]
        if system_locale:
            lang = system_locale.split('_')[0]
            print(f"[i18n] Определена системная локаль: {lang}")
            return lang
    except:
        pass
    
    return "en"


if __name__ == "__main__":
    print("=== KHX i18n Module Test ===\n")
    
    # Создаем i18n
    i18n_id = create_i18n()
    i18n = get_i18n(i18n_id)
    
    # Загружаем переводы
    i18n.load("en", {
        "greeting": "Hello, {{name}}!",
        "items.one": "{{count}} item",
        "items.other": "{{count}} items"
    })
    
    i18n.load("ru", {
        "greeting": "Привет, {{name}}!",
        "items.one": "{{count}} элемент",
        "items.few": "{{count}} элемента",
        "items.many": "{{count}} элементов"
    })
    
    # Тест переводов
    print("Английский:")
    i18n.set_locale("en")
    print(f"  {i18n.t('greeting', {'name': 'John'})}")
    print(f"  {i18n.plural('items', 1)}")
    print(f"  {i18n.plural('items', 5)}")
    
    print("\nРусский:")
    i18n.set_locale("ru")
    print(f"  {i18n.t('greeting', {'name': 'Иван'})}")
    print(f"  {i18n.plural('items', 1)}")
    print(f"  {i18n.plural('items', 2)}")
    print(f"  {i18n.plural('items', 5)}")
    
    # Форматирование
    print("\nФорматирование:")
    date = datetime(2024, 3, 15)
    print(f"  Дата (короткая): {i18n.format_date(date, 'short')}")
    print(f"  Дата (длинная): {i18n.format_date(date, 'long')}")
    print(f"  Число: {i18n.format_number(1234567.89)}")
    print(f"  Валюта: {i18n.format_currency(1234.56, 'RUB')}")
