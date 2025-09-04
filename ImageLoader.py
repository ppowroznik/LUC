from PyQt5 import QtGui, QtCore

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
)
from PyQt5.QtGui import QPixmap

import InformationButton

class ImageLoader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wczytywanie obrazu z pliku")

        # Layout
        self.layout = QVBoxLayout()

        # Przycisk do wczytywania obrazu
        self.load_button = QPushButton("Wczytaj obraz do analizy")
        self.load_button.clicked.connect(self.load_image)
        self.load_button.setFixedSize(220, 30)
        self.load_button.setStyleSheet("""
                    font-size: 18px;
                    color: #FFFFFF;
                    font-weight: bold;
                    background-color: #e16e38;
                    border-radius: 6px;
                """)

        #Tutaj przycisk z informacją

        self.info_button = InformationButton.InformationButton(text="",message="Proszę wczytac obraz OPTOS. Dosępne rozszerzenia obrazu to: *.png *.jpg *.jpeg *.bmp *.gif ", popup_title="Informacja")
        # self.info_button.setIcon(QtGui.QIcon('inf.png'))
        # self.info_button.setFixedSize(30, 30)
        # self.info_button.clicked.connect(self.show_info)
        # self.info_button.setStyleSheet("""
        #             font-size: 18px;
        #             color: #FFFFFF;
        #             font-weight: bold;
        #             # background-color: #e16e38;
        #             border-radius: 6px;
        #         """)

        # Etykieta do wyświetlania obrazu
        self.image_label = QLabel("Tutaj pojawi się obraz")
        self.image_label.setScaledContents(True)  # Automatyczne skalowanie obrazu
        self.image_label.setFixedSize(300, 300)
        # self.image_label.resize(300, 300)

        # Dodajemy widgety do layoutu
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.info_button)
        self.layout.addWidget(self.image_label)


        self.setLayout(self.layout)
        self.resize(300, 300)

    def load_image(self):
        # Otwieramy okno dialogowe do wyboru pliku
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Wybierz obraz do analizy",
            "",
            "Obrazy (*.png *.jpg *.jpeg *.bmp *.gif);;Wszystkie pliki (*)"
        )

        # Jeżeli użytkownik wybrał plik, wczytaj go
        if file_path:
            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(300, 300)
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("Nie wybrano pliku.")

    def show_info(self):
        pass