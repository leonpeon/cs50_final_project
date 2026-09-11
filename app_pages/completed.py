from app_pages.clickable_widget import ClickableWidget

# Handles the completed ideas page
class CompletedPage(ClickableWidget):
    def __init__(self, db):
        super().__init__(page=False, db=db)


        