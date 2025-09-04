from PyQt5.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, QHBoxLayout, QButtonGroup, QRadioButton
)

from PyQt5.QtCore import Qt


class RadioButtonGroup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modele do analizy")
        self.resize(300, 200)

        # Layout główny
        layout = QVBoxLayout()

        # Etykieta do wyświetlania wybranego elementu
        self.label = QLabel("Wybierz model do analizy:")
        layout.addWidget(self.label)

        # Grupa logiczna (QButtonGroup)
        self.button_group = QButtonGroup(self)
        self.button_group.buttonClicked.connect(self.on_radio_button_selected)

        # Tworzenie przycisków radiowych
        options = ["VGG16", "Model 2", "Model 3", "Model 4", "Model 5"]
        for i, option in enumerate(options):
            radio = QRadioButton(option)
            self.button_group.addButton(radio, id=i)  # Nadajemy ID każdemu przyciskowi
            layout.addWidget(radio)

        self.setLayout(layout)


    def on_radio_button_selected(self, button):
        selected_text = button.text()
        self.label.setText(f"Wybrano model: {selected_text}")
