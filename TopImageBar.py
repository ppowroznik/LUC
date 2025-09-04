from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QHBoxLayout, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class TopImageBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: #324151; border-radius: 10px;")
        self.setFixedHeight(100)

        top_layout = QHBoxLayout(self)
        top_layout.setContentsMargins(12, 8, 12, 8)
        top_layout.setSpacing(12)

        top_img1 = QLabel()
        top_img1.setPixmap(QPixmap("LUC_white.png").scaled(150, 60, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        top_img2 = QLabel()
        top_img2.setPixmap(QPixmap("logo_up.png").scaled(116, 33, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        top_img3 = QLabel()
        top_img3.setPixmap(QPixmap("logo_umlub_biale.png").scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        top_img4 = QLabel()
        top_img4.setPixmap(QPixmap("loga-PL_RGB-04.png").scaled(250, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        top_layout.addWidget(top_img1)
        top_layout.addStretch(1)
        top_layout.addWidget(top_img2)
        top_layout.addWidget(top_img3)
        top_layout.addWidget(top_img4)