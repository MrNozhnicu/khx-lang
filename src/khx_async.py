#!/usr/bin/env python3
"""
KHX Async/Await Module
"""

import asyncio
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class KHXPromise:
    """Promise implementation"""
    
    def __init__(self, executor_func):
        self.executor_func = executor_func
        self.result = None
        self.error = None
        self.resolved = False
        self.rejected = False
        self.callbacks = []
        self.error_callbacks = []
        
        # Execute immediately
        threading.Thread(target=self._execute).start()
    
    def _execute(self):
        """Execute promise"""
        try:
            def resolve(value):
                self.result = value
                self.resolved = True
                for callback in self.callbacks:
                    callback(value)
            
            def reject(error):
                self.error = error
                self.rejected = True
                for callback in self.error_callbacks:
                    callback(error)
            
            self.executor_func(resolve, reject)
        except Exception as e:
            self.error = str(e)
            self.rejected = True
    
    def then(self, callback):
        """Add success callback"""
        if self.resolved:
            callback(self.result)
        else:
            self.callbacks.append(callback)
        return self
    
    def catch(self, callback):
        """Add error callback"""
        if self.rejected:
            callback(self.error)
        else:
            self.error_callbacks.append(callback)
        return self
    
    def wait(self, timeout=None):
        """Wait for promise to resolve"""
        start = time.time()
        while not self.resolved and not self.rejected:
            if timeout and (time.time() - start) > timeout:
                raise TimeoutError("Promise timeout")
            time.sleep(0.01)
        
        if self.rejected:
            raise Exception(self.error)
        return self.result


class KHXAsync:
    """Async utilities"""
    
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=10)
    
    def run_async(self, func, *args):
        """Run function asynchronously"""
        future = self.executor.submit(func, *args)
        return future
    
    def sleep(self, seconds):
        """Async sleep"""
        time.sleep(seconds)
    
    def parallel(self, *funcs):
        """Run functions in parallel"""
        futures = [self.executor.submit(func) for func in funcs]
        results = [future.result() for future in futures]
        return results


class KHXChannel:
    """Channel for communication between coroutines"""
    
    def __init__(self, buffer_size=0):
        self.buffer_size = buffer_size
        self.queue = []
        self.closed = False
    
    def send(self, value):
        """Send value to channel"""
        if self.closed:
            raise Exception("Channel closed")
        
        if self.buffer_size > 0 and len(self.queue) >= self.buffer_size:
            raise Exception("Channel buffer full")
        
        self.queue.append(value)
        print(f"[Channel] Sent: {value}")
    
    def receive(self):
        """Receive value from channel"""
        if self.closed and not self.queue:
            raise Exception("Channel closed and empty")
        
        while not self.queue:
            if self.closed:
                raise Exception("Channel closed")
            time.sleep(0.01)
        
        value = self.queue.pop(0)
        print(f"[Channel] Received: {value}")
        return value
    
    def close(self):
        """Close channel"""
        self.closed = True
        print("[Channel] Closed")


# Global instances
_async_manager = KHXAsync()
_promises = {}
_channels = {}
_promise_counter = 0
_channel_counter = 0


def create_promise(executor_func):
    """Create promise"""
    global _promise_counter
    promise = KHXPromise(executor_func)
    promise_id = f"promise_{_promise_counter}"
    _promises[promise_id] = promise
    _promise_counter += 1
    return promise_id


def get_promise(promise_id):
    """Get promise"""
    return _promises.get(promise_id)


def run_async(func):
    """Run function asynchronously"""
    return _async_manager.run_async(func)


def async_sleep(seconds):
    """Async sleep"""
    _async_manager.sleep(seconds)


def parallel(*funcs):
    """Run functions in parallel"""
    return _async_manager.parallel(*funcs)


def create_channel(buffer_size=0):
    """Create channel"""
    global _channel_counter
    channel = KHXChannel(buffer_size)
    channel_id = f"channel_{_channel_counter}"
    _channels[channel_id] = channel
    _channel_counter += 1
    return channel_id


def get_channel(channel_id):
    """Get channel"""
    return _channels.get(channel_id)
