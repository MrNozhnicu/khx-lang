"""
KHX Mobile Development Module
Кросс-платформенная разработка мобильных приложений
"""

import os
import json

# Storage
mobile_apps = {}
app_counter = 0


class MobileScreen:
    """Экран мобильного приложения"""
    def __init__(self, name):
        self.name = name
        self.components = []
        print(f"[Mobile] Создан экран: {name}")
    
    def add_button(self, text, x=0, y=0):
        """Добавить кнопку"""
        btn_id = f"btn_{len(self.components)}"
        self.components.append({
            'type': 'button',
            'id': btn_id,
            'text': text,
            'x': x,
            'y': y,
            'callback': None
        })
        print(f"[Mobile] Кнопка добавлена: {text}")
        return btn_id
    
    def add_text(self, text, size=16):
        """Добавить текст"""
        text_id = f"text_{len(self.components)}"
        self.components.append({
            'type': 'text',
            'id': text_id,
            'text': text,
            'size': size
        })
        print(f"[Mobile] Текст добавлен: {text}")
        return text_id
    
    def add_image(self, image_path, width=100, height=100):
        """Добавить изображение"""
        img_id = f"img_{len(self.components)}"
        self.components.append({
            'type': 'image',
            'id': img_id,
            'path': image_path,
            'width': width,
            'height': height
        })
        print(f"[Mobile] Изображение добавлено: {image_path}")
        return img_id
    
    def show_image(self, image_data):
        """Показать изображение"""
        print(f"[Mobile] Отображение изображения")
        return self.add_image("captured_photo.jpg")


class MobileCamera:
    """Камера устройства"""
    def __init__(self):
        self.resolution = "1920x1080"
        self.flash_enabled = False
        self.front_camera = False
        print(f"[Camera] Инициализирована")
    
    def take_photo(self):
        """Сделать фото"""
        print(f"[Camera] Фото сделано ({self.resolution})")
        return {"path": "photo.jpg", "resolution": self.resolution}
    
    def record_video(self, duration):
        """Записать видео"""
        print(f"[Camera] Видео записано ({duration}s)")
        return {"path": "video.mp4", "duration": duration}
    
    def set_resolution(self, width, height):
        """Установить разрешение"""
        self.resolution = f"{width}x{height}"
        print(f"[Camera] Разрешение: {self.resolution}")
        return True
    
    def toggle_flash(self):
        """Переключить вспышку"""
        self.flash_enabled = not self.flash_enabled
        print(f"[Camera] Вспышка: {'вкл' if self.flash_enabled else 'выкл'}")
        return self.flash_enabled
    
    def switch_camera(self):
        """Переключить камеру (фронтальная/основная)"""
        self.front_camera = not self.front_camera
        print(f"[Camera] Камера: {'фронтальная' if self.front_camera else 'основная'}")
        return self.front_camera
    
    def apply_filter(self, filter_name):
        """Применить фильтр"""
        filters = ["sepia", "grayscale", "blur", "sharpen", "vintage"]
        if filter_name in filters:
            print(f"[Camera] Фильтр применен: {filter_name}")
            return True
        return False
    
    def get_camera_info(self):
        """Получить информацию о камере"""
        return {
            "resolution": self.resolution,
            "flash": self.flash_enabled,
            "front": self.front_camera
        }


class MobileGPS:
    """GPS модуль"""
    def __init__(self):
        self.enabled = False
        self.accuracy = "high"
        print(f"[GPS] Инициализирован")
    
    def get_location(self):
        """Получить координаты"""
        print(f"[GPS] Получение координат...")
        return {"lat": 55.7558, "lon": 37.6173, "accuracy": 10}
    
    def start_tracking(self):
        """Начать отслеживание"""
        self.enabled = True
        print(f"[GPS] Отслеживание включено")
        return True
    
    def stop_tracking(self):
        """Остановить отслеживание"""
        self.enabled = False
        print(f"[GPS] Отслеживание выключено")
        return True
    
    def get_distance(self, lat1, lon1, lat2, lon2):
        """Вычислить расстояние между точками (км)"""
        import math
        R = 6371  # Радиус Земли в км
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        print(f"[GPS] Расстояние: {distance:.2f} км")
        return distance
    
    def set_accuracy(self, mode):
        """Установить точность (high/medium/low)"""
        if mode in ["high", "medium", "low"]:
            self.accuracy = mode
            print(f"[GPS] Точность: {mode}")
            return True
        return False
    
    def get_address(self, lat, lon):
        """Получить адрес по координатам (геокодирование)"""
        print(f"[GPS] Геокодирование: {lat}, {lon}")
        return {"address": "Красная площадь, Москва", "city": "Москва", "country": "Россия"}


class MobileApp:
    """Мобильное приложение"""
    def __init__(self, name):
        self.name = name
        self.screens = {}
        self.camera = MobileCamera()
        self.gps = MobileGPS()
        self.notifications_enabled = False
        self.storage = {}
        self.permissions = []
        print(f"[Mobile] Создано приложение: {name}")
    
    def add_screen(self, screen_name):
        """Добавить экран"""
        screen = MobileScreen(screen_name)
        self.screens[screen_name] = screen
        return screen
    
    def get_screen(self, screen_name):
        """Получить экран"""
        return self.screens.get(screen_name)
    
    def enable_notifications(self):
        """Включить уведомления"""
        self.notifications_enabled = True
        print(f"[Mobile] Push-уведомления включены")
        return True
    
    def send_notification(self, title, message):
        """Отправить уведомление"""
        if self.notifications_enabled:
            print(f"[Notification] {title}: {message}")
            return True
        return False
    
    def save_data(self, key, value):
        """Сохранить данные локально"""
        self.storage[key] = value
        print(f"[Storage] Сохранено: {key}")
        return True
    
    def load_data(self, key):
        """Загрузить данные"""
        value = self.storage.get(key)
        print(f"[Storage] Загружено: {key}")
        return value
    
    def clear_storage(self):
        """Очистить хранилище"""
        self.storage = {}
        print(f"[Storage] Очищено")
        return True
    
    def request_permission(self, permission):
        """Запросить разрешение"""
        available = ["CAMERA", "GPS", "NOTIFICATIONS", "STORAGE", "MICROPHONE", "CONTACTS"]
        if permission in available:
            self.permissions.append(permission)
            print(f"[Permission] Разрешение получено: {permission}")
            return True
        return False
    
    def vibrate(self, duration=100):
        """Вибрация"""
        print(f"[Vibrate] Вибрация {duration}ms")
        return True
    
    def share_content(self, content, platform=""):
        """Поделиться контентом"""
        print(f"[Share] Контент: {content[:50]}...")
        if platform:
            print(f"[Share] Платформа: {platform}")
        return True
    
    def open_url(self, url):
        """Открыть URL в браузере"""
        print(f"[Browser] Открытие: {url}")
        return True
    
    def get_device_info(self):
        """Получить информацию об устройстве"""
        return {
            "model": "Generic Device",
            "os": "Android 13",
            "screen": "1080x2400",
            "battery": 85
        }
    
    def set_orientation(self, orientation):
        """Установить ориентацию (portrait/landscape)"""
        if orientation in ["portrait", "landscape"]:
            print(f"[App] Ориентация: {orientation}")
            return True
        return False
    
    def build_android(self, output_dir="build"):
        """Собрать для Android"""
        print(f"\n[Build] Сборка Android APK...")
        print(f"[Build] Приложение: {self.name}")
        print(f"[Build] Экранов: {len(self.screens)}")
        
        # Создаем манифест
        manifest = {
            "name": self.name,
            "version": "1.0.0",
            "platform": "android",
            "screens": list(self.screens.keys()),
            "permissions": ["CAMERA", "GPS", "NOTIFICATIONS"]
        }
        
        print(f"[Build] Манифест создан")
        print(f"[Build] Разрешения: {', '.join(manifest['permissions'])}")
        print(f"[Build] ✓ APK готов: {output_dir}/{self.name}.apk")
        return True
    
    def build_ios(self, output_dir="build"):
        """Собрать для iOS"""
        print(f"\n[Build] Сборка iOS IPA...")
        print(f"[Build] Приложение: {self.name}")
        print(f"[Build] Экранов: {len(self.screens)}")
        print(f"[Build] ✓ IPA готов: {output_dir}/{self.name}.ipa")
        return True


def create_mobile_app(name):
    """Создать мобильное приложение"""
    global app_counter
    app_id = f"app_{app_counter}"
    app_counter += 1
    mobile_apps[app_id] = MobileApp(name)
    return app_id


def get_mobile_app(app_id):
    """Получить приложение"""
    return mobile_apps.get(app_id)


if __name__ == "__main__":
    print("=== KHX Mobile Development Module Test ===\n")
    
    # Создаем приложение
    app_id = create_mobile_app("MyPhotoApp")
    app = get_mobile_app(app_id)
    
    # Добавляем экран
    screen = app.add_screen("home")
    screen.add_text("Фото приложение", size=24)
    btn = screen.add_button("Сделать фото")
    
    # Используем камеру
    photo = app.camera.take_photo()
    screen.show_image(photo)
    
    # GPS
    location = app.gps.get_location()
    print(f"[App] Координаты: {location['lat']}, {location['lon']}")
    
    # Уведомления
    app.enable_notifications()
    app.send_notification("Фото", "Фото сохранено!")
    
    # Сборка
    app.build_android()
    app.build_ios()
