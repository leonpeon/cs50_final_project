from PySide6.QtWidgets import QLabel, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QScrollArea, QTextEdit
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from app_pages.clickable_widget import ClickableWidget

# Handles the completed ideas page
class CompletedPage(ClickableWidget):
    def __init__(self, db):
        super().__init__(page=False, db=db)


        