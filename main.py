# LIGHTBULB FACTORY

# TODO
# 1. Homepage: text-box, greeting image, tags
#       - Add an aesthetically pleasing home page
# 2. Generate prompt: sentence randomiser, image generator, question asker
#       - Create database of nouns/verbs/ajective
#       - Improve UI of words - replace placeword labels with lightbulb image
#       - If the user decides to use the prompt, it should take them to the main page with prompt
# 3. View page: list of all ideas, that you can rank
#       - Create a list of all ideas that refreshes, along with and date.
# 4. Completed page: portfolio of ideas that are acted upon.
#       - Create a page which marks which ideas have been acted upon
# 5. Streaks page: shows your streak (Keep the light on)
#       - Shows list of lightbulbs
# 6. Settings: set word limit, colours, send notification.
#       - Settings page to manage word limit, GUI colours, and email notifications

from PySide6.QtWidgets import QApplication
from app_pages.main_window import MainWindow
from app_pages.database import Database

app = QApplication()
database = Database()

window = MainWindow(database)
window.show()

app.exec()
database.connection.close()