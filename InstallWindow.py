from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QLabel,QLineEdit
from LoginWindow import LoginScreen

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Install Vehicle Parking System")
        self.resize(400,200)

        layout=QVBoxLayout()

        label_db_name=QLabel("Database Name:")
        label_db_username=QLabel("Database Username:")
        label_db_password=QLabel("Database Password:")
        label_admin_username=QLabel("Admin Username:")
        label_admin_password=QLabel("Admin Password:")
        label_no_of_two_seater=QLabel("No of two wheeler space:")
        label_no_of_four_seater=QLabel("No of four wheeler space:")


        input_db_name=QLineEdit()
        input_db_username=QLineEdit()
        input_db_password=QLineEdit()
        input_admin_username=QLineEdit()
        input_admin_password=QLineEdit()
        input_two_wheeler=QLineEdit()
        input_four_wheeler=QLineEdit()

        buttonsave=QPushButton("Save Config")

        layout.addWidget(label_db_name)
        layout.addWidget(input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(input_db_password)
        layout.addWidget(label_admin_username)
        layout.addWidget(input_admin_username)
        layout.addWidget(label_admin_password)
        layout.addWidget(input_admin_password)
        layout.addWidget(label_no_of_two_seater)
        layout.addWidget(input_two_wheeler)
        layout.addWidget(label_no_of_four_seater)
        layout.addWidget(input_four_wheeler)
        layout.addWidget(buttonsave)

        buttonsave.clicked.connect(self.showStepInfo)

        self.setLayout(layout)

    def showStepInfo(self):
        self.close()
        self.login=LoginScreen()
        self.login.showLoginScreen()
        print("Save")