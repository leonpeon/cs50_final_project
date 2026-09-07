from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont

class CompletedPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.title_font = QFont()
        self.title_font.setPointSize(40)

        self.title = QLabel("Completed Ideas")
        self.title.setFont(self.title_font)

        layout.addWidget(self.title)