# RAAI-smart edit UI Flow - PyQt6 Structure
# Files: main.py, splash_screen.py, login_window.py, dashboard.py, assets/RAAI.png

# --- main.py ---
import sys
from PyQt6.QtWidgets import QApplication
from splash_screen import SplashScreen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    sys.exit(app.exec())


# --- splash_screen.py ---
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QRect
from login_window import LoginWindow

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: black;")
        self.logo = QLabel(self)
        pixmap = QPixmap("assets/RAAI.png").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo.setGeometry(200, 250, 200, 200)

        self.anim = QPropertyAnimation(self.logo, b"geometry")
        self.anim.setDuration(1000)
        self.anim.setStartValue(QRect(200, 250, 200, 200))
        self.anim.setEndValue(QRect(200, 100, 200, 200))
        self.anim.start()

        QTimer.singleShot(3000, self.show_login)

    def show_login(self):
        self.close()
        self.login = LoginWindow()
        self.login.show()


# --- login_window.py ---
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from signup_window import SignupWindow
from forgot_password import ForgotPasswordWindow
from dashboard import Dashboard

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAAI-smart edit - Login")
        self.setFixedSize(400, 350)

        widget = QWidget()
        layout = QVBoxLayout()

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.toggle_password = QPushButton("Show Password")
        self.toggle_password.setCheckable(True)
        self.toggle_password.toggled.connect(self.toggle_password_visibility)

        self.forgot_btn = QPushButton("Forgot Password?")
        self.forgot_btn.clicked.connect(self.open_forgot_password)

        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.login)

        self.signup_btn = QPushButton("New User? Sign Up")
        self.signup_btn.clicked.connect(self.open_signup)

        layout.addWidget(QLabel("Welcome to RAAI-smart edit!"))
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(self.toggle_password)
        layout.addWidget(self.forgot_btn)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.signup_btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def toggle_password_visibility(self, checked):
        self.password.setEchoMode(QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password)
        self.toggle_password.setText("Hide Password" if checked else "Show Password")

    def open_signup(self):
        self.signup = SignupWindow()
        self.signup.show()
        self.close()

    def open_forgot_password(self):
        self.forgot = ForgotPasswordWindow()
        self.forgot.show()
        self.close()

    def login(self):
        # Placeholder login
        if self.email.text() == "admin" and self.password.text() == "admin":
            self.dashboard = Dashboard()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid credentials")


# --- signup_window.py ---
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from dashboard import Dashboard

class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAAI-smart edit - Sign Up")
        self.setFixedSize(400, 400)

        widget = QWidget()
        layout = QVBoxLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("Full Name")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.age = QLineEdit()
        self.age.setPlaceholderText("Age")

        self.address = QLineEdit()
        self.address.setPlaceholderText("Address")

        self.signup_btn = QPushButton("Sign Up")
        self.signup_btn.clicked.connect(self.signup)

        layout.addWidget(QLabel("Create your account"))
        layout.addWidget(self.name)
        layout.addWidget(self.email)
        layout.addWidget(self.age)
        layout.addWidget(self.address)
        layout.addWidget(self.signup_btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def signup(self):
        self.dashboard = Dashboard()
        self.dashboard.show()
        self.close()


# --- forgot_password.py ---
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from dashboard import Dashboard

class ForgotPasswordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAAI-smart edit - Forgot Password")
        self.setFixedSize(400, 250)

        widget = QWidget()
        layout = QVBoxLayout()

        self.email = QLineEdit()
        self.email.setPlaceholderText("Enter your registered email")

        self.otp = QLineEdit()
        self.otp.setPlaceholderText("Enter OTP")

        self.get_otp_btn = QPushButton("Get OTP")
        self.login_btn = QPushButton("Login with OTP")
        self.login_btn.clicked.connect(self.login_with_otp)

        layout.addWidget(QLabel("Reset your password using OTP"))
        layout.addWidget(self.email)
        layout.addWidget(self.get_otp_btn)
        layout.addWidget(self.otp)
        layout.addWidget(self.login_btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def login_with_otp(self):
        # Simulate OTP validation
        if self.otp.text() == "1234":
            self.dashboard = Dashboard()
            self.dashboard.show()
            self.close()
        else:
            QMessageBox.warning(self, "Invalid OTP", "The OTP entered is incorrect")


# --- dashboard.py ---
from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAAI-smart edit - Dashboard")
        self.setFixedSize(500, 400)

        widget = QWidget()
        layout = QVBoxLayout()

        manual_btn = QPushButton("Manual Editing")
        manual_btn.setIcon(QIcon("assets/scissors.png"))
        manual_btn.setIconSize(QSize(40, 40))

        ai_btn = QPushButton("AI Editing")
        ai_btn.setIcon(QIcon("assets/ai.png"))
        ai_btn.setIconSize(QSize(40, 40))

        layout.addWidget(QLabel("Select an editing mode:"))
        layout.addWidget(manual_btn)
        layout.addWidget(ai_btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)
