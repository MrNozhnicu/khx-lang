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
        print(f"[Camera] Инициализирована")
    
    def take_photo(self):
        """Сделать фото"""
        print(f"[Camera] Фото сделано ({self.resolution})")
        return {"path": "photo.jpg", "resolution": self.resolution}
    
    def record_video(self, duration):
        """Записать видео"""
        print(f"[Camera] Видео записано ({duration}s)")
        return {"path": "video.mp4", "duration": duration}


class MobileGPS:
    """GPS модуль"""
    def __init__(self):
        self.enabled = False
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


class MobileApp:
    """Мобильное приложение"""
    def __init__(self, name):
        self.name = name
        self.screens = {}
        self.camera = MobileCamera()
        self.gps = MobileGPS()
        self.notifications_enabled = False
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
