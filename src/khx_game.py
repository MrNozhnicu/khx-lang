#!/usr/bin/env python3
"""
KHX Game Engine Module
"""

import time
import random


class KHXSprite:
    """Game Sprite"""
    
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.velocity_x = 0
        self.velocity_y = 0
        self.visible = True
        self.rotation = 0
        self.scale = 1.0
        self.health = 100
        self.gravity = 0
    
    def move(self, dx, dy):
        """Move sprite"""
        self.x += dx
        self.y += dy
    
    def set_velocity(self, vx, vy):
        """Set velocity"""
        self.velocity_x = vx
        self.velocity_y = vy
    
    def update(self):
        """Update sprite"""
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.velocity_y += self.gravity
    
    def collides_with(self, other):
        """Check collision"""
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)
    
    def rotate(self, angle):
        """Rotate sprite"""
        self.rotation += angle
        self.rotation %= 360
    
    def set_scale(self, scale):
        """Set scale"""
        self.scale = scale
        self.width = int(32 * scale)
        self.height = int(32 * scale)
    
    def hide(self):
        """Hide sprite"""
        self.visible = False
    
    def show(self):
        """Show sprite"""
        self.visible = True
    
    def take_damage(self, damage):
        """Take damage"""
        self.health -= damage
        return self.health > 0
    
    def heal(self, amount):
        """Heal sprite"""
        self.health = min(100, self.health + amount)


class KHXGame:
    """Game Engine"""
    
    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title
        self.sprites = []
        self.running = False
        self.fps = 60
        self.score = 0
        self.level = 1
        self.paused = False
        self.update_callback = None
        self.draw_callback = None
        self.key_handlers = {}
        self.mouse_handlers = {}
        
        print(f"[GAME] Created: {title} ({width}x{height})")
    
    def add_sprite(self, image, x, y):
        """Add sprite"""
        sprite = KHXSprite(image, x, y)
        self.sprites.append(sprite)
        print(f"[GAME] Sprite added: {image} at ({x}, {y})")
        return sprite
    
    def remove_sprite(self, sprite):
        """Remove sprite"""
        if sprite in self.sprites:
            self.sprites.remove(sprite)
    
    def on_update(self, callback):
        """Set update callback"""
        self.update_callback = callback
    
    def on_draw(self, callback):
        """Set draw callback"""
        self.draw_callback = callback
    
    def on_key_press(self, key, callback):
        """Register key press handler"""
        self.key_handlers[key] = callback
        print(f"[GAME] Key handler registered: {key}")
    
    def on_mouse_click(self, callback):
        """Register mouse click handler"""
        self.mouse_handlers['click'] = callback
        print(f"[GAME] Mouse click handler registered")
    
    def run(self):
        """Run game loop"""
        self.running = True
        print(f"[GAME] Starting game loop at {self.fps} FPS")
        
        frame_count = 0
        max_frames = 100  # Limit for demo
        
        while self.running and frame_count < max_frames:
            if not self.paused:
                # Update
                if self.update_callback:
                    self.update_callback()
                
                # Update sprites
                for sprite in self.sprites:
                    sprite.update()
                
                # Draw
                if self.draw_callback:
                    self.draw_callback()
            
            frame_count += 1
            time.sleep(1 / self.fps)
        
        print(f"[GAME] Game stopped after {frame_count} frames")
    
    def stop(self):
        """Stop game"""
        self.running = False
    
    def pause(self):
        """Pause game"""
        self.paused = True
        print(f"[GAME] Game paused")
    
    def resume(self):
        """Resume game"""
        self.paused = False
        print(f"[GAME] Game resumed")
    
    def check_collisions(self):
        """Check all collisions"""
        collisions = []
        for i, sprite1 in enumerate(self.sprites):
            for sprite2 in self.sprites[i+1:]:
                if sprite1.collides_with(sprite2):
                    collisions.append((sprite1, sprite2))
        return collisions
    
    def play_sound(self, sound_file):
        """Play sound (placeholder)"""
        print(f"[GAME] Playing sound: {sound_file}")
    
    def set_background(self, color):
        """Set background color"""
        print(f"[GAME] Background set to: {color}")
    
    def add_score(self, points):
        """Add to score"""
        self.score += points
        print(f"[GAME] Score: {self.score}")
        return self.score
    
    def next_level(self):
        """Go to next level"""
        self.level += 1
        print(f"[GAME] Level: {self.level}")
        return self.level
    
    def reset(self):
        """Reset game"""
        self.score = 0
        self.level = 1
        self.sprites = []
        print(f"[GAME] Game reset")
    
    def spawn_enemy(self, x, y, enemy_type="basic"):
        """Spawn enemy"""
        enemy = self.add_sprite(f"enemy_{enemy_type}", x, y)
        enemy.velocity_x = random.uniform(-2, 2)
        enemy.velocity_y = random.uniform(-2, 2)
        print(f"[GAME] Enemy spawned: {enemy_type}")
        return enemy
    
    def spawn_powerup(self, x, y, powerup_type="health"):
        """Spawn power-up"""
        powerup = self.add_sprite(f"powerup_{powerup_type}", x, y)
        print(f"[GAME] Power-up spawned: {powerup_type}")
        return powerup
    
    def set_gravity(self, gravity):
        """Set gravity for physics"""
        for sprite in self.sprites:
            sprite.gravity = gravity
        print(f"[GAME] Gravity set: {gravity}")
    
    def get_sprites_at(self, x, y):
        """Get sprites at position"""
        result = []
        for sprite in self.sprites:
            if (sprite.x <= x <= sprite.x + sprite.width and
                sprite.y <= y <= sprite.y + sprite.height):
                result.append(sprite)
        return result


# Global registry
_games = {}
_game_counter = 0


def create_game(width, height, title):
    """Create game"""
    global _game_counter
    game = KHXGame(width, height, title)
    game_id = f"game_{_game_counter}"
    _games[game_id] = game
    _game_counter += 1
    return game_id


def get_game(game_id):
    """Get game"""
    return _games.get(game_id)
