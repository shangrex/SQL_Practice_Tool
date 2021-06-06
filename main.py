from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import Ui
import sys
import sqlite3
import pandas as pd

con = sqlite3.connect('human_resource.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS job
               (Jid text PRIMARY KEY, Job_Name text, Salary text, Cid text)''')

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS  company
               (Cid text PRIMARY KEY, Capital int, CName text)''')

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS  employee
               (Eid text PRIMARY KEY, Age int, Gender text)''')

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS  resume
               (Eid text PRIMARY KEY, Age int, Universiy text)''')

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS  hr
               (Hid text PRIMARY KEY, Phone text, Email text)''')

# Insert a row of data
# cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")



class ExampleApp(QtWidgets.QMainWindow, Ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.Search_btn.clicked.connect(self.click_search_btn)
        self.Input_btn.clicked.connect(self.click_input_btn)
        self.Delete_btn.clicked.connect(self.click_delete_btn)


    def click_search_btn(self):
        print("click search btn")
        print(self.input_text.toPlainText())
        print(self.output_text.toPlainText())
        try:
            tmp = cur.execute(self.input_text.toPlainText())
            tmp_s = ""
            for i in tmp:
                for j in i:
                    tmp_s += j + ' '
                tmp_s += '\n'
            self.output_text.setPlainText(tmp_s)
            
        except Exception as e:
            print(e)


    def click_input_btn(self):
        '''
        Input all the Data from data folder
        '''
        job_data = pd.read_csv('data/job.csv')
        for i in range(len(job_data)):
            cur.execute("INSERT INTO job VALUES (?, ?, ?, ?)", job_data.iloc[i])

        employee_data = pd.read_csv('data/employee.csv')
        for i in range(len(employee_data)):
            cur.execute("INSERT INTO employee VALUES (?, ?, ?)", employee_data.iloc[i])
    
        hr_data = pd.read_csv('data/hr.csv')
        for i in range(len(hr_data)):
            cur.execute("INSERT INTO hr VALUES (?, ?, ?)", hr_data.iloc[i])
    
        company_data = pd.read_csv('data/company.csv')
        for i in range(len(company_data)):
            cur.execute("INSERT INTO company VALUES (?, ?, ?)", company_data.iloc[i])

        resume_data = pd.read_csv('data/resume.csv')
        for i in range(len(resume_data)):
            cur.execute("INSERT INTO resume VALUES (?, ?, ?)", resume_data.iloc[i])
    

    def click_delete_btn(self):
        '''
        Delete all the Data from data folder
        '''
        print("deleting all data")
        cur.execute('DELETE FROM job')
        cur.execute('DELETE FROM company')
        cur.execute('DELETE FROM employee')
        cur.execute('DELETE FROM hr')
        cur.execute('DELETE FROM resume')

    def dump_data(self):
        '''
        Dump all the data to output
        '''
        print("dump all")
        tmp = ""
        for i in cur.execute('SELECT * FROM job'):
            tmp += 'Jid,Job_Name,Salary,Cid\n'
            for j in i:
                tmp += j+','
            tmp += '\n'

        self.output_text.setPlainText(tmp)

        
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