from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QButtonGroup
import sys


Ui_MainWindow, QtBaseClass = uic.loadUiType(r"INSERT YOUR ABSOLUTE PATH HERE")


class CaeserCipherDecipherEncipher(QMainWindow):
    def __init__(self):
        super(CaeserCipherDecipherEncipher, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                     "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.ui.EncryptButton.clicked.connect(self.encrypt)
        self.ui.DecryptButton.clicked.connect(self.decrypt)
        self.text = None
        self.shifts = None
        
    def handle_error(self, to_encrypt):
        textsectionname = "plain text section" if to_encrypt == True else "caeser text section"
        if self.text == "" and (self.shifts == "" or self.shifts.isdigit() == False):
            self.ui.ErrorBox.setPlainText(f"Please enter a number a valid number of shifts and text in the {textsectionname}")
            return True
        elif self.text == "":
            self.ui.ErrorBox.setPlainText("Please enter text in the plain text section")
            return True
        elif self.shifts == "":
            self.ui.ErrorBox.setPlainText("Please enter number of shifts")
            return True
        elif self.shifts.isdigit() == False:
            self.ui.ErrorBox.setPlainText("Please enter a valid number of shifts")
            return True
        return False
        
    def get_list_of_indexes_upper_and_lower(self, string):
        list_indexes = []
        for i in range(len(string)):
            list_indexes.append(string[i].isupper())
        return list_indexes

    def convert_string_to_encoded_list(self, string):
        encoded_list = []
        for i in range(len(string)):
            if string[i].lower() in self.alphabet_list:
                index = self.alphabet_list.index(string[i].lower())
                encoded_list.append(index)
            else:
                encoded_list.append(string[i])
        return encoded_list

    def add_shift(self, encodedlist, shift):
        for i in range(len(encodedlist)):
            if type(encodedlist[i]) == int:
                encodedlist[i] = int(encodedlist[i])
                encodedlist[i] += shift 
                encodedlist[i] = encodedlist[i] % 26 
        return encodedlist

    def convert_shifted_list_to_string(self, shifted_list, list_indexes):
        string = ""
        for i in range(len(shifted_list)):
            if type(shifted_list[i]) == int:
                letter = self.alphabet_list[shifted_list[i]]
                if list_indexes[i] == True:
                    letter = letter.upper()
                string += letter
            else:
                string += shifted_list[i]
        return string

    def to_cipher(self, string, shift):
        upper_case_indexes = self.get_list_of_indexes_upper_and_lower(string)
        encoded_list = self.convert_string_to_encoded_list(string)
        shifted_list = self.add_shift(encoded_list, shift)
        cipher = self.convert_shifted_list_to_string(shifted_list, upper_case_indexes)
        return cipher

    def decipher(self, string, shift):
        shift = 0 - shift
        upper_case_indexes = self.get_list_of_indexes_upper_and_lower(string)
        encoded_list = self.convert_string_to_encoded_list(string)
        shifted_list = self.add_shift(encoded_list, shift)
        decrypted_cipher = self.convert_shifted_list_to_string(shifted_list, upper_case_indexes)
        return decrypted_cipher

    def encrypt(self):
        self.ui.CipherBox.setPlainText("")
        self.text = self.ui.PlainTextBox.toPlainText()
        self.shifts = self.ui.ShiftsBox.toPlainText()
        has_errors = self.handle_error(True)
        if has_errors == False:
            self.shifts = int(self.shifts)
            encryption = self.to_cipher(self.text, self.shifts)
            self.ui.ErrorBox.setPlainText("")
            self.ui.CipherBox.setPlainText(encryption)
            
    def decrypt(self):
        self.ui.PlainTextBox.setPlainText("")
        self.text = self.ui.CipherBox.toPlainText()
        self.shifts = self.ui.ShiftsBox.toPlainText()
        has_errors = self.handle_error(False)
        if has_errors == False:
            self.shifts = int(self.shifts)
            decryption = self.decipher(self.text, self.shifts)
            self.ui.ErrorBox.setPlainText("")
            self.ui.PlainTextBox.setPlainText(decryption)



if __name__ == "__main__":
    caesar_app = QApplication(sys.argv)
    caesarwindow = CaeserCipherDecipherEncipher()
    caesarwindow.show()
    caesar_app.exec_()

    
