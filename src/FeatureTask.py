from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
import os

class featureTask(QDialog):
    def __init__(self):
        super(featureTask, self).__init__()
        loadUi('featureTask.ui', self)
        self.setWindowTitle('Feature Task')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(400, 200)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowModality(Qt.ApplicationModal)
        self.setModal(True)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def initUI(self):
        self.setWindowTitle("Contoh Panel Teks")
        self.setGeometry(100, 100, 300, 200)
        
        self.button = QPushButton('Tampilkan Panel Teks', self)
        self.button.setGeometry(50, 50, 200, 30)
        self.button.clicked.connect(self.showTextPanel)


    def on_pushButton_clicked(self):
        self.close()