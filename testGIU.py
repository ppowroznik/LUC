import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


# class CustomPopup(QDialog):
#     def __init__(self, message, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Mój Popup")
#         self.setModal(True)
#
#         layout = QVBoxLayout()
#
#         label = QLabel(message)
#         label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(label)
#
#         buttons = QDialogButtonBox(QDialogButtonBox.Ok)
#         buttons.accepted.connect(self.accept)
#         layout.addWidget(buttons)
#
#         self.setLayout(layout)
#         self.resize(250, 120)
#
#         self.setStyleSheet("""
#                     QDialog {
#                         background-color: #324151;
#                         border-radius: 10px;
#                     }
#                     QLabel {
#                         font-size: 14px;
#                         color: #FFFFFF;
#                     }
#                     QPushButton {
#                         background-color: #e16e38;
#                         color: white;
#                         padding: 6px 12px;
#                         border-radius: 6px;
#                     }
#                     QPushButton:hover {
#                         background-color: #c5744e;
#                     }
#                 """)


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class CustomPopup(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mój Popup")
        self.setModal(True)

        layout = QVBoxLayout()
        label = QLabel(message)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)
        layout.addWidget(buttons)

        self.setLayout(layout)
        self.resize(250, 120)
        self.setStyleSheet("""
            QDialog { background-color: #f5f5f7; border-radius: 10px; }
            QLabel { font-size: 14px; color: #7d7d7d; }
            QPushButton { background-color: #e16e38; color: white; padding: 6px 12px; border-radius: 6px; }
            QPushButton:hover { background-color: #c5744e; }
        """)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lubelska Unia Cyfrowa")

        main_layout = QVBoxLayout(self)

        # ===== TOP PANEL =====
        self.image_panel_widget_top = QWidget()
        self.image_panel_widget_top.setStyleSheet("background-color: #324151; border-radius: 10px;")
        self.image_panel_widget_top.setFixedHeight(100)

        top_layout = QHBoxLayout(self.image_panel_widget_top)
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
        self.image_panel_widget_bottom = QWidget()
        self.image_panel_widget_bottom.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        self.image_panel_widget_bottom.setFixedHeight(130)

        bottom_layout = QHBoxLayout(self.image_panel_widget_bottom)
        bottom_layout.setContentsMargins(12, 8, 12, 8)
        bottom_layout.setSpacing(12)

        bottom_img1 = QLabel()
        bottom_img1.setPixmap(QPixmap("01_znak_siatka_podstawowy_kolor_biale_tlo-1.png").scaled(300, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        bottom_img2 = QLabel()
        bottom_img2.setPixmap(QPixmap("05_znak_-siatka_uproszczony_kolor_biale_tlo-1.png").scaled(300, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))

        bottom_layout.addWidget(bottom_img1, alignment=Qt.AlignLeft | Qt.AlignVCenter)
        bottom_layout.addStretch(1)
        bottom_layout.addWidget(bottom_img2, alignment=Qt.AlignRight | Qt.AlignVCenter)

        main_layout.addWidget(self.image_panel_widget_bottom)

        self.resize(1200, 800)

    def show_custom_popup(self):
        popup = CustomPopup("To jest mój własny popup z przyciskiem OK", self)
        popup.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Lubelska Unia Cyfrowa - Detekcja chorób rzadkich oczu")
    app.setOrganizationName("LUC")
    window = MyWindow()
    window.setWindowTitle("Lubelska Unia Cyfrowa - Detekcja chorób rzadkich oczu")
    window.show()
    sys.exit(app.exec_())
