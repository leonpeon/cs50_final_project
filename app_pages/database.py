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


    def view_ideas(self):
        ideas = self.db.execute("SELECT idea, date, tag, favourite, completed, id FROM ideas").fetchall()
        return ideas

    def delete_idea(self, idea_id):
        self.db.execute("DELETE FROM ideas WHERE id = ?", (idea_id,))
        self.connection.commit()

    def update_favourites(self, idea_id):
        favourite_status = self.db.execute("SELECT favourite FROM ideas WHERE id = ?", (idea_id,)).fetchone()[0]

        if favourite_status == 0:
            self.db.execute("UPDATE ideas SET favourite = 1 WHERE id = ?", (idea_id,))
            favourite_status = 1
        else:
            self.db.execute("UPDATE ideas SET favourite = 0 WHERE id = ?", (idea_id,))
            favourite_status = 0

        self.connection.commit()
        return favourite_status

    def return_favourite_status(self, idea_id):
        status = self.db.execute("SELECT favourite FROM ideas WHERE id = ?", (idea_id,)).fetchone()[0]
        return status
