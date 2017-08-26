from rsa import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer, QSize

class QHLine(QFrame):
	    def __init__(self):
	        super(QHLine, self).__init__()
	        self.setFrameShape(QFrame.HLine)
	        self.setFrameShadow(QFrame.Sunken)

class View(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def generateSlot(self):
		p = int(self.p_spin.value())
		q = int(self.q_spin.value())

		print(p, q)
		public_key, private_key = generate_keys(p, q)
		self.public_key.setText(str(public_key))
		self.private_key.setText(str(private_key))

	def actionSlot(self):
		from ast import literal_eval
		action_type = self.action.currentIndex()
		msg = self.msg_text.toPlainText()

		if action_type == 0: #Encrypt
			public_key = self.public_key.text()
			public_key = literal_eval(public_key)

			new_msg = encrypt(msg, public_key)

		elif action_type == 1: #Decrypt
			private_key = self.private_key.text()
			private_key = literal_eval(private_key)

			new_msg = decrypt(msg, private_key)

		self.msg_text.setPlainText(new_msg)
	
	def initUI(self):
		self.setMinimumSize(QSize(300, 400))
		self.setMaximumSize(QSize(300, 400))
		self.setWindowTitle("RSA tools")

		self.p_spin = QSpinBox()
		self.q_spin = QSpinBox()
		self.public_key = QLineEdit()
		self.private_key = QLineEdit()
		self.msg_text = QTextEdit()
		self.keys_btn = QPushButton("Generate")
		self.msg_btn = QPushButton("Start")
		self.prepare_btn = QPushButton("Prepare")
		self.unprepare_btn = QPushButton("UnPrepare")
		self.action = QComboBox()

		self.action.addItem("Encrypt")
		self.action.addItem("Decrypt")

		self.p_spin.setMinimum(2)
		self.q_spin.setMinimum(2)
		self.p_spin.setMaximum(1e4)
		self.q_spin.setMaximum(1e4)

		self.keys_btn.clicked.connect(self.generateSlot)
		self.msg_btn.clicked.connect(self.actionSlot)

		h_box1 = QHBoxLayout()
		h_box1.addWidget(QLabel("Set value for P: "))
		h_box1.addStretch(1)
		h_box1.addWidget(self.p_spin)

		h_box2 = QHBoxLayout()
		h_box2.addWidget(QLabel("Set value for Q: "))
		h_box2.addStretch(1)
		h_box2.addWidget(self.q_spin)

		h_box3 = QHBoxLayout()
		h_box3.addStretch(1)
		h_box3.addWidget(self.keys_btn)

		h_box4 = QHBoxLayout()
		h_box4.addWidget(QLabel("Public key: "))
		h_box4.addWidget(self.public_key)

		h_box5 = QHBoxLayout()
		h_box5.addWidget(QLabel("Private key: "))
		h_box5.addWidget(self.private_key)

		h_box6 = QHBoxLayout()
		h_box6.addWidget(QLabel("Action: "))
		h_box6.addWidget(self.action)

		h_box7 = QHBoxLayout()
		h_box7.addStretch(1)
		h_box7.addWidget(self.msg_btn)

		vbox = QVBoxLayout()

		vbox.addLayout(h_box1)
		vbox.addLayout(h_box2)
		vbox.addLayout(h_box3)

		vbox.addWidget(QHLine())

		vbox.addLayout(h_box4)
		vbox.addLayout(h_box5)

		vbox.addWidget(QHLine())

		vbox.addLayout(h_box6)
		
		vbox.addWidget(QLabel("Message:"))
		vbox.addWidget(self.msg_text)
		vbox.addLayout(h_box7)

		self.setLayout(vbox)
		self.show()

app = QApplication([])
view = View()
app.exec()