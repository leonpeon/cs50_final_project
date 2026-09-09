from PySide6.QtWidgets import QMainWindow, QStackedWidget
from app_pages.home import HomePage
from app_pages.spark import SparkPage
from app_pages.view import ViewPage
from app_pages.completed import CompletedPage
from app_pages.streak import StreakPage


# Handles each page
class MainWindow(QMainWindow):
    def __init__(self, database):
        super().__init__()

        self.setWindowTitle("Lightbulb Factory")
        self.showFullScreen()

        # Initialise pages
        self.home_page = HomePage(database)
        self.prompt_page = SparkPage()
        self.view_page = ViewPage(database)
        self.completed_page = CompletedPage(database)
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

        self.pages.currentChanged.connect(self.page_change)


    # Handles page updates
    def page_change(self):
        if self.pages.currentWidget() == self.view_page:
            self.view_page.refresh_page()

        if self.pages.currentWidget() == self.completed_page:
            self.completed_page.refresh_completed_page()
        