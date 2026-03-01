#!/usr/bin/env python3
"""
KHX Testing Framework
"""

import time
import traceback


class KHXTest:
    """Test case"""
    
    def __init__(self, name, func):
        self.name = name
        self.func = func
        self.passed = False
        self.error = None
        self.duration = 0
    
    def run(self):
        """Run test"""
        print(f"  Running: {self.name}...", end=" ")
        start = time.time()
        
        try:
            self.func()
            self.passed = True
            self.duration = time.time() - start
            print(f"✓ PASS ({self.duration:.3f}s)")
            return True
        except AssertionError as e:
            self.passed = False
            self.error = str(e)
            self.duration = time.time() - start
            print(f"✗ FAIL ({self.duration:.3f}s)")
            print(f"    Error: {self.error}")
            return False
        except Exception as e:
            self.passed = False
            self.error = str(e)
            self.duration = time.time() - start
            print(f"✗ ERROR ({self.duration:.3f}s)")
            print(f"    Error: {self.error}")
            return False


class KHXTestSuite:
    """Test suite"""
    
    def __init__(self, name):
        self.name = name
        self.tests = []
        self.passed = 0
        self.failed = 0
        self.total_duration = 0
    
    def add_test(self, name, func):
        """Add test"""
        test = KHXTest(name, func)
        self.tests.append(test)
    
    def run(self):
        """Run all tests"""
        print(f"\n{'='*60}")
        print(f"Test Suite: {self.name}")
        print(f"{'='*60}")
        
        for test in self.tests:
            if test.run():
                self.passed += 1
            else:
                self.failed += 1
            self.total_duration += test.duration
        
        print(f"\n{'='*60}")
        print(f"Results: {self.passed} passed, {self.failed} failed")
        print(f"Duration: {self.total_duration:.3f}s")
        print(f"{'='*60}\n")
        
        return self.failed == 0


class KHXAssert:
    """Assertion utilities"""
    
    @staticmethod
    def equal(actual, expected, message=""):
        """Assert equal"""
        if actual != expected:
            msg = message or f"Expected {expected}, got {actual}"
            raise AssertionError(msg)
    
    @staticmethod
    def not_equal(actual, expected, message=""):
        """Assert not equal"""
        if actual == expected:
            msg = message or f"Expected not {expected}, got {actual}"
            raise AssertionError(msg)
    
    @staticmethod
    def true(value, message=""):
        """Assert true"""
        if not value:
            msg = message or f"Expected True, got {value}"
            raise AssertionError(msg)
    
    @staticmethod
    def false(value, message=""):
        """Assert false"""
        if value:
            msg = message or f"Expected False, got {value}"
            raise AssertionError(msg)
    
    @staticmethod
    def greater(actual, expected, message=""):
        """Assert greater than"""
        if not actual > expected:
            msg = message or f"Expected {actual} > {expected}"
            raise AssertionError(msg)
    
    @staticmethod
    def less(actual, expected, message=""):
        """Assert less than"""
        if not actual < expected:
            msg = message or f"Expected {actual} < {expected}"
            raise AssertionError(msg)
    
    @staticmethod
    def contains(container, item, message=""):
        """Assert contains"""
        if item not in container:
            msg = message or f"Expected {container} to contain {item}"
            raise AssertionError(msg)


class KHXBenchmark:
    """Benchmarking utilities"""
    
    @staticmethod
    def measure(func, iterations=1000):
        """Measure execution time"""
        print(f"\n[Benchmark] Running {iterations} iterations...")
        
        start = time.time()
        for _ in range(iterations):
            func()
        duration = time.time() - start
        
        avg = duration / iterations
        print(f"[Benchmark] Total: {duration:.6f}s")
        print(f"[Benchmark] Average: {avg:.9f}s per iteration")
        print(f"[Benchmark] Throughput: {iterations/duration:.2f} ops/sec")
        
        return duration


class KHXMock:
    """Mock object"""
    
    def __init__(self, name="Mock"):
        self.name = name
        self.calls = []
        self.return_value = None
    
    def __call__(self, *args, **kwargs):
        """Record call"""
        self.calls.append((args, kwargs))
        return self.return_value
    
    def set_return_value(self, value):
        """Set return value"""
        self.return_value = value
    
    def called(self):
        """Check if called"""
        return len(self.calls) > 0
    
    def call_count(self):
        """Get call count"""
        return len(self.calls)
    
    def reset(self):
        """Reset mock"""
        self.calls = []


# Global registry
_test_suites = {}
_suite_counter = 0


def create_test_suite(name):
    """Create test suite"""
    global _suite_counter
    suite = KHXTestSuite(name)
    suite_id = f"suite_{_suite_counter}"
    _test_suites[suite_id] = suite
    _suite_counter += 1
    return suite_id


def get_test_suite(suite_id):
    """Get test suite"""
    return _test_suites.get(suite_id)


def assert_equal(actual, expected):
    """Assert equal"""
    KHXAssert.equal(actual, expected)


def assert_true(value):
    """Assert true"""
    KHXAssert.true(value)


def assert_false(value):
    """Assert false"""
    KHXAssert.false(value)


def create_mock(name="Mock"):
    """Create mock"""
    return KHXMock(name)


def benchmark(func, iterations=1000):
    """Benchmark function"""
    return KHXBenchmark.measure(func, iterations)
