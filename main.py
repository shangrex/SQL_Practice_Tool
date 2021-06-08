from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import Ui
import sys
import sqlite3
import pandas as pd

con = sqlite3.connect('human_resource.db')
cur = con.cursor()
print("hello")
# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS job
               (Jid text PRIMARY KEY, Job_Name text, Salary int, Cid text)''')

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

        self.function = ['sql', 'job_browse', 'user_browse', 'update_profile', 'company_fileter', 'company_profile', 'search_job', 'not_search_job', 'possible_company']
        self.mode = 0
        self.comboBox.addItems(self.function)
        self.comboBox.currentIndexChanged.connect(self.f_mode)
    
    def f_mode(self):
        self.mode = self.comboBox.currentIndex()


    def click_search_btn(self):
        print(f"click search btn {self.function[self.mode]}")
        print(self.input_text.toPlainText())
        print(self.output_text.toPlainText())
        try:
            if self.mode == 0:
                tmp = cur.execute(self.input_text.toPlainText())
                tmp_s = ""
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)
            if self.mode == 1:
                tmp = cur.execute('SELECT * FROM job,company WHERE job.cid=company.cid')
                tmp_s = "Job id, Job Name, Salary, Company id, company id, capital, company name \n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)
            if self.mode == 2:
                tmp = cur.execute('SELECT * FROM employee')
                tmp_s = "Name, Age, Gender\n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)
            if self.mode == 3:
                txt = self.input_text.toPlainText()
                txt = txt.split(' ')
                txt_id = txt[0]
                txt_age = txt[1]
                txt_gen = txt[2]
                tmp = cur.execute('UPDATE employee SET Age=? WHERE Eid=?', (txt_age, txt_id))
                tmp = cur.execute('UPDATE employee SET Gender=? WHERE Eid=?', (txt_gen, txt_id))
                tmp = cur.execute('SELECT * FROM employee')
                tmp_s = "Name, Age, Gender\n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)
            if self.mode == 4:
                txt = self.input_text.toPlainText()
                txt = txt.split(' ')
                txt_sal = txt[0]
                tmp = cur.execute('SELECT CName, AVG(job.Salary), COUNT(job.jid) FROM job,company WHERE company.cid=job.cid GROUP BY job.cid HAVING AVG(Salary)>(?)', [int(txt_sal)])
                tmp_s = "company name  , average salary, count company\n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)  
            if self.mode == 5:
                txt = self.input_text.toPlainText()
                txt = txt.split(' ')
                txt_cname = txt[0]
                tmp_s = "Max Salary\n"
                tmp = cur.execute('SELECT Max(Salary) FROM job,company WHERE job.cid=company.cid AND company.CName=(?)', [txt_cname])
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                tmp = cur.execute('SELECT Min(Salary) FROM job,company WHERE job.cid=company.cid AND company.CName=(?)', [txt_cname])
                tmp_s += "Min Salary\n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                tmp = cur.execute('SELECT Sum(Salary) FROM job,company WHERE job.cid=company.cid AND company.CName=(?)', [txt_cname])
                tmp_s += "Sum Salary\n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                tmp = cur.execute('SELECT AVG(Salary) FROM job,company WHERE job.cid=company.cid AND company.CName=(?)', [txt_cname])
                tmp_s += "AVG Salary\n"
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)  
            if self.mode == 6:
                txt = self.input_text.toPlainText()
                txt = txt.split(' ')
                tmp = ""
                for i in txt:
                    tmp += '\'' + i + '\','
                tmp_s = "Job id, Job Name, Salary, company id\n"
                tmp = tmp[:-1]
                query = "SELECT * FROM job WHERE Job_Name IN ({})".format(tmp)
                tmp = cur.execute(query)
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)  
            if self.mode == 7:
                txt = self.input_text.toPlainText()
                txt = txt.split(' ')
                tmp = ""
                for i in txt:
                    tmp += '\'' + i + '\','
                tmp_s = "Search\n"
                tmp = tmp[:-1]
                query = "SELECT * FROM job WHERE Job_Name NOT IN ({})".format(tmp)
                tmp = cur.execute(query)
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
                    tmp_s += '\n'
                self.output_text.setPlainText(tmp_s)  
            if self.mode == 8:
                tmp_s = ""
                query = "SELECT CName FROM company WHERE EXISTS (SELECT * FROM job WHERE job.cid=company.cid)"
                tmp = cur.execute(query)
                for i in tmp:
                    for j in i:
                        tmp_s += str(j) + ' '
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
            cur.execute("INSERT INTO job VALUES (?, ?, ?, ?)", (job_data.iloc[i][0], job_data.iloc[i][1], int(job_data.iloc[i][2]), job_data.iloc[i][3]))

        employee_data = pd.read_csv('data/employee.csv')
        for i in range(len(employee_data)):
            cur.execute("INSERT INTO employee VALUES (?, ?, ?)", (employee_data.iloc[i][0], int(employee_data.iloc[i][1]), employee_data.iloc[i][2]))
    
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