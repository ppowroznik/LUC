from contextlib import nullcontext
from idlelib.runscript import indent_message
from tokenize import String

from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QHBoxLayout, QButtonGroup, QRadioButton
)

from PyQt5.QtCore import Qt

import InformationButton


class RadioButtonGroup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modele do analizy")
        self.resize(300, 200)

        # Layout główny i w środku horyzontalny
        self.layout = QVBoxLayout()
        self.inner_layout = QHBoxLayout()

        # Etykieta do wyświetlania wybranego elementu
        self.label = QLabel("Wybierz model do analizy:")
        self.label.setStyleSheet("color: #7d7d7d; font-size: 20px;")
        # layout.addWidget(self.label)
        self.inner_layout.addWidget(self.label)
        self.inner_layout.setAlignment(Qt.AlignCenter)

        self.info_button = InformationButton.InformationButton(text="",
                                                               message="Proszę wybrać model na podstawie którego zostanie zweryfikowane występowania objawów dla rzadkich chorób oczu",
                                                               popup_title="Informacja")
        self.inner_layout.addWidget(self.info_button)
        self.layout.addLayout(self.inner_layout)
        self.layout.setAlignment(Qt.AlignLeft)

        # Grupa logiczna (QButtonGroup)
        # self.button_group = QButtonGroup(self)
        self.button_group = []
        # self.button_group.buttonClicked.connect(self.on_radio_button_selected)

        # Tworzenie przycisków radiowych
        options = ["VGG16", "Model 2", "Model 3", "Model 4", "Model 5"]
        for i, option in enumerate(options):
            radio = QRadioButton(option)
            radio.setStyleSheet('QRadioButton'
                                '{'
                                'color: #7d7d7d;'
                                'font-size: 16px;'
                                # 'spacing : 10px;'
                                'margin : 5px'
                                       "}"
                                )
            # self.button_group.addButton(radio, id=i)  # Nadajemy ID każdemu przyciskowi
            self.button_group.append(radio)
            self.layout.addWidget(radio)

        self.verify_button = QPushButton("Zweryfikuj obraz")
        self.verify_button.clicked.connect(self.verify)
        self.verify_button.setFixedSize(220, 30)
        self.verify_button.setStyleSheet("""
                                        font-size: 18px;
                                        color: #FFFFFF;
                                        font-weight: bold;
                                        background-color: #e16e38;
                                        border-radius: 6px;
                                    """)

        self.layout.addWidget(self.verify_button)

        self.setLayout(self.layout)

    def verify(self):
        for i, rb in enumerate(self.button_group):
            if rb.isChecked():
                self.label.setText(f"Wybrano model: {i+1}")
                self.label.setStyleSheet("QLabel { font-size: 20px; color: #7d7d7d; }")
                return
            self.label.setText(f"Proszę wybrać model bo analizy")
            self.label.setStyleSheet("QLabel { font-size: 28px; color: #e16e38; }")

    def on_radio_button_selected(self, button):
        selected_text = button.text()
        self.label.setText(f"Wybrano model: {selected_text}")
        self.label.setStyleSheet("QLabel { font-size: 40px; color: red; }")

