from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QSize


class ClickableWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(650, 170))

        self.setAttribute(Qt.WA_StyledBackground, True)

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
        print("Widget clicked")