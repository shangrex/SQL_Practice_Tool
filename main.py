from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import Ui
import sys
import sqlite3

con = sqlite3.connect('human_resource.db')
cur = con.cursor()


# Create table
cur.execute('''CREATE TABLE job
               (Jid text, Job_Name text, Salary text, Cid text)''')

# Create table
cur.execute('''CREATE TABLE company
               (Cid text, Capital int, CName text)''')

# Create table
cur.execute('''CREATE TABLE employee
               (Eid text, Age int, Gender text)''')

# Create table
cur.execute('''CREATE TABLE resume
               (Eid text, Age int, Universiy text)''')

# Create table
cur.execute('''CREATE TABLE job
               (Jid text, Job_Name text, Salary text, Cid text)''')

# Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")



class ExampleApp(QtWidgets.QMainWindow, Ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Search_btn.clicked.connect(self.click_search_btn)



    def click_search_btn(self):
        print("click search btn")
        print(self.input_text.toPlainText())
        print(self.output_text.toPlainText())


        
def main():
    app = QApplication(sys.argv)
    form = ExampleApp()

    form.show()
    app.exec_()




if __name__ == '__main__':
    main()


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()