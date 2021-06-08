# SQL_Practice_Tool


## Introduction
This project aims to practice sql commend in Qt Interface with the human resource bank's data.

## Installment
First, install PyQt
```
sudo apt-get install qttools5-dev-tools
sudo apt-get install qttools5-dev
```
Then install Python package
```
pipenv install --dev
```
Install the Database, sqlite3
```
sudp apt install sqlte3
```

Turn the *.ui file to python file
```
pyuic5 Ui.ui -o Ui.py
```

## ER schema
![](https://i.imgur.com/Y81JZSN.png)
[link](https://drive.google.com/file/d/10KKWdZmozOKzuvoHM6rYbei583mMSkrI/view?usp=sharing)


## Function
* create table(default)
	* if the table not exist, then create the table
	> NOT EXISTS
* Input Data
	* Add all the data to database
	> INSERT
* Delete Data
	* Delete all the data
	> DELETE
* sql 
	* Execute the sql command
* job browse
	* Browse the job's information
		> SECECT-FROM-WHERE
* user_browse
	* Browse the user's information
* udpate_profile
	* Change the user's profile
	> UPDATE
* company_fileter
	* Use Salary for fileter the job & company
		> HAVING, COUNT, AVG
* company_profile
	* See the company information and the distrubtion of salary
	> MAX, MIN, AVG, SUM
* search_job
	* Search the job's name in multiple keywords
	> IN
* not_search_job
	* Search the job's name except the input keywords
	> NOT IN
* possible_company
	* Show the company's name which have provided job
	> EXISTS

## SQL Example

* test command
	```
	SELECT * FROM job
	```
* SELECT-FROM-WHERE
	* command
	```
	SELECT jid FROM job WHERE Job_Name='程式設計師'
	```
	* output
	```
	20190806150516_3662835 
	```
* DELETE
	* command
	```
	DELETE FROM job WHERE job_Name='程式設計師'
	```
* INSERT
	* command
	```
	INSERT INTO job (Jid, Job_Name, Salary, Cid ) VALUES ('20190806150516_3662835','程式設計師', 28000, '258709_22449566')

	```

* UPDATE
	* command
	```
	UPDATE job SET Salary = 0 WHERE Jid='20190709111058_6239461'
	```
* IN
	* command
	```
	SELECT * FROM job WHERE Job_Name IN ('程式設計師', '機構設計高級(資深)工程師')
	```
* NOT IN
	* command
	```
	SELECT * FROM job WHERE Job_Name NOT IN ('程式設計師', '機構設計高級(資深)工程師')
	```
* EXISTS
	* command
	```
	SELECT * FROM job WHERE EXISTS (SELECT * FROM job, Company WHERE job.Cid=Company.Cid)
	```
* NOT EXISTS
	* command
	```
	SELECT * FROM job WHERE NOT EXISTS (SELECT * FROM job, Company WHERE job.Cid=Company.Cid)
	```
* COUNT
	* command
	```
	SELECT Job_Name FROM job WHERE Salary=40000
	```
* SUM
	* command
	```
	SELECT SUM(Salary) FROM job WHERE Salary>20000
	```
* MAX
	* command
	```
	SELECT Max(Salary) FROM job WHERE Salary>20000
	```
* AVG
	* command
	```
	SELECT AVG(Salary) FROM job WHERE Cid='258709_22449566'

	```
	
* HAVING
	* command
	```
	SELECT CName, AVG(job.Salary) FROM job,company WHERE company.cid=job.cid GROUP BY job.cid HAVING AVG(Salary)>40000
	
	SELECT CName, Salary FROM company,job WHERE job.cid=company.cid GROUP BY job.cid HAVING MAX(job.Salary)
	```
## reference
[yes123](https://www.yes123.com.tw/admin/job_refer_comp_info.asp?p_id=258709_22449566)
[sql tutorial referece 1](https://www.fooish.com/sql/exists.html)
[sql tutorial referece 2](https://www.runoob.com/sqlite/sqlite-update.html)


job.salary

exist statement