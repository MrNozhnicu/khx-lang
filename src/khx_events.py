"""
KHX Event System Module
Продвинутая система событий
"""

import time
from collections import defaultdict

# Storage
event_emitters = {}
emitter_counter = 0


class EventEmitter:
    """Эмиттер событий"""
    def __init__(self):
        self.listeners = defaultdict(list)
        self.once_listeners = defaultdict(list)
        print(f"[Events] Создан эмиттер")
    
    def on(self, event, callback, priority=0):
        """Подписаться на событие"""
        self.listeners[event].append({
            'callback': callback,
            'priority': priority
        })
        # Сортируем по приоритету (больше = выше)
        self.listeners[event].sort(key=lambda x: x['priority'], reverse=True)
        print(f"[Events] Подписка на '{event}' (приоритет: {priority})")
        return True
    
    def once(self, event, callback):
        """Подписаться на событие (один раз)"""
        self.once_listeners[event].append(callback)
        print(f"[Events] Подписка на '{event}' (один раз)")
        return True
    
    def off(self, event, callback=None):
        """Отписаться от события"""
        if callback is None:
            # Удалить все обработчики
            if event in self.listeners:
                del self.listeners[event]
            if event in self.once_listeners:
                del self.once_listeners[event]
            print(f"[Events] Удалены все обработчики '{event}'")
        else:
            # Удалить конкретный обработчик
            self.listeners[event] = [
                l for l in self.listeners[event] 
                if l['callback'] != callback
            ]
            self.once_listeners[event] = [
                l for l in self.once_listeners[event] 
                if l != callback
            ]
            print(f"[Events] Удален обработчик '{event}'")
        return True
    
    def emit(self, event, *args, **kwargs):
        """Вызвать событие"""
        print(f"[Events] Событие: {event}")
        
        # Обычные обработчики
        for listener in self.listeners.get(event, []):
            try:
                listener['callback'](*args, **kwargs)
            except Exception as e:
                print(f"[Events] ✗ Ошибка в обработчике: {e}")
        
        # Одноразовые обработчики
        for callback in self.once_listeners.get(event, []):
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"[Events] ✗ Ошибка в обработчике: {e}")
        
        # Очищаем одноразовые
        if event in self.once_listeners:
            self.once_listeners[event] = []
        
        return True
    
    def emit_async(self, event, *args, **kwargs):
        """Асинхронное событие"""
        print(f"[Events] Async событие: {event}")
        # Симуляция асинхронности
        return self.emit(event, *args, **kwargs)
    
    def list_events(self):
        """Список всех событий"""
        events = set(list(self.listeners.keys()) + list(self.once_listeners.keys()))
        print(f"\n[Events] Зарегистрированные события ({len(events)}):")
        for event in events:
            count = len(self.listeners.get(event, [])) + len(self.once_listeners.get(event, []))
            print(f"  • {event} ({count} обработчиков)")
        return list(events)


def create_event_emitter():
    """Создать эмиттер событий"""
    global emitter_counter
    emitter_id = f"emitter_{emitter_counter}"
    emitter_counter += 1
    event_emitters[emitter_id] = EventEmitter()
    return emitter_id


def get_event_emitter(emitter_id):
    """Получить эмиттер"""
    return event_emitters.get(emitter_id)


# Глобальный эмиттер
global_emitter = EventEmitter()


def on(event, callback, priority=0):
    """Глобальная подписка"""
    return global_emitter.on(event, callback, priority)


def emit(event, *args, **kwargs):
    """Глобальное событие"""
    return global_emitter.emit(event, *args, **kwargs)


if __name__ == "__main__":
    print("=== KHX Event System Test ===\n")
    
    # Создаем эмиттер
    emitter_id = create_event_emitter()
    emitter = get_event_emitter(emitter_id)
    
    # Регистрируем обработчики
    def on_user_login(user):
        print(f"[Handler] Пользователь вошел: {user['name']}")
    
    def on_user_logout(user):
        print(f"[Handler] Пользователь вышел: {user['name']}")
    
    def validate_data():
        print(f"[Handler] Валидация данных (приоритет 10)")
    
    def save_to_db():
        print(f"[Handler] Сохранение в БД (приоритет 5)")
    
    emitter.on("user:login", on_user_login)
    emitter.on("user:logout", on_user_logout)
    
    # С приоритетом
    emitter.on("save", validate_data, priority=10)
    emitter.on("save", save_to_db, priority=5)
    
    # Одноразовый
    emitter.once("init", lambda: print("[Handler] Инициализация (один раз)"))
    
    # Вызываем события
    print("\nВызов событий:")
    emitter.emit("user:login", {"name": "Иван", "id": 1})
    emitter.emit("save")
    emitter.emit("init")
    emitter.emit("init")  # Не сработает второй раз
    
    # Список событий
    emitter.list_events()
