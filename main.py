# LIGHTBULB FACTORY

# TODO
# 1. Homepage: text-box, greeting image, tags
#       - Save what the user has written once submitted.
#       - Give ability to add tags
#       - Add an aethetically pleasing home page
# 2. Generate prompt: sentence randomiser, image generator, question asker
#       - Create database of nouns/verbs
#       - Button press will randomly generate noun-verb-noun sequence
#       - Get image database
#       - Generate random images
#       - Create list of questions
# 3. View page: list of all ideas, that you can rank
#       - Create a list of all ideas, along with adjustable rank and date.
# 4. Completed page: portfolio of ideas that are acted upon.
#       - Create a page which marks which ideas have been acted upon
# 5. Streaks page: shows your streak (Keep the light on)
#       - Shows list of lightbulbs
# 6. Settings: set word limit, colours, send notification.
#       - Settings page to manage word limit, GUI colours, and email notifications

from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, QVBoxLayout)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lightbulb Factory")
        self.showFullScreen()

        # HOME PAGE
        self.home_page = QWidget()
        title_font = QFont()
        title_font.setPointSize(40)

        home_page_layout = QVBoxLayout(self.home_page)
        home_title = QLabel("Welcome to the factory")
        home_title.setFont(title_font)
        home_title.setAlignment(Qt.AlignCenter)

        idea_text_box = QTextEdit(placeholderText="Write your idea")

        submit_button = QPushButton("Save")
        submit_button.clicked.connect(lambda: print(idea_text_box.toPlainText()))


        home_page_layout.addWidget(home_title)
        home_page_layout.addWidget(idea_text_box)
        home_page_layout.addWidget(submit_button)


        # Prompt Page
        self.prompt_page = QWidget()
        prompt_page_layout = QVBoxLayout(self.prompt_page)
        prompt_page_title =  QLabel("Click for a prompt")
        prompt_page_title.setAlignment(Qt.AlignCenter)

        prompt_page_layout.addWidget(prompt_page_title)


        # Create stacked widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.prompt_page)

        self.setCentralWidget(self.pages)

        # Creates a menu bar to navigate to different pages
        menubar = self.menuBar()
        home = menubar.addAction("Create")
        home.triggered.connect(self.show_home_page)
        
        spark = menubar.addAction("Spark")
        spark.triggered.connect(self.show_spark_page)

        view = menubar.addAction("View")
        completed = menubar.addAction("Home")

        quit = menubar.addAction("Quit")
        quit.triggered.connect(lambda: self.close())

    def show_home_page(self):
        self.pages.setCurrentWidget(self.home_page)

    def show_spark_page(self):
        self.pages.setCurrentWidget(self.prompt_page)
    

        



app = QApplication()

window = MainWindow()
window.show()

app.exec()