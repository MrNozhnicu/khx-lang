"""
KHX Debugging Tools Module
Инструменты отладки и профилирования
"""

import time
import sys
from collections import defaultdict

# Storage
breakpoints = {}
profiler_data = defaultdict(lambda: {'calls': 0, 'total_time': 0})
debug_enabled = True
call_stack = []


class Debugger:
    """Отладчик"""
    def __init__(self):
        self.breakpoints = set()
        self.variables = {}
        self.step_mode = False
        print(f"[Debug] Отладчик инициализирован")
    
    def set_breakpoint(self, line):
        """Установить точку останова"""
        self.breakpoints.add(line)
        print(f"[Debug] Breakpoint установлен на строке {line}")
        return True
    
    def remove_breakpoint(self, line):
        """Удалить точку останова"""
        if line in self.breakpoints:
            self.breakpoints.remove(line)
            print(f"[Debug] Breakpoint удален со строки {line}")
            return True
        return False
    
    def list_breakpoints(self):
        """Список точек останова"""
        print(f"\n[Debug] Точки останова ({len(self.breakpoints)}):")
        for bp in sorted(self.breakpoints):
            print(f"  • Строка {bp}")
        return list(self.breakpoints)

    def inspect_variable(self, var_name):
        """Инспектировать переменную"""
        if var_name in self.variables:
            value = self.variables[var_name]
            print(f"\n[Debug] Переменная: {var_name}")
            print(f"  Тип: {type(value).__name__}")
            print(f"  Значение: {value}")
            return value
        else:
            print(f"[Debug] ✗ Переменная '{var_name}' не найдена")
            return None


def debug_breakpoint():
    """Точка останова"""
    if debug_enabled:
        print(f"\n[Debug] ⚠ BREAKPOINT")
        print(f"[Debug] Стек вызовов: {len(call_stack)} уровней")
        for i, frame in enumerate(call_stack[-5:]):
            print(f"  {i+1}. {frame}")
        return True
    return False


def debug_log(*args):
    """Отладочный лог"""
    if debug_enabled:
        message = ' '.join(str(arg) for arg in args)
        print(f"[Debug] {message}")
        return True
    return False


def profile_start(name):
    """Начать профилирование"""
    profiler_data[name]['start_time'] = time.time()
    profiler_data[name]['calls'] += 1
    print(f"[Profiler] Начало: {name}")


def profile_end(name):
    """Закончить профилирование"""
    if 'start_time' in profiler_data[name]:
        elapsed = time.time() - profiler_data[name]['start_time']
        profiler_data[name]['total_time'] += elapsed
        print(f"[Profiler] Конец: {name} ({elapsed*1000:.2f}ms)")
        del profiler_data[name]['start_time']
        return elapsed
    return 0


def profile_report():
    """Отчет профилирования"""
    print(f"\n[Profiler] Отчет:")
    print(f"{'Функция':<30} {'Вызовов':<10} {'Время (ms)':<15} {'Среднее (ms)':<15}")
    print("-" * 70)
    
    for name, data in sorted(profiler_data.items(), key=lambda x: x[1]['total_time'], reverse=True):
        calls = data['calls']
        total = data['total_time'] * 1000
        avg = total / calls if calls > 0 else 0
        print(f"{name:<30} {calls:<10} {total:<15.2f} {avg:<15.2f}")


def get_call_stack():
    """Получить стек вызовов"""
    return call_stack.copy()


def push_call(func_name):
    """Добавить в стек"""
    call_stack.append(func_name)


def pop_call():
    """Убрать из стека"""
    if call_stack:
        call_stack.pop()


def memory_usage():
    """Использование памяти"""
    import sys
    objects = len(sys.gettrace() or [])
    print(f"[Debug] Объектов в памяти: ~{objects}")
    return objects


if __name__ == "__main__":
    print("=== KHX Debugging Tools Test ===\n")
    
    # Тест отладки
    debugger = Debugger()
    debugger.set_breakpoint(10)
    debugger.set_breakpoint(25)
    debugger.list_breakpoints()
    
    # Тест логирования
    print("\nТест логирования:")
    debug_log("Начало выполнения")
    debug_log("Значение X:", 42)
    debug_breakpoint()
    
    # Тест профилирования
    print("\nТест профилирования:")
    
    def test_function():
        profile_start("test_function")
        time.sleep(0.01)
        profile_end("test_function")
    
    def another_function():
        profile_start("another_function")
        time.sleep(0.02)
        profile_end("another_function")
    
    # Вызываем несколько раз
    for i in range(3):
        test_function()
        another_function()
    
    # Отчет
    profile_report()
    
    # Стек вызовов
    print("\nТест стека вызовов:")
    push_call("main()")
    push_call("process_data()")
    push_call("validate()")
    print(f"Стек: {get_call_stack()}")
    pop_call()
    print(f"Стек: {get_call_stack()}")
