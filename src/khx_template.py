"""
KHX Template Engine Module
Шаблонизатор для генерации HTML и текста
"""

import re

# Storage
templates = {}
template_counter = 0


class Template:
    """Шаблон"""
    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.parent = None
        self.blocks = {}
        print(f"[Template] Создан: {name}")
    
    def render(self, context=None):
        """Рендерить шаблон"""
        context = context or {}
        result = self.content
        
        # 1. Обработка переменных {{ variable }}
        result = self._render_variables(result, context)
        
        # 2. Обработка циклов {% for item in items %}
        result = self._render_loops(result, context)
        
        # 3. Обработка условий {% if condition %}
        result = self._render_conditions(result, context)
        
        # 4. Обработка фильтров {{ variable|filter }}
        result = self._render_filters(result, context)
        
        return result
    
    def _render_variables(self, content, context):
        """Рендерить переменные"""
        # Находим все {{ variable }}
        pattern = r'\{\{\s*(\w+(?:\.\w+)*)\s*\}\}'
        
        def replace_var(match):
            var_path = match.group(1)
            value = self._get_nested_value(context, var_path)
            return str(value) if value is not None else ''
        
        return re.sub(pattern, replace_var, content)
    
    def _render_loops(self, content, context):
        """Рендерить циклы"""
        # {% for item in items %} ... {% endfor %}
        pattern = r'\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}'
        
        def replace_loop(match):
            item_name = match.group(1)
            list_name = match.group(2)
            loop_content = match.group(3)
            
            items = context.get(list_name, [])
            result = []
            
            for item in items:
                loop_context = context.copy()
                loop_context[item_name] = item
                rendered = self._render_variables(loop_content, loop_context)
                result.append(rendered)
            
            return ''.join(result)
        
        return re.sub(pattern, replace_loop, content, flags=re.DOTALL)
    
    def _render_conditions(self, content, context):
        """Рендерить условия"""
        # {% if condition %} ... {% endif %}
        pattern = r'\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}'
        
        def replace_condition(match):
            condition = match.group(1)
            if_content = match.group(2)
            
            value = context.get(condition, False)
            if value:
                return if_content
            return ''
        
        return re.sub(pattern, replace_condition, content, flags=re.DOTALL)
    
    def _render_filters(self, content, context):
        """Рендерить фильтры"""
        # {{ variable|filter }}
        pattern = r'\{\{\s*(\w+)\|(\w+)\s*\}\}'
        
        def replace_filter(match):
            var_name = match.group(1)
            filter_name = match.group(2)
            
            value = context.get(var_name, '')
            
            # Применяем фильтр
            if filter_name == 'upper':
                return str(value).upper()
            elif filter_name == 'lower':
                return str(value).lower()
            elif filter_name == 'capitalize':
                return str(value).capitalize()
            elif filter_name == 'length':
                return str(len(value)) if hasattr(value, '__len__') else '0'
            elif filter_name == 'reverse':
                return str(value)[::-1]
            
            return str(value)
        
        return re.sub(pattern, replace_filter, content)
    
    def _get_nested_value(self, context, path):
        """Получить вложенное значение (user.name)"""
        keys = path.split('.')
        value = context
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            elif hasattr(value, key):
                value = getattr(value, key)
            else:
                return None
        
        return value
    
    def extend(self, parent_template):
        """Наследование шаблона"""
        self.parent = parent_template
        print(f"[Template] {self.name} наследует {parent_template.name}")
    
    def block(self, block_name, content):
        """Определить блок"""
        self.blocks[block_name] = content


def load_template(filename):
    """Загрузить шаблон из файла"""
    global template_counter
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        template_id = f"template_{template_counter}"
        template_counter += 1
        
        templates[template_id] = Template(filename, content)
        print(f"[Template] Загружен из файла: {filename}")
        return template_id
        
    except FileNotFoundError:
        print(f"[Template] ✗ Файл не найден: {filename}")
        return None


def create_template(name, content):
    """Создать шаблон из строки"""
    global template_counter
    
    template_id = f"template_{template_counter}"
    template_counter += 1
    
    templates[template_id] = Template(name, content)
    return template_id


def get_template(template_id):
    """Получить шаблон"""
    return templates.get(template_id)


def render_string(template_string, context=None):
    """Быстрый рендеринг строки"""
    temp = Template("inline", template_string)
    return temp.render(context)


if __name__ == "__main__":
    print("=== KHX Template Engine Test ===\n")
    
    # Тест 1: Переменные
    print("Тест 1: Переменные")
    template1 = create_template("test1", "<h1>{{ title }}</h1><p>{{ content }}</p>")
    t1 = get_template(template1)
    result1 = t1.render({"title": "Привет", "content": "Это тест"})
    print(result1)
    
    # Тест 2: Циклы
    print("\nТест 2: Циклы")
    template2 = create_template("test2", 
        "<ul>{% for user in users %}<li>{{ user.name }}</li>{% endfor %}</ul>")
    t2 = get_template(template2)
    result2 = t2.render({
        "users": [
            {"name": "Иван"},
            {"name": "Мария"},
            {"name": "Петр"}
        ]
    })
    print(result2)
    
    # Тест 3: Условия
    print("\nТест 3: Условия")
    template3 = create_template("test3", 
        "{% if logged_in %}<p>Добро пожаловать!</p>{% endif %}")
    t3 = get_template(template3)
    result3 = t3.render({"logged_in": True})
    print(result3)
    
    # Тест 4: Фильтры
    print("\nТест 4: Фильтры")
    template4 = create_template("test4", 
        "<p>{{ name|upper }}</p><p>{{ text|capitalize }}</p>")
    t4 = get_template(template4)
    result4 = t4.render({"name": "john", "text": "hello world"})
    print(result4)
    
    # Тест 5: Комплексный
    print("\nТест 5: Комплексный шаблон")
    complex_template = """
<html>
<head><title>{{ page_title }}</title></head>
<body>
    <h1>{{ heading|upper }}</h1>
    {% if show_users %}
    <ul>
    {% for user in users %}
        <li>{{ user.name }} ({{ user.age }})</li>
    {% endfor %}
    </ul>
    {% endif %}
</body>
</html>
"""
    template5 = create_template("test5", complex_template)
    t5 = get_template(template5)
    result5 = t5.render({
        "page_title": "Пользователи",
        "heading": "список пользователей",
        "show_users": True,
        "users": [
            {"name": "Алексей", "age": 25},
            {"name": "Ольга", "age": 30}
        ]
    })
    print(result5)
