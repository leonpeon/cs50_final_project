from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout, QGridLayout, QScrollArea, QMessageBox)
from PySide6.QtCore import QCalendar, Qt, QSize
from PySide6.QtGui import QFont, QIcon

class ViewPage(QWidget):
    def __init__(self, db):
        super().__init__()
        self.title_font = QFont()
        self.title_font.setPointSize(40)
        self.db = db

        layout = QVBoxLayout(self)

        self.title = QLabel("Your Ideas Archive")
        self.title.setFont(self.title_font)
        layout.addWidget(self.title)

        # Creates ability to scroll through ideas
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.ideas_widget = QWidget()
        self.ideas_layout = QVBoxLayout(self.ideas_widget)

        # Loops through ideas
        self.load_page()

        scroll_area.setWidget(self.ideas_widget)
        layout.addWidget(scroll_area)

    def confirm_delete(self, id):
        confirmation = QMessageBox.question(self, "Delete Idea?", 
                                            "Are you sure you want to delete this idea")
        if confirmation == QMessageBox.StandardButton.Yes:
            self.db.delete_idea(id)
            self.refresh_page()

    def favourites_clicked(self, button):
        if self.db.update_favourites(button.property("button_id")) == 1:
            button.setIcon(QIcon("./icons/filled_favourite.png"))
        else:
            button.setIcon(QIcon("./icons/favourite.png"))

    def refresh_page(self):
        while self.ideas_layout.count():
            item = self.ideas_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.load_page()

    def load_page(self):
        for idea, date, tag, idea_id in self.db.view_ideas():
            one_idea = QWidget()
            one_idea_layout = QGridLayout(one_idea)
            date_label = QLabel(date)
            idea_label = QLabel(idea)

            favourite_button = QPushButton()
            if self.db.return_favourite_status(idea_id) == 1:
                favourite_button.setIcon(QIcon("./icons/filled_favourite.png"))
            else:
                favourite_button.setIcon(QIcon("./icons/favourite.png"))
            favourite_button.setIconSize(QSize(30, 30))
            favourite_button.setProperty("button_id", idea_id)
            favourite_button.setStyleSheet("""
                QPushButton {
                border: none;
                background: transparent;
                }
                QPushButton:hover {
                    background: transparent;
                }
            """)
            favourite_button.clicked.connect(lambda checked=False, 
                                                button=favourite_button: 
                                                self.favourites_clicked(button))

            completed_button = QPushButton("Mark Done")
            delete_button = QPushButton("Delete")

            one_idea.setProperty("tag", tag)

            delete_button.clicked.connect(lambda checked=False, 
                                            id=idea_id: 
                                            self.confirm_delete(id))

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
            self.ideas_layout.addWidget(one_idea)

        


