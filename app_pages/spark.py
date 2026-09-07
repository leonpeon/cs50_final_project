from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLayout, QGroupBox, QTextEdit, 
                               QMainWindow, QStackedWidget, QPushButton, QWidget, 
                               QVBoxLayout, QHBoxLayout)
from PySide6.QtCore import QCalendar, Qt
from PySide6.QtGui import QFont
from random import choice

class SparkPage(QWidget):
    def __init__(self):
        super().__init__()
        self.title_font = QFont()
        self.title_font.setPointSize(40)
        self.word_font = QFont()
        self.word_font.setPointSize(24)

        layout = QVBoxLayout(self)
        self.title =  QLabel("Click for a prompt")
        self.title.setFont(self.title_font)
        self.title.setAlignment(Qt.AlignCenter)

        self.prompt_frame = QWidget()
        prompt_frame_layout = QHBoxLayout(self.prompt_frame)
        label1 = QLabel("ONE")
        label2 = QLabel("TWO")
        label3 = QLabel("THREE")

        for label in [label1, label2, label3]:
            label.setAlignment(Qt.AlignCenter)
            label.setFont(self.word_font)
            prompt_frame_layout.addWidget(label)

        spark_button = QPushButton("Generate")
        spark_button.clicked.connect(lambda: self.generate_prompt(label1, label2, label3))

        layout.addWidget(self.title)
        layout.addWidget(self.prompt_frame)
        layout.addWidget(spark_button)

    # Gives a noun-verb-noun prompt when the generate button is pressed
    def generate_prompt(self, label1, label2, label3):
        with open("./word_lists/nouns_5000.txt") as file:
            noun_list = file.readlines()
            first_noun = choice(noun_list)
            second_noun = choice(noun_list)

            # Checks if the second noun was already selected
            while second_noun == first_noun:
                second_noun = choice(noun_list)

            label1.setText(first_noun)
            label3.setText(second_noun)

        with open("./word_lists/verbs_5000.txt") as file:
            verb = choice(file.readlines())

            label2.setText(verb)