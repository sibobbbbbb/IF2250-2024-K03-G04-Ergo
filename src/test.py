import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Contoh Panel Teks")
        self.setGeometry(100, 100, 300, 200)
        
        self.button = QPushButton('Tampilkan Panel Teks', self)
        self.button.setGeometry(50, 50, 200, 30)
        self.button.clicked.connect(self.showTextPanel)
        
    def showTextPanel(self):
        # Membuat panel teks
        self.text_panel = QWidget()
        layout = QVBoxLayout()
        
        # Membuat widget input teks
        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)
        
        # Membuat tombol OK
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.getText)
        layout.addWidget(ok_button)
        
        # Mengatur layout
        self.text_panel.setLayout(layout)
        self.setCentralWidget(self.text_panel)
        
    def getText(self):
        text = self.text_edit.text()
        print("Teks yang dimasukkan:", text)
        
        # Menghapus panel teks setelah mendapat input
        self.text_panel.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
