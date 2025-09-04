from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
import CustomPopup

class InformationButton(QPushButton):
    def __init__(self, text="Ala", message="Default message", parent=None):
        super().__init__(text, parent)
        self.setFixedSize(30, 30)
        self.message = message
        self.setIcon(QtGui.QIcon('inf.png'))
        self.clicked.connect(self.show_custom_popup)
        self.setStyleSheet("""
            font-size: 18px;
            color: #FFFFFF;
            font-weight: bold;
            border-radius: 6px;
        """)

    def show_custom_popup(self):
        main_window = self.window()
        popup = CustomPopup.CustomPopup(self.message, main_window)
        popup.exec_()
