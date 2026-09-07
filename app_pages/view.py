from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout, QGridLayout, QScrollArea)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont

class ViewPage(QWidget):
    def __init__(self, db):
        super().__init__()
        self.title_font = QFont()
        self.title_font.setPointSize(40)

        layout = QVBoxLayout(self)

        self.title = QLabel("Your Ideas Archive")
        self.title.setFont(self.title_font)
        layout.addWidget(self.title)

        # Creates ability to scroll through ideas
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.ideas_widget = QWidget()
        ideas_layout = QVBoxLayout(self.ideas_widget)

        # Loops through ideas
        for idea, date, tag, favourite, completed in db.view_ideas():
            one_idea = QWidget()
            one_idea_layout = QGridLayout(one_idea)
            date_label = QLabel(date)
            idea_label = QLabel(idea)
            favourite_button = QPushButton(str(favourite))
            completed_button = QPushButton(str(completed))
            delete_button = QPushButton("ADD DELETE")

            one_idea.setObjectName("ideaWidget")
            one_idea.setStyleSheet("""
            #ideaWidget {
                border: 1px solid gray;
                border-radius: 5px;
            }
            """)

            one_idea_layout.addWidget(date_label, 0, 0, 1, 5, alignment=Qt.AlignCenter)
            one_idea_layout.addWidget(idea_label, 1, 0, 3, 4)
            one_idea_layout.addWidget(favourite_button, 1, 5)
            one_idea_layout.addWidget(completed_button, 2, 5)
            one_idea_layout.addWidget(delete_button, 3, 5)
            ideas_layout.addWidget(one_idea)


        scroll_area.setWidget(self.ideas_widget)
        layout.addWidget(scroll_area)
