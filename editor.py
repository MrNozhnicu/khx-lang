#!/usr/bin/env python3
"""
KHX Code Editor - Visual Studio Code style editor
"""

import sys
import os
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QFileDialog, 
                             QAction, QToolBar, QSplitter, QTreeView, QVBoxLayout,
                             QWidget, QStatusBar, QMessageBox, QTabWidget, QLabel,
                             QDockWidget, QListWidget, QLineEdit, QHBoxLayout, QPushButton)
from PyQt5.QtGui import (QFont, QSyntaxHighlighter, QTextCharFormat, QColor, 
                         QPalette, QIcon, QKeySequence, QTextCursor, QFontMetrics)
from PyQt5.QtCore import Qt, QRegExp, QFileSystemWatcher, QDir, QTimer
from PyQt5.Qsci import QsciScintilla, QsciLexerCustom


class KHXLexer(QsciLexerCustom):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Define styles
        self.setDefaultColor(QColor("#D4D4D4"))
        self.setDefaultPaper(QColor("#1E1E1E"))
        self.setDefaultFont(QFont("Consolas", 11))
        
        # Style definitions
        self.styles = {
            'default': 0,
            'keyword': 1,
            'string': 2,
            'number': 3,
            'comment': 4,
            'function': 5,
            'operator': 6,
            'type': 7,
        }
        
        # Keywords
        self.keywords = [
            'let', 'func', 'class', 'if', 'else', 'while', 'for',
            'return', 'match', 'print', 'true', 'false', 'null',
            'this', 'and', 'or', 'not', 'async', 'await',
            'window', 'button', 'label', 'input', 'show'
        ]
        
        # Types
        self.types = ['int', 'float', 'string', 'bool', 'void']
        
        # GUI Functions
        self.gui_functions = [
            'create_window', 'add_label', 'add_button', 'add_input',
            'add_textarea', 'add_checkbox', 'add_list', 'add_dropdown',
            'add_slider', 'add_progressbar', 'get_text', 'set_text',
            'show_message', 'show_error', 'show_warning', 'show_window',
            'run_app', 'get_widget'
        ]
        
    def language(self):
        return "KHX"
    
    def description(self, style):
        descriptions = {
            0: "Default",
            1: "Keyword",
            2: "String",
            3: "Number",
            4: "Comment",
            5: "Function",
            6: "Operator",
            7: "Type",
        }
        return descriptions.get(style, "")
    
    def styleText(self, start, end):
        editor = self.editor()
        if editor is None:
            return
        
        text = editor.text()[start:end]
        
        self.startStyling(start)
        
        i = 0
        while i < len(text):
            # Comments
            if i < len(text) - 1 and text[i:i+2] == '//':
                j = i
                while j < len(text) and text[j] != '\n':
                    j += 1
                self.setStyling(j - i, self.styles['comment'])
                i = j
                continue
            
            # Strings
            if text[i] in '"\'':
                quote = text[i]
                j = i + 1
                while j < len(text) and text[j] != quote:
                    if text[j] == '\\':
                        j += 2
                    else:
                        j += 1
                if j < len(text):
                    j += 1
                self.setStyling(j - i, self.styles['string'])
                i = j
                continue
            
            # Numbers
            if text[i].isdigit():
                j = i
                while j < len(text) and (text[j].isdigit() or text[j] == '.'):
                    j += 1
                self.setStyling(j - i, self.styles['number'])
                i = j
                continue
            
            # Keywords, types, identifiers
            if text[i].isalpha() or text[i] == '_':
                j = i
                while j < len(text) and (text[j].isalnum() or text[j] == '_'):
                    j += 1
                word = text[i:j]
                
                if word in self.keywords:
                    self.setStyling(j - i, self.styles['keyword'])
                elif word in self.types:
                    self.setStyling(j - i, self.styles['type'])
                elif word in self.gui_functions:
                    self.setStyling(j - i, self.styles['function'])
                else:
                    # Check if it's a function call
                    k = j
                    while k < len(text) and text[k] in ' \t':
                        k += 1
                    if k < len(text) and text[k] == '(':
                        self.setStyling(j - i, self.styles['function'])
                    else:
                        self.setStyling(j - i, self.styles['default'])
                i = j
                continue
            
            # Operators
            if text[i] in '+-*/=<>!&|':
                self.setStyling(1, self.styles['operator'])
                i += 1
                continue
            
            # Default
            self.setStyling(1, self.styles['default'])
            i += 1


class CodeEditor(QsciScintilla):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Font
        font = QFont("Consolas", 11)
        self.setFont(font)
        
        # Margins - Dracula theme
        fontmetrics = QFontMetrics(font)
        self.setMarginWidth(0, fontmetrics.width("00000") + 6)
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#282A36"))
        self.setMarginsForegroundColor(QColor("#6272A4"))
        
        # Brace matching
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)
        self.setMatchedBraceBackgroundColor(QColor("#44475A"))
        self.setMatchedBraceForegroundColor(QColor("#FF79C6"))
        
        # Current line - Dracula theme
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#44475A"))
        self.setCaretForegroundColor(QColor("#F8F8F2"))
        
        # Indentation
        self.setIndentationsUseTabs(False)
        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setAutoIndent(True)
        
        # Colors - Dracula theme
        self.setPaper(QColor("#282A36"))
        self.setColor(QColor("#F8F8F2"))
        
        # Lexer
        lexer = KHXLexer(self)
        
        # Set Dracula lexer colors
        lexer.setColor(QColor("#F8F8F2"), 0)  # default
        lexer.setColor(QColor("#FF79C6"), 1)  # keyword - pink
        lexer.setColor(QColor("#F1FA8C"), 2)  # string - yellow
        lexer.setColor(QColor("#BD93F9"), 3)  # number - purple
        lexer.setColor(QColor("#6272A4"), 4)  # comment - gray
        lexer.setColor(QColor("#50FA7B"), 5)  # function - green
        lexer.setColor(QColor("#F8F8F2"), 6)  # operator - white
        lexer.setColor(QColor("#8BE9FD"), 7)  # type - cyan
        
        self.setLexer(lexer)
        
        # Autocomplete
        self.setAutoCompletionSource(QsciScintilla.AcsAll)
        self.setAutoCompletionThreshold(2)
        self.setAutoCompletionCaseSensitivity(False)
        
        # Selection - Dracula theme
        self.setSelectionBackgroundColor(QColor("#44475A"))
        self.setSelectionForegroundColor(QColor("#F8F8F2"))


class OutputPanel(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setFont(QFont("Consolas", 10))
        
        # Dracula theme for output panel
        palette = self.palette()
        palette.setColor(QPalette.Base, QColor("#282A36"))
        palette.setColor(QPalette.Text, QColor("#F8F8F2"))
        self.setPalette(palette)


class FileExplorer(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setHeaderHidden(True)
        
        # Dracula theme for file explorer
        self.setStyleSheet("""
            QTreeView {
                background-color: #21222C;
                color: #F8F8F2;
                border: none;
            }
            QTreeView::item:hover {
                background-color: #44475A;
            }
            QTreeView::item:selected {
                background-color: #44475A;
                color: #F8F8F2;
            }
        """)


class KHXEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("KHX Code Editor - Dracula Theme")
        self.setGeometry(100, 100, 1400, 900)
        
        # Apply Dracula theme
        self.setStyleSheet("""
            QMainWindow {
                background-color: #282A36;
            }
            QMenuBar {
                background-color: #343746;
                color: #F8F8F2;
                border-bottom: 1px solid #191A21;
            }
            QMenuBar::item:selected {
                background-color: #44475A;
            }
            QMenu {
                background-color: #282A36;
                color: #F8F8F2;
                border: 1px solid #44475A;
            }
            QMenu::item:selected {
                background-color: #44475A;
            }
            QToolBar {
                background-color: #343746;
                border: none;
                spacing: 3px;
                padding: 5px;
            }
            QToolButton {
                background-color: transparent;
                color: #F8F8F2;
                border: none;
                padding: 5px;
            }
            QToolButton:hover {
                background-color: #44475A;
            }
            QStatusBar {
                background-color: #BD93F9;
                color: #282A36;
                font-weight: bold;
            }
            QTabWidget::pane {
                border: none;
                background-color: #282A36;
            }
            QTabBar::tab {
                background-color: #21222C;
                color: #6272A4;
                padding: 8px 20px;
                border: none;
                border-top: 2px solid transparent;
            }
            QTabBar::tab:selected {
                background-color: #282A36;
                color: #F8F8F2;
                border-top: 2px solid #FF79C6;
            }
            QTabBar::tab:hover {
                background-color: #343746;
                color: #F8F8F2;
            }
            QDockWidget {
                color: #F8F8F2;
                titlebar-close-icon: url(close.png);
                titlebar-normal-icon: url(float.png);
            }
            QDockWidget::title {
                background-color: #343746;
                padding: 5px;
            }
        """)
        
        # Create menu bar
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        new_action = QAction("New", self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction("Open", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("Save", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("Save As...", self)
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        
        undo_action = QAction("Undo", self)
        undo_action.setShortcut(QKeySequence.Undo)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("Redo", self)
        redo_action.setShortcut(QKeySequence.Redo)
        edit_menu.addAction(redo_action)
        
        edit_menu.addSeparator()
        
        cut_action = QAction("Cut", self)
        cut_action.setShortcut(QKeySequence.Cut)
        edit_menu.addAction(cut_action)
        
        copy_action = QAction("Copy", self)
        copy_action.setShortcut(QKeySequence.Copy)
        edit_menu.addAction(copy_action)
        
        paste_action = QAction("Paste", self)
        paste_action.setShortcut(QKeySequence.Paste)
        edit_menu.addAction(paste_action)
        
        # Run menu
        run_menu = menubar.addMenu("Run")
        
        run_action = QAction("Run Program", self)
        run_action.setShortcut("F5")
        run_action.triggered.connect(self.run_program)
        run_menu.addAction(run_action)
        
        run_gui_action = QAction("Run GUI Program", self)
        run_gui_action.setShortcut("F6")
        run_gui_action.triggered.connect(self.run_gui_program)
        run_menu.addAction(run_gui_action)
        
        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addSeparator()
        
        run_btn = QAction("▶ Run", self)
        run_btn.triggered.connect(self.run_program)
        toolbar.addAction(run_btn)
        
        run_gui_btn = QAction("▶ Run GUI", self)
        run_gui_btn.triggered.connect(self.run_gui_program)
        toolbar.addAction(run_gui_btn)
        
        # Central widget with tabs
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        
        # Create first editor
        self.editor = CodeEditor()
        self.tabs.addTab(self.editor, "Untitled")
        
        # File explorer dock
        self.file_dock = QDockWidget("Explorer", self)
        self.file_explorer = FileExplorer()
        self.file_dock.setWidget(self.file_explorer)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.file_dock)
        
        # Output panel dock
        self.output_dock = QDockWidget("Output", self)
        self.output_panel = OutputPanel()
        self.output_dock.setWidget(self.output_panel)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.output_dock)
        
        # Main layout
        self.setCentralWidget(self.tabs)
        
        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        
        # Line/Column indicator - Dracula theme
        self.line_col_label = QLabel("Ln 1, Col 1")
        self.line_col_label.setStyleSheet("color: #282A36; padding: 0 10px; font-weight: bold;")
        self.status_bar.addPermanentWidget(self.line_col_label)
        
        # Language indicator - Dracula theme
        self.lang_label = QLabel("KHX")
        self.lang_label.setStyleSheet("color: #282A36; padding: 0 10px; font-weight: bold;")
        self.status_bar.addPermanentWidget(self.lang_label)
        
        # Connect cursor position change
        self.editor.cursorPositionChanged.connect(self.update_cursor_position)
        
    def get_current_editor(self):
        return self.tabs.currentWidget()
    
    def new_file(self):
        editor = CodeEditor()
        editor.cursorPositionChanged.connect(self.update_cursor_position)
        index = self.tabs.addTab(editor, "Untitled")
        self.tabs.setCurrentIndex(index)
        self.status_bar.showMessage("New file created")
    
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "KHX Files (*.khx);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                editor = CodeEditor()
                editor.setText(content)
                editor.cursorPositionChanged.connect(self.update_cursor_position)
                
                tab_name = os.path.basename(filename)
                index = self.tabs.addTab(editor, tab_name)
                self.tabs.setCurrentIndex(index)
                
                self.current_file = filename
                self.status_bar.showMessage(f"Opened: {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {str(e)}")
    
    def save_file(self):
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_file_as()
    
    def save_file_as(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "KHX Files (*.khx);;All Files (*)"
        )
        
        if filename:
            if not filename.endswith('.khx'):
                filename += '.khx'
            self.save_to_file(filename)
            self.current_file = filename
            
            tab_name = os.path.basename(filename)
            self.tabs.setTabText(self.tabs.currentIndex(), tab_name)
    
    def save_to_file(self, filename):
        try:
            editor = self.get_current_editor()
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(editor.text())
            self.status_bar.showMessage(f"Saved: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")
    
    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.get_current_editor().clear()
    
    def run_program(self):
        # Save current file first
        if not self.current_file:
            self.save_file_as()
            if not self.current_file:
                return
        else:
            self.save_file()
        
        self.output_panel.clear()
        self.output_panel.append("=== Running KHX Program ===\n")
        
        try:
            # Ищем интерпретатор
            if os.path.exists('src/khx_v5.py'):
                interpreter = 'src/khx_v5.py'
            elif os.path.exists('khx_v5.py'):
                interpreter = 'khx_v5.py'
            else:
                interpreter = 'khx.py'
            
            # Run the KHX interpreter
            result = subprocess.run(
                [sys.executable, interpreter, self.current_file],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.stdout:
                self.output_panel.append(result.stdout)
            
            if result.stderr:
                self.output_panel.append(f"\n=== Errors ===\n{result.stderr}")
                self.output_panel.setTextColor(QColor("#F48771"))
            
            if result.returncode == 0:
                self.output_panel.append("\n=== Program finished successfully ===")
                self.status_bar.showMessage("Program executed successfully")
            else:
                self.output_panel.append(f"\n=== Program exited with code {result.returncode} ===")
                self.status_bar.showMessage(f"Program failed with code {result.returncode}")
                
        except subprocess.TimeoutExpired:
            self.output_panel.append("\n=== Program timeout (10s) ===")
            self.status_bar.showMessage("Program timeout")
        except Exception as e:
            self.output_panel.append(f"\n=== Error: {str(e)} ===")
            self.status_bar.showMessage(f"Error: {str(e)}")
    
    def run_gui_program(self):
        # Save current file first
        if not self.current_file:
            self.save_file_as()
            if not self.current_file:
                return
        else:
            self.save_file()
        
        self.output_panel.clear()
        self.output_panel.append("=== Running KHX GUI Program ===\n")
        
        try:
            # Run the KHX GUI interpreter
            result = subprocess.run(
                [sys.executable, 'khx_v2.py', self.current_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.stdout:
                self.output_panel.append(result.stdout)
            
            if result.stderr:
                self.output_panel.append(f"\n=== Errors ===\n{result.stderr}")
                self.output_panel.setTextColor(QColor("#F48771"))
            
            if result.returncode == 0:
                self.output_panel.append("\n=== GUI Program finished ===")
                self.status_bar.showMessage("GUI Program executed")
            else:
                self.output_panel.append(f"\n=== Program exited with code {result.returncode} ===")
                self.status_bar.showMessage(f"Program failed with code {result.returncode}")
                
        except subprocess.TimeoutExpired:
            self.output_panel.append("\n=== Program timeout (30s) ===")
            self.status_bar.showMessage("Program timeout")
        except Exception as e:
            self.output_panel.append(f"\n=== Error: {str(e)} ===")
            self.status_bar.showMessage(f"Error: {str(e)}")
    
    def update_cursor_position(self):
        editor = self.get_current_editor()
        line, col = editor.getCursorPosition()
        self.line_col_label.setText(f"Ln {line + 1}, Col {col + 1}")


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    editor = KHXEditor()
    editor.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
