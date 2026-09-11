# LIGHTBULB FACTORY

# TODO
# 1. Homepage:
#       - Add an aesthetically pleasing home page
# 2. Prompt page:
#       - Make better txt file for adjectvies, nouns and verbs
#       - Replace placeholder word labels with lightbulb images
#       - If the user decides to use the prompt, it should take them to the main page with prompt (create button)
#       - Combine prompt page with homepage
# 3. View page:
#       - Improve widget UI
#       - Favourited ideas should move to the beginning.
#       - Add filter search (by date asc, desc, tags)
# 4. Completed page:
#       - Create SQL column for "date_completed"
#       - Add delete button?
# 5. Streaks page:
#       - Create submenus for each year (2026, 2027)
# 6. Settings:
#       - Create setting for word limit
#       - Create bg colour setting
#       - Create notification setting

from PySide6.QtWidgets import QApplication
from app_pages.main_window import MainWindow
from app_pages.database import Database

app = QApplication()
database = Database()

window = MainWindow(database)
window.show()

app.exec()
database.connection.close()