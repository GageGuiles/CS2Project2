from logic import *
from gui import *


def main():
    application = QApplication([])
    window = PasswordGeneratorApp()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()
