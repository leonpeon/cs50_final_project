from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PySide6.QtCore import Qt, QSize


class ClickableWidget(QWidget):
    def __init__(self, date, idea, id, db):
        super().__init__()
        self.db = db
        self.setFixedSize(QSize(650, 170))

        self.setAttribute(Qt.WA_StyledBackground, True)

        self.one_idea_layout = QVBoxLayout(self)
        date_label = QLabel(date)
        
        # Text frame for idea
        idea_label = QTextEdit()
        idea_label.setReadOnly(True)
        idea_label.setPlainText(idea)
        idea_label.setMaximumHeight(150)
        idea_label.setStyleSheet("""
            QTextEdit {
                background-color: transparent;
                border: none;
            }
        """)
        idea_label.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        idea_label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        # self.setProperty("tag", tag)
        self.id = id

        self.one_idea_layout.addWidget(date_label, alignment=Qt.AlignCenter)
        self.one_idea_layout.addWidget(idea_label)

        self.setStyleSheet("""
            ClickableWidget {
                border: 1px solid gray;
                border-radius: 5px;
            }

            ClickableWidget:hover {
                border: 2px solid orange;
            }
        """)

        self.setCursor(Qt.PointingHandCursor)


    def mousePressEvent(self, event):
        # Get the widget information
        idea, date, tag = self.db.retrieve_idea(self.id)
