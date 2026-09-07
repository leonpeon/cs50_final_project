from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout)
from app_pages.home import HomePage
from app_pages.spark import SparkPage
from app_pages.view import ViewPage
from app_pages.completed import CompletedPage
from app_pages.streak import StreakPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lightbulb Factory")
        self.showFullScreen()

        # Initialise pages
        self.home_page = HomePage()
        self.prompt_page = SparkPage()
        self.view_page = ViewPage()
        self.completed_page = CompletedPage()
        self.streak_page = StreakPage()

        # Create stacked widget
        self.pages = QStackedWidget()
        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.prompt_page)
        self.pages.addWidget(self.view_page)
        self.pages.addWidget(self.completed_page)
        self.pages.addWidget(self.streak_page)

        self.setCentralWidget(self.pages)

        # Creates a menu bar to navigate to different pages
        menubar = self.menuBar()
        
        home = menubar.addAction("Create")
        home.triggered.connect(lambda: self.pages.setCurrentWidget(self.home_page))
        
        spark = menubar.addAction("Spark")
        spark.triggered.connect(lambda: self.pages.setCurrentWidget(self.prompt_page))

        view = menubar.addAction("View")
        view.triggered.connect(lambda: self.pages.setCurrentWidget(self.view_page))

        completed = menubar.addAction("Completed")
        completed.triggered.connect(lambda: self.pages.setCurrentWidget(self.completed_page))

        streak = menubar.addAction("Streak")
        streak.triggered.connect(lambda: self.pages.setCurrentWidget(self.streak_page))

        quit = menubar.addAction("X")
        quit.triggered.connect(lambda: self.close())