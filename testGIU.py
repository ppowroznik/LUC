from PyQt5 import QtGui, QtCore


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QHBoxLayout, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import ImageLoader, CustomPopup, TopImageBar, BottomImageBar, RadioButtons, InformationButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lubelska Unia Cyfrowa")

        main_layout = QVBoxLayout(self)

        # ===== TOP PANEL =====
        self.image_panel_widget_top = TopImageBar.TopImageBar()
        main_layout.addWidget(self.image_panel_widget_top)

        # ===== CENTER (ŚRODKOWY OBSZAR) =====
        self.center_widget = QWidget()
        self.center_widget.setStyleSheet("background-color: #f5f5f7; border-radius: 10px;")
        center_layout = QVBoxLayout(self.center_widget)
        center_layout.setContentsMargins(16, 16, 16, 16)
        center_layout.setSpacing(12)

        # center_title = QLabel("Środkowy obszar – tu możesz dodawać własne widżety")
        # center_title.setStyleSheet("color: #7d7d7d; font-size: 16px;")
        # center_title.setAlignment(Qt.AlignHCenter)

        # button_info = InfoButton.InfoAboutApp()
        message = """
        Aplikacja ma za zadanie detekcji cech charakterystycznych chorób rzadkich oczu: 
        retinopatii barwinkowej (ang. Retinitis Pigmentosa) oraz dystrofii czopkowo-pręcikowej (ang. Cone-Rod Dystrophy). 
        Aplikacja także rozpoznaje obrazy, które nie zawierają wyżej wymienionych objawów.
        
        Retinopatia barwnikowa jest genetycznie uwarunkowaną choroba oczu, 
        charakteryzująca się postępującym uszkodzeniem i degeneracją fotoreceptorów siatkówki – pręcików i czopków. 
        Proces ten prowadzi do stopniowej utraty widzenia. Zaczyna się od zmniejszenia widzenia peryferyjnego, 
        a następnie obejmuje centralne pole widzenia. 
        
        Dystrofia czopkowo-pręcikowa jest grupą postepujących, wrodzonych chorób siatkówki. 
        Zmiany chorobowe dotyczą przede wszystkim czopków, odpowiedzialnych za widzenie dzienne, 
        rozpoznawanie barw i widzenie precyzyjne, a także w mniejszym zakresie pręcików, odpowiedzialnych za widzenie zmierzchowe. 
        Objawy towarzyszące chorobie to oczopląs, postępujący spadek ostrości wzroku, nadwrażliwość na światło, 
        zaburzenia rozróżniania barw oraz ubytek w centralnej części pola widzenia. 

        Wykonanie analizy w celu zidentyfikowania chorób rzadkich oczu składa się z następujących czynności:
        1.	Wczytania szerokokątnego obrazu powierzchni siatkówki.
        2.	Wybrania modelu uczenia maszynowego na podstawie którego zostanie przeprowadzona analiza.
        3.	Uzyskania wskazówek dotyczących.
        """

        button_info = InformationButton.InformationButton(text="",message=message, popup_title="Samouczek", icon_image="tutorial.png")
        center_layout.addWidget(button_info)

        image_layout = ImageLoader.ImageLoader()
        center_layout.addWidget(image_layout)
        button_layout = RadioButtons.RadioButtonGroup()
        center_layout.addWidget(button_layout)

        # center_layout.addWidget(center_title, alignment=Qt.AlignTop | Qt.AlignHCenter)
        center_layout.addStretch(1)

        # klucz: stretch=1 żeby środek wypełniał przestrzeń między top i bottom
        main_layout.addWidget(self.center_widget, 1)

        # ===== BOTTOM PANEL =====
        self.image_panel_widget_bottom = BottomImageBar.BottomImageBar()
        main_layout.addWidget(self.image_panel_widget_bottom)

        self.resize(1200, 800)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Lubelska Unia Cyfrowa - Detekcja chorób rzadkich oczu")
    app.setOrganizationName("LUC")
    window = MyWindow()
    window.setWindowTitle("Lubelska Unia Cyfrowa - Detekcja chorób rzadkich oczu")
    window.show()
    sys.exit(app.exec_())