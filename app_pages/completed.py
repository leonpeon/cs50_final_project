from PySide6.QtWidgets import QLabel, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QScrollArea, QTextEdit
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont

# Handles the completed ideas page
class CompletedPage(QWidget):
    def __init__(self, db):
        super().__init__()
        layout = QVBoxLayout(self)
        self.title_font = QFont()
        self.title_font.setPointSize(40)
        self.db = db

        self.title = QLabel("Completed Ideas")
        self.title.setFont(self.title_font)

        layout.addWidget(self.title)

        # Frame for ideas and the side preview
        self.idea_frame = QWidget()
        self.idea_frame_layout = QHBoxLayout(self.idea_frame)

        # Creates ability to scroll through ideas
        scroll_area = QScrollArea()

        self.ideas_widget = QWidget()
        self.ideas_layout = QVBoxLayout(self.ideas_widget)

        # Adds a preview frame for the idea
        self.preview_widget = QWidget()
        self.preview_layout = QHBoxLayout(self.preview_widget)
        self.preview_widget.setStyleSheet("""
            QWidget {
                border: 2px solid black;
             border-radius: 10px;
        }
        """)
        test_label = QLabel("HELLO!")
        self.preview_layout.addWidget(test_label)

        # Loops through ideas
        self.load_page()

        scroll_area.setWidget(self.ideas_widget)
        scroll_area.setFixedSize(QSize(700, 500))


        self.idea_frame_layout.addWidget(scroll_area)
        self.idea_frame_layout.addWidget(self.preview_widget)

        layout.addWidget(self.idea_frame)


    # Loads each idea
    def load_page(self):
        for idea, date, tag, idea_id, completed in self.db.view_ideas():
            if completed:
                one_idea = QWidget()
                one_idea.setFixedSize(QSize(650, 170))
                one_idea_layout = QVBoxLayout(one_idea)
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

                one_idea.setProperty("tag", tag)

                one_idea.setObjectName("ideaWidget")
                one_idea.setStyleSheet("""
                #ideaWidget {
                    border: 1px solid gray;
                    border-radius: 5px;
                }
                """)

                one_idea_layout.addWidget(date_label, alignment=Qt.AlignCenter)
                one_idea_layout.addWidget(idea_label)
                self.ideas_layout.addWidget(one_idea)


    # Refreshes page upon each deletion or after idea is marked complete
    def refresh_page(self):
        while self.ideas_layout.count():
            item = self.ideas_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.load_page()


        