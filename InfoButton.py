
from PyQt5 import QtGui, QtCore, Qt

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class InfoAboutApp(QWidget):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("Wczytywanie obrazu z pliku")

        # Layout
        self.layout = QVBoxLayout()

# Przycisk do wczytywania obrazu
        self.load_button = QPushButton("Samouczek")
        self.load_button.setIcon("icon_info.jpg")
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setFixedSize(220, 30)
        self.load_button.setStyleSheet("""
                    font-size: 18px;
                    color: #FFFFFF;
                    font-weight: bold;
                    background-color: #e16e38;
                    border-radius: 6px;
                """)