from PySide6.QtWidgets import (QComboBox, QLabel, QTextEdit, 
                               QPushButton, QWidget, 
                               QVBoxLayout)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont
import sqlite3

# HOME PAGE
# TODO: Update GUI, save idea to a SQL database

class HomePage(QWidget):
    def __init__(self, db):
        super().__init__()
        self.title_font = QFont()
        self.title_font.setPointSize(40)

        layout = QVBoxLayout(self)

        self.home_title = QLabel("Welcome to the factory")
        self.home_title.setFont(self.title_font)

        self.idea_text_box = QTextEdit(placeholderText="Write your idea")
        self.idea_text_box.setFixedSize(750, 300)

        self.tags_combobox = QComboBox(placeholderText="Add tag", duplicatesEnabled=False)
        self.tags_combobox.addItems([
            "No tag",
            "Software",
            "Games",
            "Stories",
            "Misc"
        ])

        self.submit_button = QPushButton("Save")
        self.submit_button.clicked.connect(lambda: db.save_idea(self.idea_text_box, self.tags_combobox))

        layout.addWidget(self.home_title, alignment=Qt.AlignCenter)
        layout.addWidget(self.idea_text_box, alignment=Qt.AlignCenter)
        layout.addWidget(self.tags_combobox, alignment=Qt.AlignCenter)
        layout.addWidget(self.submit_button)