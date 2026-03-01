#!/usr/bin/env python3
"""
KHX GUI Module - Support for creating GUI applications
"""

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, 
                             QPushButton, QLineEdit, QTextEdit, QVBoxLayout,
                             QHBoxLayout, QMessageBox, QListWidget, QComboBox,
                             QCheckBox, QRadioButton, QSlider, QProgressBar,
                             QMenuBar, QMenu, QAction, QToolBar, QStatusBar,
                             QTabWidget, QGroupBox, QSpinBox, QDialog)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QIcon, QColor, QPalette


class KHXWindow:
    """Base window class for KHX GUI applications"""
    
    def __init__(self, title="KHX Window", width=800, height=600):
        self.app = QApplication.instance()
        if self.app is None:
            self.app = QApplication(sys.argv)
        
        self.window = QMainWindow()
        self.window.setWindowTitle(title)
        self.window.setGeometry(100, 100, width, height)
        
        # Central widget
        self.central_widget = QWidget()
        self.window.setCentralWidget(self.central_widget)
        
        # Main layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Widgets storage
        self.widgets = {}
        self.widget_counter = 0
        
    def add_label(self, text, font_size=12):
        """Add a label to the window"""
        label = QLabel(text)
        label.setFont(QFont("Arial", font_size))
        self.layout.addWidget(label)
        
        widget_id = f"label_{self.widget_counter}"
        self.widgets[widget_id] = label
        self.widget_counter += 1
        return widget_id
    
    def add_button(self, text, callback=None):
        """Add a button to the window"""
        button = QPushButton(text)
        if callback:
            button.clicked.connect(callback)
        self.layout.addWidget(button)
        
        widget_id = f"button_{self.widget_counter}"
        self.widgets[widget_id] = button
        self.widget_counter += 1
        return widget_id
    
    def add_input(self, placeholder=""):
        """Add a text input field"""
        input_field = QLineEdit()
        input_field.setPlaceholderText(placeholder)
        self.layout.addWidget(input_field)
        
        widget_id = f"input_{self.widget_counter}"
        self.widgets[widget_id] = input_field
        self.widget_counter += 1
        return widget_id
    
    def add_textarea(self, placeholder=""):
        """Add a multi-line text area"""
        textarea = QTextEdit()
        textarea.setPlaceholderText(placeholder)
        self.layout.addWidget(textarea)
        
        widget_id = f"textarea_{self.widget_counter}"
        self.widgets[widget_id] = textarea
        self.widget_counter += 1
        return widget_id
    
    def add_checkbox(self, text):
        """Add a checkbox"""
        checkbox = QCheckBox(text)
        self.layout.addWidget(checkbox)
        
        widget_id = f"checkbox_{self.widget_counter}"
        self.widgets[widget_id] = checkbox
        self.widget_counter += 1
        return widget_id
    
    def add_list(self, items):
        """Add a list widget"""
        list_widget = QListWidget()
        for item in items:
            list_widget.addItem(item)
        self.layout.addWidget(list_widget)
        
        widget_id = f"list_{self.widget_counter}"
        self.widgets[widget_id] = list_widget
        self.widget_counter += 1
        return widget_id
    
    def add_dropdown(self, items):
        """Add a dropdown/combobox"""
        dropdown = QComboBox()
        dropdown.addItems(items)
        self.layout.addWidget(dropdown)
        
        widget_id = f"dropdown_{self.widget_counter}"
        self.widgets[widget_id] = dropdown
        self.widget_counter += 1
        return widget_id
    
    def add_slider(self, min_val=0, max_val=100):
        """Add a slider"""
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        self.layout.addWidget(slider)
        
        widget_id = f"slider_{self.widget_counter}"
        self.widgets[widget_id] = slider
        self.widget_counter += 1
        return widget_id
    
    def add_progressbar(self):
        """Add a progress bar"""
        progressbar = QProgressBar()
        self.layout.addWidget(progressbar)
        
        widget_id = f"progressbar_{self.widget_counter}"
        self.widgets[widget_id] = progressbar
        self.widget_counter += 1
        return widget_id
    
    def get_widget(self, widget_id):
        """Get widget by ID"""
        return self.widgets.get(widget_id)
    
    def get_text(self, widget_id):
        """Get text from input or textarea"""
        widget = self.widgets.get(widget_id)
        if isinstance(widget, QLineEdit):
            return widget.text()
        elif isinstance(widget, QTextEdit):
            return widget.toPlainText()
        return ""
    
    def set_text(self, widget_id, text):
        """Set text to label, input, or textarea"""
        widget = self.widgets.get(widget_id)
        if isinstance(widget, QLabel):
            widget.setText(text)
        elif isinstance(widget, QLineEdit):
            widget.setText(text)
        elif isinstance(widget, QTextEdit):
            widget.setPlainText(text)
    
    def show_message(self, title, message):
        """Show a message box"""
        QMessageBox.information(self.window, title, message)
    
    def show_error(self, title, message):
        """Show an error message box"""
        QMessageBox.critical(self.window, title, message)
    
    def show_warning(self, title, message):
        """Show a warning message box"""
        QMessageBox.warning(self.window, title, message)
    
    def set_theme_dark(self):
        """Apply dark theme"""
        self.window.setStyleSheet("""
            QMainWindow, QWidget {
                background-color: #1E1E1E;
                color: #CCCCCC;
            }
            QPushButton {
                background-color: #0E639C;
                color: white;
                border: none;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1177BB;
            }
            QLineEdit, QTextEdit {
                background-color: #2D2D2D;
                color: #CCCCCC;
                border: 1px solid #3E3E3E;
                padding: 5px;
            }
            QLabel {
                color: #CCCCCC;
            }
        """)
    
    def set_theme_light(self):
        """Apply light theme"""
        self.window.setStyleSheet("")
    
    def show(self):
        """Show the window"""
        self.window.show()
    
    def run(self):
        """Run the application event loop"""
        self.window.show()
        sys.exit(self.app.exec_())


# Global window registry
_windows = {}
_window_counter = 0


def create_window(title="KHX Window", width=800, height=600):
    """Create a new window and return its ID"""
    global _window_counter
    window = KHXWindow(title, width, height)
    window_id = f"window_{_window_counter}"
    _windows[window_id] = window
    _window_counter += 1
    return window_id


def get_window(window_id):
    """Get window by ID"""
    return _windows.get(window_id)


def show_window(window_id):
    """Show a window"""
    window = _windows.get(window_id)
    if window:
        window.show()


def run_app(window_id):
    """Run the application with the specified window"""
    window = _windows.get(window_id)
    if window:
        window.run()
