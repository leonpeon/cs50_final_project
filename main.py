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
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont
from random import choice


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lightbulb Factory")
        self.showFullScreen()
        title_font = QFont()

        # HOME PAGE
        # TODO: Update GUI, save idea to a SQL database
        self.home_page = QWidget()
        title_font.setPointSize(40)

        home_page_layout = QVBoxLayout(self.home_page)
        home_title = QLabel("Welcome to the factory")
        home_title.setFont(title_font)

        idea_text_box = QTextEdit(placeholderText="Write your idea")
        idea_text_box.setFixedSize(750, 300)

        submit_button = QPushButton("Save")
        submit_button.clicked.connect(lambda: self.clear_idea(idea_text_box))

        home_page_layout.addWidget(home_title, alignment=Qt.AlignCenter)
        home_page_layout.addWidget(idea_text_box, alignment=Qt.AlignCenter)
        home_page_layout.addWidget(submit_button)


        # PROMPT
        self.prompt_page = QWidget()
        prompt_page_layout = QVBoxLayout(self.prompt_page)
        prompt_page_title =  QLabel("Click for a prompt")
        prompt_page_title.setFont(title_font)
        prompt_page_title.setAlignment(Qt.AlignCenter)

        prompt_frame = QWidget()
        prompt_frame_layout = QHBoxLayout(prompt_frame)
        label1 = QLabel("ONE")
        label2 = QLabel("TWO")
        label3 = QLabel("THREE")

        for label in [label1, label2, label3]:
            label.setAlignment(Qt.AlignCenter)
            prompt_frame_layout.addWidget(label)

        spark_button = QPushButton("Generate")
        spark_button.clicked.connect(lambda: self.generate_prompt(label1, label2, label3))

        prompt_page_layout.addWidget(prompt_page_title)
        prompt_page_layout.addWidget(prompt_frame)
        prompt_page_layout.addWidget(spark_button)


        # VIEW PAGE

        # COMPLETED PAGE

        # STREAK PAGE



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
        completed = menubar.addAction("Completed")
        streak = menubar.addAction("Streak")

        quit = menubar.addAction("Quit")
        quit.triggered.connect(lambda: self.close())

    def show_home_page(self):
        self.pages.setCurrentWidget(self.home_page)

    def show_spark_page(self):
        self.pages.setCurrentWidget(self.prompt_page)

    # FUNCTIONS FOR HOME PAGE
    def clear_idea(self, text_field):
        print(text_field.toPlainText())
        text_field.clear()

    # FUNCTIONS FOR SPARK PAGE
    # Gives a noun-verb-noun prompt when the generate button is pressed
    def generate_prompt(self, label1, label2, label3):
        with open("word_lists/nouns_5000.txt") as file:
            noun_list = file.readlines()
            first_noun = choice(noun_list)
            second_noun = choice(noun_list)

            # Checks if the second noun was already selected
            while second_noun == first_noun:
                second_noun = choice(noun_list)

            label1.setText(first_noun)
            label3.setText(second_noun)

        with open("word_lists/verbs_5000.txt") as file:
            verb = choice(file.readlines())

            label2.setText(verb)

              
    

        



app = QApplication()

window = MainWindow()
window.show()

app.exec()