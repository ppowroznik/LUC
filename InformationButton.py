from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
import CustomPopup

class InformationButton(QPushButton):
    def __init__(self, text="", message="Default message", popup_title="", icon_image="inf_color.png", parent=None):
        super().__init__(text, parent)
        if icon_image == 'tutorial.png':
            self.setFixedSize(80, 80)
        else:
            self.setFixedSize(30, 30)
        self.message = message
        self.popup_title = popup_title
        self.icon_image = icon_image
        # self.icon_image = QPixmap(icon_image)
        self.setIcon(QtGui.QIcon(icon_image))
        if icon_image == 'tutorial.png':
            self.setIconSize(QSize(70,70))
        self.clicked.connect(self.show_custom_popup)
        self.setStyleSheet("""
            font-size: 18px;
            color: #FFFFFF;
            font-weight: bold;
            border-radius: 6px;
        """)

    def show_custom_popup(self):
        main_window = self.window()
        popup = CustomPopup.CustomPopup(self.message, self.popup_title, main_window)
        popup.exec_()
