from PyQt5.QtWidgets import (
    QWidget, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class BottomImageBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        self.setFixedHeight(130)

        bottom_layout = QHBoxLayout(self)
        bottom_layout.setContentsMargins(12, 8, 12, 8)
        bottom_layout.setSpacing(12)

        bottom_img1 = QLabel()
        bottom_img1.setPixmap(
            QPixmap("01_znak_siatka_podstawowy_kolor_biale_tlo-1.png").scaled(300, 120, Qt.KeepAspectRatio,
                                                                              Qt.SmoothTransformation))
        bottom_img2 = QLabel()
        bottom_img2.setPixmap(
            QPixmap("05_znak_-siatka_uproszczony_kolor_biale_tlo-1.png").scaled(300, 120, Qt.KeepAspectRatio,
                                                                                Qt.SmoothTransformation))

        bottom_layout.addWidget(bottom_img1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(bottom_img2, alignment=Qt.AlignRight | Qt.AlignVCenter)