from PyQt6.QtWidgets import *
from gui import *
import random
import string


class PasswordGeneratorApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_generate.clicked.connect(lambda: self.generate_password())

    def generate_password(self):
        try:
            self.cap_count = int(self.text_cap.toPlainText())
            self.sym_count = int(self.text_sym.toPlainText())
            self.num_count = int(self.text_num.toPlainText())
            self.total_count = self.cap_count + self.sym_count + self.num_count

            if self.total_count < 6:
                self.label_pass.setText(f'Password length must be > 6')
            elif self.total_count > 15:
                self.label_pass.setText(f'Password length must be < 15')
            else:
                positions = random.sample(range(self.total_count), self.cap_count + self.num_count + self.sym_count)

                password = ''
                for i in range(self.total_count):
                    if i in positions[:self.cap_count]:
                        password += random.choice(string.ascii_uppercase)
                    elif i in positions[self.cap_count:self.cap_count + self.num_count]:
                        password += random.choice(string.digits)
                    elif i in positions[self.cap_count + self.num_count:]:
                        password += random.choice(string.punctuation)
                    else:
                        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

                self.label_pass.setText(password)
        except:
            self.label_pass.setText("Inputs must be numeric")
