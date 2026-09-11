from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QGridLayout, QHBoxLayout, QScrollArea
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont


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
        self.setAttribute(Qt.WA_StyledBackground, True)

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
        self.preview_widget.setFixedSize(QSize(500, 500))
        self.preview_layout = QHBoxLayout(self.preview_widget)
        self.preview_widget.setObjectName("preview_widget")
        self.preview_widget.setStyleSheet("""
            #preview_widget {
                border: 2px solid black;
                border-radius: 10px;
        }
        """)

        ### TODO
        idea_preview = QLabel("HELLO!")
        self.preview_layout.addWidget(idea_preview)

        self.load_page()

        # Add elements to the ideas widget
        scroll_area.setWidget(self.scroll_widget)
        scroll_area.setFixedSize(QSize(600, 500))

        self.idea_frame_layout.addWidget(scroll_area)
        self.idea_frame_layout.addWidget(self.preview_widget)

        # Adds idea widget to the main widget
        self.frame_layout.addWidget(self.idea_frame)


    def load_page(self):
        for idea, date, tag, idea_id, completed in self.db.view_ideas():

            # If COMPLETED page
            if not self.is_view_page:
                if completed:
                    self.one_idea = QWidget()
                    self.one_idea_layout = QVBoxLayout(self.one_idea)
                    self.clickable_idea(idea, date, idea_id)
                    self.scroll_layout.addWidget(self.one_idea)

            # If VIEW page
            else:
                if not completed:
                    self.one_idea = QWidget()
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

        # Adds styling to each idea widget
        self.one_idea.setObjectName("idea_widget")
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
        # Get the widget information
        idea, date, tag = self.db.retrieve_idea(self.id)
        print("I'm clicked")

    # Refreshes page upon each deletion or after idea is marked complete
    def refresh_page(self):
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.load_page()
