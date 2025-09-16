from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
import CustomPopup

class InformationButton(QPushButton):
    def __init__(self, text="", message="Default message", popup_title="", parent=None):
        super().__init__(text, parent)
        self.setFixedSize(30, 30)
        self.message = message
        self.popup_title = popup_title
        self.setIcon(QtGui.QIcon('inf_color.png'))
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
