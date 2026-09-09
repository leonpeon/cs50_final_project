from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPainter
from datetime import date, timedelta

class StreakPage(QWidget):
    def __init__(self):
        super().__init__()
        self.title_font = QFont()
        self.title_font.setPointSize(40)

        self.page_layout = QVBoxLayout(self)

        self.title = QLabel("Keep on shining")
        self.title.setFont(self.title_font)

        self.page_layout.addWidget(self.title)

        self.calendar = QWidget()
        self.calendar_layout = QGridLayout(self.calendar)
        self.calendar_layout.setHorizontalSpacing(2)
        self.page_layout.addWidget(self.calendar)
        self.create_calendar()


    # Create a grid of boxes (calendar) that each represent a day of the year
    def create_calendar(self):
        self.year = 2026
        current_date = date(self.year, 1, 1)
        end_date = date(self.year, 12, 31)

        row = 0
        column = 0

        while current_date <= end_date:
            day_dot = DayDot(current_date)

            if column == 20:
                row += 1
                column = 0
    
            self.calendar_layout.addWidget(day_dot, row, column)

            column += 1
            current_date += timedelta(days=1)


# A widget to represent the calendar dots
class DayDot(QWidget):
    def __init__(self, date):
        super().__init__()

        self.date = date
        self.setFixedSize(15, 15)

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(Qt.yellow)
        painter.setPen(Qt.NoPen)

        painter.drawEllipse(3, 3, 9 ,9)
