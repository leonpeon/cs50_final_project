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
# 5. Settings: set word limit, colours, send notification.
#       - Settings page to manage word limit, GUI colours, and email notifications

from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lightbulb Factory")
        self.showFullScreen()

        menubar = self.menuBar()
        home = menubar.addAction("Home")
        help = menubar.addAction("Help")
        view = menubar.addAction("Home")
        completed = menubar.addAction("Home")
        quit = menubar.addAction("Quit")
        quit.triggered.connect(lambda: self.close())


        # Home Page



app = QApplication()

window = MainWindow()
window.show()

app.exec()