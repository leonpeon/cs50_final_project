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

from PySide6.QtWidgets import QApplication
from app_pages.main_window import MainWindow

app = QApplication()

window = MainWindow()
window.show()

app.exec()