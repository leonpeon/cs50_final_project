from PySide6.QtWidgets import QLabel, QWidget, QGridLayout, QVBoxLayout, QScrollArea, QTextEdit
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

        # Creates ability to scroll through ideas
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.ideas_widget = QWidget()
        self.ideas_layout = QVBoxLayout(self.ideas_widget)

        # Loops through ideas
        self.load_completed_page()

        scroll_area.setWidget(self.ideas_widget)
        layout.addWidget(scroll_area)


    # Loads each idea
    def load_completed_page(self):
        for idea, date, tag, idea_id, completed in self.db.view_ideas():
            if completed:
                one_idea = QWidget()
                one_idea.setFixedSize(QSize(700, 170))
                one_idea_layout = QGridLayout(one_idea)
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

                one_idea_layout.addWidget(date_label, 0, 0, 1, 5, alignment=Qt.AlignCenter)
                one_idea_layout.addWidget(idea_label, 1, 0, 3, 4)
                self.ideas_layout.addWidget(one_idea)


    # Refreshes page upon each deletion or after idea is marked complete
    def refresh_completed_page(self):
        while self.ideas_layout.count():
            item = self.ideas_layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()

        self.load_completed_page()