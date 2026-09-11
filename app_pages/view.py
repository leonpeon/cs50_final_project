from app_pages.clickable_widget import ClickableWidget


# Handles the view page
class ViewPage(ClickableWidget):
    def __init__(self, db):
        super().__init__(page=True, db=db)