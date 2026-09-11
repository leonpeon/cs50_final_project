from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTextEdit, QGridLayout, 
                               QHBoxLayout, QScrollArea, QPushButton, QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon


class ClickableWidget(QWidget):
    def __init__(self, page, db):
        super().__init__()
        self.db = db

        # The 'page' argument checks if it is the view (True) or completed (False) page.
        self.is_view_page = page

        # Page layout
        self.frame_layout = QVBoxLayout(self)

        # Sets the title font
        self.title_font = QFont()
        self.title_font.setPointSize(40)

        # Database
        self.db = db

        # Sets size of the frame, and allows widget inside to have their own styling
        self.setFixedSize(QSize(1150, 710))

        # Establishes title for each page
        if self.is_view_page:
            self.title = QLabel("Your Ideas Archive")
        else:
            self.title = QLabel("Completed Ideas")

        self.title.setFont(self.title_font)
        self.frame_layout.addWidget(self.title)

        # Widget for srollable ideas and the side preview
        self.idea_frame = QWidget()
        self.idea_frame_layout = QHBoxLayout(self.idea_frame)

        # Creates ability to scroll through ideas
        scroll_area = QScrollArea()

        # LEFT: Creates widget for scrollable ideas
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)

        # RIGHT: Creates a widget which shows the idea when clicked
        self.preview_widget = QWidget()
        self.preview_widget.setFixedSize(QSize(400, 500))
        self.preview_layout = QVBoxLayout(self.preview_widget)
        self.preview_widget.setObjectName("preview_widget")
        self.preview_widget.setStyleSheet("""
            #preview_widget {
                border: 2px solid black;
                border-radius: 10px;
        }
        """)

        # Sets up the preview widget
        self.date = "OO-OO-OOOO"
        self.clicked_idea = "Click an idea for a preview"

        self.date_preview = QLabel(self.date)

        self.idea_preview = QTextEdit()
        self.idea_preview.setReadOnly(True)
        self.idea_preview.setPlainText(self.clicked_idea)
        self.idea_preview.setStyleSheet("""
            QTextEdit {
                background-color: transparent;
                border: none;
            }
        """)

        self.preview_layout.addWidget(self.date_preview, alignment=Qt.AlignCenter)
        self.preview_layout.addWidget(self.idea_preview)

        self.load_page()

        # Add elements to the ideas widget
        scroll_area.setWidget(self.scroll_widget)
        scroll_area.setFixedSize(QSize(700, 500))

        self.idea_frame_layout.addWidget(scroll_area)
        self.idea_frame_layout.addWidget(self.preview_widget)

        # Adds idea widget to the main widget
        self.frame_layout.addWidget(self.idea_frame)


    def load_page(self):
        for idea, date, tag, idea_id, completed in self.db.view_ideas():

            # If COMPLETED page
            if not self.is_view_page:
                if completed:
                    self.one_idea = IdeaCard(idea_id, self)
                    self.one_idea_layout = QVBoxLayout(self.one_idea)
                    self.clickable_idea(idea, date, idea_id)
                    self.scroll_layout.addWidget(self.one_idea)

            # If VIEW page
            else:
                if not completed:
                    self.one_idea = IdeaCard(idea_id, self)
                    self.one_idea_layout = QGridLayout(self.one_idea)
                    self.clickable_idea(idea, date, idea_id)
                    self.scroll_layout.addWidget(self.one_idea)
            

    def clickable_idea(self, idea, date, id):
        # Label for date
        date_label = QLabel(date)
           
        # Text frame for idea
        idea_label = QTextEdit()
        idea_label.setReadOnly(True)
        idea_label.setPlainText(idea)
        idea_label.setFixedSize(540, 100)
        idea_label.setStyleSheet("""
            QTextEdit {
                background-color: transparent;
                border: none;
            }
        """)
        # Gets rid of the scroll bar
        idea_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # Stops text box from being clickable
        idea_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        # Sets the id for each idea widget
        self.id = id

        if not self.is_view_page:
            self.one_idea_layout.addWidget(date_label, alignment=Qt.AlignCenter)
            self.one_idea_layout.addWidget(idea_label)
        else:
            self.one_idea_layout.addWidget(date_label, 0, 0, 1, 5, alignment=Qt.AlignCenter)
            self.one_idea_layout.addWidget(idea_label, 1, 0, 3, 4)

        # Adds extra functions if it is the view page
        if self.is_view_page:
            # Favourite button functionality
            favourite_button = QPushButton()
            if self.db.return_favourite_status(id) == 1:
                favourite_button.setIcon(QIcon("./icons/filled_favourite.png"))
            else:
                favourite_button.setIcon(QIcon("./icons/favourite.png"))
            favourite_button.setIconSize(QSize(30, 30))
            favourite_button.setProperty("button_id", id)
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
                                            id=id: 
                                            self.confirm_delete(id))

            # Completed button functionality
            completed_button = QPushButton("Mark Done")
            completed_button.clicked.connect(lambda checked=False,
                                                id=id,
                                                widget=self.one_idea:
                                                self.confirm_complete(id, widget))

            # Add each element to the widget
            self.one_idea_layout.addWidget(favourite_button, 1, 5)
            self.one_idea_layout.addWidget(completed_button, 2, 5)
            self.one_idea_layout.addWidget(delete_button, 3, 5)
            self.scroll_layout.addWidget(self.one_idea)


    # Refreshes page upon each deletion or after idea is marked complete
    def refresh_page(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.load_page()


    def handle_idea_click(self, idea_id):
        idea, date, tag = self.db.retrieve_idea(idea_id)
        self.clicked_idea = idea
        self.date_preview.setText(date)
        self.idea_preview.setPlainText(self.clicked_idea)

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

    # Updates the favourites icon when clicked, and updates the database
    def favourites_clicked(self, button):
        if self.db.update_favourites(button.property("button_id")) == 1:
            button.setIcon(QIcon("./icons/filled_favourite.png"))
        else:
            button.setIcon(QIcon("./icons/favourite.png"))


# Handles each idea
class IdeaCard(QWidget):
    def __init__(self, idea_id, parent_page):
        super().__init__()
        self.idea_id = idea_id
        self.parent_page = parent_page

        # Allows styling for each widget
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Adds styling to each idea widget
        self.setObjectName("idea_widget")
        self.setStyleSheet("""
            #idea_widget {
                border: 1px solid gray;
                border-radius: 5px;
            }

            #idea_widget:hover {
                border: 2px solid orange;
            }
        """)

        # Turns cursor to hand when on a clickable area
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        self.parent_page.handle_idea_click(self.idea_id)