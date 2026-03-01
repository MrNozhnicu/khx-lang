"""
KHX Audio Module - Работа со звуком и музыкой
"""

import time


class AudioObject:
    """Аудио объект"""
    
    def __init__(self, filename):
        self.filename = filename
        self.volume = 1.0
        self.playing = False
        self.loop = False
        self.position = 0
        self.duration = 180  # 3 минуты
        print(f"[Audio] Загружен: {filename}")
    
    def apply_effect(self, effect_name, intensity=0.5):
        """Применить эффект"""
        effects = ["reverb", "echo", "distortion", "chorus", "flanger", "delay"]
        if effect_name in effects:
            print(f"[Audio] Эффект '{effect_name}' применен (интенсивность: {intensity})")
            return True
        return False
    
    def set_volume(self, volume):
        """Установить громкость (0.0 - 1.0)"""
        self.volume = max(0.0, min(1.0, volume))
        print(f"[Audio] Громкость: {self.volume * 100:.0f}%")
        return True
    
    def play(self):
        """Воспроизвести"""
        self.playing = True
        print(f"[Audio] Воспроизведение: {self.filename}")
        return True
    
    def pause(self):
        """Пауза"""
        self.playing = False
        print(f"[Audio] Пауза")
        return True
    
    def stop(self):
        """Остановить"""
        self.playing = False
        self.position = 0
        print(f"[Audio] Остановлено")
        return True
    
    def seek(self, position):
        """Перемотать на позицию (секунды)"""
        self.position = max(0, min(self.duration, position))
        print(f"[Audio] Позиция: {self.position}s")
        return True
    
    def set_loop(self, loop):
        """Установить зацикливание"""
        self.loop = loop
        print(f"[Audio] Зацикливание: {'вкл' if loop else 'выкл'}")
        return True
    
    def fade_in(self, duration=2.0):
        """Плавное появление"""
        print(f"[Audio] Fade in ({duration}s)")
        return True
    
    def fade_out(self, duration=2.0):
        """Плавное затухание"""
        print(f"[Audio] Fade out ({duration}s)")
        return True
    
    def get_info(self):
        """Получить информацию"""
        return {
            "filename": self.filename,
            "duration": self.duration,
            "position": self.position,
            "volume": self.volume,
            "playing": self.playing,
            "loop": self.loop
        }
    
    def set_speed(self, speed):
        """Установить скорость воспроизведения"""
        print(f"[Audio] Скорость: {speed}x")
        return True
    
    def normalize(self):
        """Нормализовать громкость"""
        print(f"[Audio] Нормализация выполнена")
        return True
    
    def trim(self, start, end):
        """Обрезать аудио"""
        print(f"[Audio] Обрезано: {start}s - {end}s")
        return True
    
    def export(self, filename, format="mp3"):
        """Экспортировать в файл"""
        formats = ["mp3", "wav", "ogg", "flac"]
        if format in formats:
            print(f"[Audio] Экспортировано: {filename}.{format}")
            return True
        return False


class AudioMixer:
    """Аудио микшер"""
    
    def __init__(self):
        self.tracks = []
        self.master_volume = 1.0
        print(f"[Mixer] Инициализирован")
    
    def add_track(self, audio):
        """Добавить трек"""
        self.tracks.append(audio)
        print(f"[Mixer] Трек добавлен: {audio.filename}")
        return len(self.tracks) - 1
    
    def remove_track(self, index):
        """Удалить трек"""
        if 0 <= index < len(self.tracks):
            track = self.tracks.pop(index)
            print(f"[Mixer] Трек удален: {track.filename}")
            return True
        return False
    
    def set_master_volume(self, volume):
        """Установить общую громкость"""
        self.master_volume = max(0.0, min(1.0, volume))
        print(f"[Mixer] Общая громкость: {self.master_volume * 100:.0f}%")
        return True
    
    def play_all(self):
        """Воспроизвести все треки"""
        for track in self.tracks:
            track.play()
        print(f"[Mixer] Воспроизведение {len(self.tracks)} треков")
        return True
    
    def stop_all(self):
        """Остановить все треки"""
        for track in self.tracks:
            track.stop()
        print(f"[Mixer] Все треки остановлены")
        return True


# Global storage
audio_objects = {}
audio_counter = 0
mixers = {}
mixer_counter = 0


def load_audio(filename):
    """Загрузить аудио файл"""
    global audio_counter
    audio_id = f"audio_{audio_counter}"
    audio_counter += 1
    audio_objects[audio_id] = AudioObject(filename)
    return audio_id


def get_audio(audio_id):
    """Получить аудио объект"""
    return audio_objects.get(audio_id)


def create_mixer():
    """Создать микшер"""
    global mixer_counter
    mixer_id = f"mixer_{mixer_counter}"
    mixer_counter += 1
    mixers[mixer_id] = AudioMixer()
    return mixer_id


def get_mixer(mixer_id):
    """Получить микшер"""
    return mixers.get(mixer_id)


if __name__ == "__main__":
    print("=== KHX Audio Module Test ===\n")
    
    # Загрузка аудио
    audio_id = load_audio("song.mp3")
    audio = get_audio(audio_id)
    
    # Управление воспроизведением
    audio.play()
    audio.set_volume(0.8)
    audio.set_loop(True)
    audio.apply_effect("reverb", 0.7)
    
    # Микшер
    mixer_id = create_mixer()
    mixer = get_mixer(mixer_id)
    mixer.add_track(audio)
    mixer.set_master_volume(0.9)
    mixer.play_all()
