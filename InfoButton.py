
from PyQt5 import QtGui, QtCore, Qt

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtGui

import InformationButton

class InfoAboutApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Samouczek")

        # Layout
        self.layout = QVBoxLayout()

# Przycisk do wczytywania obrazu
        self.load_button = QPushButton("")
        self.load_button.setIcon(QIcon("tutorial.png"))
            # "icon_info.jpg"))
        self.load_button.setIconSize(QSize(40, 40))
        self.load_button.clicked.connect(self.clicked)
        self.load_button.setFixedSize(50, 50)
        self.load_button.setStyleSheet("""
                    font-size: 18px;
                    color: #FFFFFF;
                    font-weight: bold;
                    background-color: #e16e38;
                    border-radius: 6px;
                """)

        self.layout.addWidget(self.load_button)
        self.layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.layout)

    def clicked(self):
        InformationButton.InformationButton(text="",
                                            message="Proszę wczytac obraz OPTOS. Dosępne rozszerzenia obrazu to: *.png *.jpg *.jpeg *.bmp *.gif ",
                                            popup_title="Informacja")