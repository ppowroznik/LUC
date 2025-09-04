
from PyQt5 import QtGui, QtCore


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QHBoxLayout, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import ImageLoader, CustomPopup, TopImageBar, BottomImageBar


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

        center_title = QLabel("Środkowy obszar – tu możesz dodawać własne widżety")
        center_title.setStyleSheet("color: #7d7d7d; font-size: 16px;")
        center_title.setAlignment(Qt.AlignHCenter)

        # Image loader
        image_layout = ImageLoader.ImageLoader()
        center_layout.addWidget(image_layout)

        # przykładowy przycisk „?” w środku
        self.button = QPushButton("?")
        self.button.setFixedSize(22, 22)
        self.button.clicked.connect(self.show_custom_popup)
        self.button.setStyleSheet("""
            font-size: 18px;
            color: #FFFFFF;
            font-weight: bold;
            background-color: #e16e38;
            border-radius: 6px;
        """)

        center_layout.addWidget(center_title, alignment=Qt.AlignTop | Qt.AlignHCenter)
        center_layout.addStretch(1)
        center_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        center_layout.addStretch(2)

        # klucz: stretch=1 żeby środek wypełniał przestrzeń między top i bottom
        main_layout.addWidget(self.center_widget, 1)

        # ===== BOTTOM PANEL =====
        self.image_panel_widget_bottom = BottomImageBar.BottomImageBar()
        main_layout.addWidget(self.image_panel_widget_bottom)

        self.resize(1200, 800)

    def show_custom_popup(self):
        popup = CustomPopup.CustomPopup("To jest mój własny popup z przyciskiem OK", self)
        popup.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Lubelska Unia Cyfrowa - Detekcja chorób rzadkich oczu")
    app.setOrganizationName("LUC")
    window = MyWindow()
    window.setWindowTitle("Lubelska Unia Cyfrowa - Detekcja chorób rzadkich oczu")
    window.show()
    sys.exit(app.exec_())