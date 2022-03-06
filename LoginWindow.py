from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit
import sys
from HomeWindow import HomeScreen

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Login")
        self.resize(250,250)

        layout=QVBoxLayout()

        label_username=QLabel("Username:")
        input_username=QLineEdit()
        label_password=QLabel("Password:")
        input_password=QLineEdit()

        btn_login=QPushButton("Login")

        layout.addWidget(label_username)
        layout.addWidget(input_username)
        layout.addWidget(label_password)
        layout.addWidget(input_password)
        layout.addWidget(btn_login)

        btn_login.clicked.connect(self.showHome)

        self.setLayout(layout)

    def showLoginScreen(self):
        self.show()

    def showHome(self):
        self.close()
        self.home=HomeScreen()
        self.home.show()