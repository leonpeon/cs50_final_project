from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont
import sqlite3

class ViewPage(QWidget):
    def __init__(self, db):
        super().__init__()
        self.title_font = QFont()
        self.title_font.setPointSize(40)

        layout = QVBoxLayout(self)

        view_page_title = QLabel("Your Ideas Archive")
        view_page_title.setFont(self.title_font)

        layout.addWidget(view_page_title)