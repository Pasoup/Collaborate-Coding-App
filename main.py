from include.pyside6Import import *
from classFiles.pages.authenPage import Authen



# -------------------- Run App --------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Authen()
    window.resize(600, 420)
    window.show()

    sys.exit(app.exec())