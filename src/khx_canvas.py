#!/usr/bin/env python3
"""
KHX Canvas & Graphics Module
"""

from PIL import Image, ImageDraw, ImageFont
import math


class KHXCanvas:
    """2D Canvas for drawing"""
    
    def __init__(self, width, height, background="white"):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), background)
        self.draw = ImageDraw.Draw(self.image)
        print(f"[Canvas] Created {width}x{height}")
    
    def draw_line(self, x1, y1, x2, y2, color="black", width=1):
        """Draw line"""
        self.draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
        print(f"[Canvas] Line: ({x1},{y1}) to ({x2},{y2})")
    
    def draw_rectangle(self, x, y, width, height, color="black", fill=None):
        """Draw rectangle"""
        self.draw.rectangle([(x, y), (x + width, y + height)], 
                           outline=color, fill=fill)
        print(f"[Canvas] Rectangle at ({x},{y})")
    
    def draw_circle(self, x, y, radius, color="black", fill=None):
        """Draw circle"""
        self.draw.ellipse([(x - radius, y - radius), 
                          (x + radius, y + radius)], 
                         outline=color, fill=fill)
        print(f"[Canvas] Circle at ({x},{y}) r={radius}")
    
    def draw_ellipse(self, x, y, width, height, color="black", fill=None):
        """Draw ellipse"""
        self.draw.ellipse([(x, y), (x + width, y + height)], 
                         outline=color, fill=fill)
        print(f"[Canvas] Ellipse at ({x},{y})")
    
    def draw_polygon(self, points, color="black", fill=None):
        """Draw polygon"""
        self.draw.polygon(points, outline=color, fill=fill)
        print(f"[Canvas] Polygon with {len(points)} points")
    
    def draw_text(self, x, y, text, color="black", size=12):
        """Draw text"""
        try:
            font = ImageFont.truetype("arial.ttf", size)
        except:
            font = ImageFont.load_default()
        
        self.draw.text((x, y), text, fill=color, font=font)
        print(f"[Canvas] Text at ({x},{y}): {text}")
    
    def fill(self, color):
        """Fill canvas with color"""
        self.draw.rectangle([(0, 0), (self.width, self.height)], fill=color)
        print(f"[Canvas] Filled with {color}")
    
    def clear(self):
        """Clear canvas"""
        self.fill("white")
    
    def save(self, filename):
        """Save to file"""
        self.image.save(filename)
        print(f"[Canvas] Saved to {filename}")
        return True
    
    def get_pixel(self, x, y):
        """Get pixel color"""
        return self.image.getpixel((x, y))
    
    def set_pixel(self, x, y, color):
        """Set pixel color"""
        self.draw.point((x, y), fill=color)


class KHXGradient:
    """Gradient generator"""
    
    @staticmethod
    def linear(start_color, end_color, steps):
        """Generate linear gradient"""
        # Parse RGB colors
        start_rgb = KHXGradient._parse_color(start_color)
        end_rgb = KHXGradient._parse_color(end_color)
        
        gradient = []
        for i in range(steps):
            ratio = i / (steps - 1) if steps > 1 else 0
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * ratio)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * ratio)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * ratio)
            gradient.append((r, g, b))
        
        return gradient
    
    @staticmethod
    def _parse_color(color):
        """Parse color string to RGB"""
        if isinstance(color, tuple):
            return color
        
        # Simple color names
        colors = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "yellow": (255, 255, 0),
            "cyan": (0, 255, 255),
            "magenta": (255, 0, 255)
        }
        
        return colors.get(color.lower(), (0, 0, 0))


class KHXShape:
    """Shape utilities"""
    
    @staticmethod
    def star(cx, cy, radius, points=5):
        """Generate star points"""
        coords = []
        angle = math.pi / points
        
        for i in range(points * 2):
            r = radius if i % 2 == 0 else radius / 2
            x = cx + r * math.cos(i * angle - math.pi / 2)
            y = cy + r * math.sin(i * angle - math.pi / 2)
            coords.append((x, y))
        
        return coords
    
    @staticmethod
    def regular_polygon(cx, cy, radius, sides):
        """Generate regular polygon points"""
        coords = []
        angle = 2 * math.pi / sides
        
        for i in range(sides):
            x = cx + radius * math.cos(i * angle - math.pi / 2)
            y = cy + radius * math.sin(i * angle - math.pi / 2)
            coords.append((x, y))
        
        return coords


# Global registry
_canvases = {}
_canvas_counter = 0


def create_canvas(width, height, background="white"):
    """Create canvas"""
    global _canvas_counter
    canvas = KHXCanvas(width, height, background)
    canvas_id = f"canvas_{_canvas_counter}"
    _canvases[canvas_id] = canvas
    _canvas_counter += 1
    return canvas_id


def get_canvas(canvas_id):
    """Get canvas"""
    return _canvases.get(canvas_id)
