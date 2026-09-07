from datetime import datetime
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("lightbulb.db")
        self.db = self.connection.cursor()

        self.date = datetime.now().strftime("%d-%m-%Y")


    def save_idea(self, text_field, tag):
        print(f"SAVED: {text_field.toPlainText()}")
        self.db.execute("INSERT INTO ideas (idea, tag, date) VALUES (?, ?, ?)", (text_field.toPlainText(), tag.currentText(), self.date))
        self.connection.commit()
        text_field.clear()