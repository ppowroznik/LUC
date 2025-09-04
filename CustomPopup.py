from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QHBoxLayout
)

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