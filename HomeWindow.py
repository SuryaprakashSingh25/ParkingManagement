from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QFrame


class HomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.resize(500,400)
        widget=QWidget()

        layout_horizontal=QHBoxLayout()
        menu_vertical_layout=QVBoxLayout()

        btn_home=QPushButton("Home")
        btn_add=QPushButton("Add Vehicle")
        btn_manage = QPushButton("Manage Vehicle")
        btn_history = QPushButton("History")

        btn_home.clicked.connect(self.showHome)
        btn_add.clicked.connect(self.showAdd)
        btn_manage.clicked.connect(self.showManage)
        btn_history.clicked.connect(self.showHistory)

        menu_frame = QFrame()

        menu_vertical_layout.addWidget(btn_home)
        menu_vertical_layout.addWidget(btn_add)
        menu_vertical_layout.addWidget(btn_manage)
        menu_vertical_layout.addWidget(btn_history)
        menu_vertical_layout.addStretch()
        menu_frame.setLayout(menu_vertical_layout)
        menu_frame.setMinimumWidth(200)
        menu_frame.setMaximumHeight(200)


        parent_vertical=QVBoxLayout()
        vertical_1=QVBoxLayout()
        label_home=QLabel("Home")
        vertical_1.addWidget(label_home)

        vertical_2=QVBoxLayout()
        label_add_vehicle = QLabel("Add Vehicle")
        vertical_2.addWidget(label_add_vehicle)

        vertical_3=QVBoxLayout()
        label_manage = QLabel("Manage")
        vertical_3.addWidget(label_manage)

        vertical_4=QVBoxLayout()
        label_history = QLabel("History")
        vertical_4.addWidget(label_history)

        self.frame_1=QFrame()
        self.frame_1.setLayout(vertical_1)
        self.frame_2=QFrame()
        self.frame_2.setLayout(vertical_2)
        self.frame_3=QFrame()
        self.frame_3.setLayout(vertical_3)
        self.frame_4=QFrame()
        self.frame_4.setLayout(vertical_4)

        parent_vertical.addWidget(self.frame_1)
        parent_vertical.addWidget(self.frame_2)
        parent_vertical.addWidget(self.frame_3)
        parent_vertical.addWidget(self.frame_4)

        layout_horizontal.addWidget(menu_frame)
        layout_horizontal.addLayout(parent_vertical)
        parent_vertical.addStretch()
        menu_vertical_layout.addStretch()
        layout_horizontal.addStretch()
        widget.setLayout(layout_horizontal)

        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()

        self.setCentralWidget(widget)

    def showHome(self):
        self.frame_1.show()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()

    def showAdd(self):
        self.frame_1.hide()
        self.frame_2.show()
        self.frame_3.hide()
        self.frame_4.hide()

    def showManage(self):
        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.show()
        self.frame_4.hide()

    def showHistory(self):
        self.frame_1.hide()
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.show()