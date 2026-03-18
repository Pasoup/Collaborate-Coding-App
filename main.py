import sys
from PySide6.QtWidgets import QApplication, QWidget
import requests
from output import Ui_Form 

url = "https://collaborate-coding-app.onrender.com"

class MyWorkshopApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.MainPages.setCurrentIndex(0)
        
        self.ui.loginRegisterBtn.clicked.connect(self.changeToRegister)
        self.ui.registerLoginBtn.clicked.connect(self.changeToLogin)

        self.ui.registerConfirmBtn.clicked.connect(self.register)
        self.ui.loginConfirmBtn.clicked.connect(self.login)
    def changeToRegister(self):
        self.ui.MainPages.setCurrentIndex(1)

    def changeToLogin(self):
        self.ui.MainPages.setCurrentIndex(0)

    def register(self):
        username = self.ui.registerUsername.toPlainText().strip()
        passwrod = self.ui.registerPassword.toPlainText().strip()
        confirm_password = self.ui.registerConfirmPassword.toPlainText().strip()
        print(f"DEBUG: Comparing '{passwrod}' with '{confirm_password}'")
        if passwrod != confirm_password:
            print("Passsword not the same")
            return

        try:
            url = "https://collaborate-coding-app.onrender.com/register"
            response = requests.post(url, json={"username": username, "password": passwrod})

            if response.status_code == 200:
                print("Register sucessful!")
                self.changeToLogin()
            else:
                print("Register failed!")
        except Exception as e:
            print("could not connect to server")
    
    def login(self):
        username = self.ui.loginUsername.toPlainText().strip()
        password = self.ui.loginPassword.toPlainText().strip()
        try:
            url = "https://collaborate-coding-app.onrender.com/login"
            response = requests.post(url, json={"username": username, "password": password})
            if response.status_code == 200:
                print(f"Login sucess for , {username}!")
                self.ui.MainPages.setCurrentIndex(2) 
                self.ui.homeUserName.setText(f"{username}'s Dashboard") 
            else:
                print("Login failed")
        except Exception as e:
            print("could not connect to server")



if __name__ == "__main__":
   
    app = QApplication(sys.argv)    
    window = MyWorkshopApp()
    window.show()
    sys.exit(app.exec())