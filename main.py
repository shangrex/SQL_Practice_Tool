from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import Ui
import sys
import sqlite3



class ExampleApp(QtWidgets.QMainWindow, Ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Search_btn.clicked.connect(self.click_search_btn)



    def click_search_btn(self):
        print("click search btn")
        print(self.input_text.toPlainText())


        
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()

    form.show()
    app.exec_()




if __name__ == '__main__':
    main()
