#!/usr/bin/env python3
"""
KHX Advanced CLI Module
"""

import sys
import time


class KHXColor:
    """ANSI color codes"""
    
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


class KHXCLI:
    """CLI utilities"""
    
    @staticmethod
    def print_colored(text, color="white", bold=False):
        """Print colored text"""
        colors = {
            "black": KHXColor.BLACK,
            "red": KHXColor.RED,
            "green": KHXColor.GREEN,
            "yellow": KHXColor.YELLOW,
            "blue": KHXColor.BLUE,
            "magenta": KHXColor.MAGENTA,
            "cyan": KHXColor.CYAN,
            "white": KHXColor.WHITE
        }
        
        color_code = colors.get(color.lower(), KHXColor.WHITE)
        bold_code = KHXColor.BOLD if bold else ""
        
        print(f"{bold_code}{color_code}{text}{KHXColor.RESET}")
    
    @staticmethod
    def print_table(data, headers=None):
        """Print table"""
        if not data:
            return
        
        # Calculate column widths
        if headers:
            col_widths = [len(str(h)) for h in headers]
        else:
            col_widths = [0] * len(data[0])
        
        for row in data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Print headers
        if headers:
            header_row = " | ".join(str(h).ljust(w) for h, w in zip(headers, col_widths))
            print(header_row)
            print("-" * len(header_row))
        
        # Print rows
        for row in data:
            print(" | ".join(str(cell).ljust(w) for cell, w in zip(row, col_widths)))
    
    @staticmethod
    def progress_bar(current, total, width=40, prefix="Progress"):
        """Print progress bar"""
        percent = current / total if total > 0 else 0
        filled = int(width * percent)
        bar = '█' * filled + '░' * (width - filled)
        
        sys.stdout.write(f'\r{prefix}: |{bar}| {percent*100:.1f}%')
        sys.stdout.flush()
        
        if current >= total:
            print()  # New line when complete
    
    @staticmethod
    def spinner(message="Loading", duration=2):
        """Show spinner"""
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        end_time = time.time() + duration
        i = 0
        
        while time.time() < end_time:
            sys.stdout.write(f'\r{message} {frames[i % len(frames)]}')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        
        sys.stdout.write(f'\r{message} ✓\n')
        sys.stdout.flush()
    
    @staticmethod
    def prompt(message, default=None):
        """Prompt for input"""
        if default:
            message = f"{message} [{default}]: "
        else:
            message = f"{message}: "
        
        response = input(message)
        return response if response else default
    
    @staticmethod
    def prompt_select(message, options):
        """Prompt for selection"""
        print(message)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                choice = int(input("Select (number): "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
    
    @staticmethod
    def prompt_confirm(message, default=True):
        """Prompt for confirmation"""
        suffix = " [Y/n]: " if default else " [y/N]: "
        response = input(message + suffix).lower()
        
        if not response:
            return default
        
        return response in ['y', 'yes']
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        print('\033[2J\033[H', end='')
    
    @staticmethod
    def print_box(text, width=None, padding=1):
        """Print text in a box"""
        lines = text.split('\n')
        if width is None:
            width = max(len(line) for line in lines) + padding * 2
        
        print('┌' + '─' * width + '┐')
        for line in lines:
            padded = line.center(width)
            print(f'│{padded}│')
        print('└' + '─' * width + '┘')
    
    @staticmethod
    def print_success(message):
        """Print success message"""
        KHXCLI.print_colored(f"✓ {message}", "green", bold=True)
    
    @staticmethod
    def print_error(message):
        """Print error message"""
        KHXCLI.print_colored(f"✗ {message}", "red", bold=True)
    
    @staticmethod
    def print_warning(message):
        """Print warning message"""
        KHXCLI.print_colored(f"⚠ {message}", "yellow", bold=True)
    
    @staticmethod
    def print_info(message):
        """Print info message"""
        KHXCLI.print_colored(f"ℹ {message}", "blue")


# Export functions
def print_colored(text, color="white"):
    KHXCLI.print_colored(text, color)


def print_table(data, headers=None):
    KHXCLI.print_table(data, headers)


def progress_bar(current, total):
    KHXCLI.progress_bar(current, total)


def spinner(message="Loading", duration=2):
    KHXCLI.spinner(message, duration)


def prompt(message, default=None):
    return KHXCLI.prompt(message, default)


def prompt_select(message, options):
    return KHXCLI.prompt_select(message, options)


def print_success(message):
    KHXCLI.print_success(message)


def print_error(message):
    KHXCLI.print_error(message)


def print_box(text):
    KHXCLI.print_box(text)
