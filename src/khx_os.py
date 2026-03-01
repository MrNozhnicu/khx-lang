#!/usr/bin/env python3
"""
KHX OS Module - Operating System Creation Support
"""

import os
import sys
import time
import threading
from collections import deque


class KHXProcess:
    """Process representation in KHX OS"""
    
    def __init__(self, pid, name, code):
        self.pid = pid
        self.name = name
        self.code = code
        self.state = "ready"  # ready, running, waiting, terminated
        self.priority = 0
        self.memory = {}
        self.created_at = time.time()
    
    def __repr__(self):
        return f"Process(pid={self.pid}, name={self.name}, state={self.state})"


class KHXFileSystem:
    """Simple virtual file system"""
    
    def __init__(self):
        self.files = {}
        self.current_dir = "/"
        self.directories = {"/": []}
    
    def create_file(self, path, content=""):
        """Create a file"""
        self.files[path] = content
        dir_path = os.path.dirname(path) or "/"
        if dir_path not in self.directories:
            self.directories[dir_path] = []
        filename = os.path.basename(path)
        if filename not in self.directories[dir_path]:
            self.directories[dir_path].append(filename)
        return True
    
    def read_file(self, path):
        """Read a file"""
        return self.files.get(path, None)
    
    def write_file(self, path, content):
        """Write to a file"""
        if path in self.files:
            self.files[path] = content
            return True
        return False
    
    def delete_file(self, path):
        """Delete a file"""
        if path in self.files:
            del self.files[path]
            dir_path = os.path.dirname(path) or "/"
            filename = os.path.basename(path)
            if filename in self.directories.get(dir_path, []):
                self.directories[dir_path].remove(filename)
            return True
        return False
    
    def list_dir(self, path="/"):
        """List directory contents"""
        return self.directories.get(path, [])
    
    def create_dir(self, path):
        """Create a directory"""
        if path not in self.directories:
            self.directories[path] = []
            parent = os.path.dirname(path) or "/"
            dirname = os.path.basename(path)
            if parent in self.directories and dirname not in self.directories[parent]:
                self.directories[parent].append(dirname + "/")
            return True
        return False


class KHXScheduler:
    """Simple process scheduler"""
    
    def __init__(self):
        self.ready_queue = deque()
        self.running_process = None
        self.time_quantum = 100  # milliseconds
    
    def add_process(self, process):
        """Add process to ready queue"""
        process.state = "ready"
        self.ready_queue.append(process)
    
    def schedule(self):
        """Schedule next process"""
        if self.ready_queue:
            self.running_process = self.ready_queue.popleft()
            self.running_process.state = "running"
            return self.running_process
        return None
    
    def preempt(self):
        """Preempt current process"""
        if self.running_process:
            self.running_process.state = "ready"
            self.ready_queue.append(self.running_process)
            self.running_process = None


class KHXOperatingSystem:
    """Simple operating system kernel"""
    
    def __init__(self, name="KHX-OS"):
        self.name = name
        self.version = "1.0"
        self.processes = {}
        self.next_pid = 1
        self.scheduler = KHXScheduler()
        self.filesystem = KHXFileSystem()
        self.running = False
        self.boot_time = None
        self.system_calls = {}
        
        # Initialize system
        self._init_system()
    
    def _init_system(self):
        """Initialize system components"""
        # Create root directory
        self.filesystem.create_dir("/")
        self.filesystem.create_dir("/bin")
        self.filesystem.create_dir("/home")
        self.filesystem.create_dir("/tmp")
        
        # Register system calls
        self.register_syscall("print", self._syscall_print)
        self.register_syscall("read", self._syscall_read)
        self.register_syscall("write", self._syscall_write)
    
    def boot(self):
        """Boot the operating system"""
        if self.running:
            print(f"[{self.name}] System already running")
            return False
        
        print(f"[{self.name}] Booting...")
        print(f"[{self.name}] Version {self.version}")
        print(f"[{self.name}] Initializing file system...")
        print(f"[{self.name}] Starting scheduler...")
        
        self.running = True
        self.boot_time = time.time()
        
        print(f"[{self.name}] Boot complete!")
        print(f"[{self.name}] System ready.")
        return True
    
    def shutdown(self):
        """Shutdown the operating system"""
        if not self.running:
            print(f"[{self.name}] System not running")
            return False
        
        print(f"[{self.name}] Shutting down...")
        print(f"[{self.name}] Terminating processes...")
        
        for pid, process in self.processes.items():
            process.state = "terminated"
        
        self.running = False
        uptime = time.time() - self.boot_time
        print(f"[{self.name}] Uptime: {uptime:.2f} seconds")
        print(f"[{self.name}] Shutdown complete.")
        return True
    
    def create_process(self, name, code):
        """Create a new process"""
        pid = self.next_pid
        self.next_pid += 1
        
        process = KHXProcess(pid, name, code)
        self.processes[pid] = process
        self.scheduler.add_process(process)
        
        print(f"[{self.name}] Process created: PID={pid} NAME={name}")
        return pid
    
    def kill_process(self, pid):
        """Kill a process"""
        if pid in self.processes:
            process = self.processes[pid]
            process.state = "terminated"
            print(f"[{self.name}] Process terminated: PID={pid}")
            return True
        return False
    
    def list_processes(self):
        """List all processes"""
        return list(self.processes.values())
    
    def register_syscall(self, name, handler):
        """Register a system call"""
        self.system_calls[name] = handler
    
    def syscall(self, name, *args):
        """Execute a system call"""
        if name in self.system_calls:
            return self.system_calls[name](*args)
        print(f"[{self.name}] Unknown system call: {name}")
        return None
    
    def _syscall_print(self, message):
        """System call: print"""
        print(f"[PROCESS] {message}")
        return True
    
    def _syscall_read(self, path):
        """System call: read file"""
        return self.filesystem.read_file(path)
    
    def _syscall_write(self, path, content):
        """System call: write file"""
        return self.filesystem.write_file(path, content)
    
    def get_info(self):
        """Get system information"""
        info = {
            "name": self.name,
            "version": self.version,
            "running": self.running,
            "processes": len(self.processes),
            "uptime": time.time() - self.boot_time if self.boot_time else 0
        }
        return info


# Global OS registry
_operating_systems = {}
_os_counter = 0


def create_os(name="KHX-OS"):
    """Create a new operating system"""
    global _os_counter
    os_instance = KHXOperatingSystem(name)
    os_id = f"os_{_os_counter}"
    _operating_systems[os_id] = os_instance
    _os_counter += 1
    return os_id


def get_os(os_id):
    """Get OS by ID"""
    return _operating_systems.get(os_id)


def boot_os(os_id):
    """Boot an operating system"""
    os_instance = _operating_systems.get(os_id)
    if os_instance:
        return os_instance.boot()
    return False


def shutdown_os(os_id):
    """Shutdown an operating system"""
    os_instance = _operating_systems.get(os_id)
    if os_instance:
        return os_instance.shutdown()
    return False


def create_process(os_id, name, code):
    """Create a process in OS"""
    os_instance = _operating_systems.get(os_id)
    if os_instance:
        return os_instance.create_process(name, code)
    return None


def list_processes(os_id):
    """List processes in OS"""
    os_instance = _operating_systems.get(os_id)
    if os_instance:
        return os_instance.list_processes()
    return []
