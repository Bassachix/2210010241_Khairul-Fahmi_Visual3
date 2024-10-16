# Created by Khairul Fahmi_2210010241_5P

# ============= Window Management =============
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        cwa = self.frameGeometry() # Cek ukuran main window app kita
        cwc = QDesktopWidget().availableGeometry().center() # Pada screen saya: (682, 363)

        #Print(cwc)
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.setFixedSize(500, 500) # Agar tidak bisa di resize! icon maximize juga akan otomatis hilang

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()