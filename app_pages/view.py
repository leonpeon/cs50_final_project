from PySide6.QtWidgets import (QLabel, QPushButton, QWidget, 
                               QVBoxLayout, QGridLayout,
                               QScrollArea, QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon


# Handles the view page
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


    # Loads the uncompleted ideas
    def load_page(self):
        for idea, date, tag, idea_id, completed in self.db.view_ideas():
            if not completed:
                one_idea = QWidget()
                one_idea.setFixedSize(QSize(700, 170))
                one_idea_layout = QGridLayout(one_idea)
                date_label = QLabel(date)
                idea_label = QLabel(idea)

                # Favourite button functionality
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

                # Delete button functionality
                delete_button = QPushButton("Delete")
                delete_button.clicked.connect(lambda checked=False, 
                                                id=idea_id: 
                                                self.confirm_delete(id))

                # Completed button functionality
                completed_button = QPushButton("Mark Done")
                completed_button.clicked.connect(lambda checked=False,
                                                    id=idea_id,
                                                    widget=one_idea:
                                                    self.confirm_complete(id, widget))

                # Allows user to search by tags
                one_idea.setProperty("tag", tag)

                # Adds styling to the idea widget
                one_idea.setObjectName("ideaWidget")
                one_idea.setStyleSheet("""
                #ideaWidget {
                    border: 1px solid gray;
                    border-radius: 5px;
                }
                """)

                # Add each element to the widget
                one_idea_layout.addWidget(date_label, 0, 0, 1, 5, alignment=Qt.AlignCenter)
                one_idea_layout.addWidget(idea_label, 1, 0, 3, 4)
                one_idea_layout.addWidget(favourite_button, 1, 5)
                one_idea_layout.addWidget(completed_button, 2, 5)
                one_idea_layout.addWidget(delete_button, 3, 5)
                self.ideas_layout.addWidget(one_idea)


    # Shows a messagebox asking the user if they are sure they want to delete an idea
    def confirm_delete(self, id):
        confirmation = QMessageBox.question(self, "Delete Idea?", 
                                            "Are you sure you want to delete this idea?")
        if confirmation == QMessageBox.StandardButton.Yes:
            self.db.delete_idea(id)
            self.refresh_page()


    # Asks the user if they are sure they want to mark an idea as complete
    def confirm_complete(self, id, widget):
        confirmation = QMessageBox.question(self, "Mark Complete?",
                                            "Do you want to mark this idea as complete?")
        if confirmation == QMessageBox.StandardButton.Yes:
            self.db.add_completed(id)
            widget.deleteLater()
            self.refresh_page()
            self.completedpage.refresh_completed_page()


    # Updates the favourites icon when clicked, and updates the database
    def favourites_clicked(self, button):
        if self.db.update_favourites(button.property("button_id")) == 1:
            button.setIcon(QIcon("./icons/filled_favourite.png"))
        else:
            button.setIcon(QIcon("./icons/favourite.png"))


    # Refreshes page upon each deletion or after idea is marked complete
    def refresh_page(self):
        while self.ideas_layout.count():
            item = self.ideas_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.load_page()

        


