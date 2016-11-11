'''
Created on Fixed Jan 27 2015
http://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
@author: rduvalwa2
'''

import unittest
import mysql.connector
from db_info import login_info
from db_info import login_info2
from mysql.connector.errors import Error

class TestPassword(unittest.TestCase):
    
    
    def test_password_rows(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from active_passwords;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 50)
        cursor.close()
        db.close()

    def test_password_rowsJ(self):
        db = mysql.connector.Connect(**login_info2)
        cursor = db.cursor()
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from active_passwords;"
        cursor.execute(statement)
        row = cursor.fetchone()
        print("Row is " ,row[0])
        self.assertTrue(row[0] == 50)
        cursor.close()
        db.close()

'''        
    def test_password_values(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select * from active_passwords where ap in ('password_db');"
        cursor.execute(statement)
        row2 = cursor.fetchone()
        print("AP is " ,row2[0] , "UID" , row2[1], "pwd " , row2[2] )
        self.assertTrue(row2[0] == "password_db")
        self.assertTrue(row2[1] == "rduval")
        self.assertTrue(row2[2] == "reddog")
        cursor.close()
        db.close()

    def test_password_reslt(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select * from active_passwords where ap in ('password_db');"
        cursor.execute(statement)
        row2 = cursor.fetchone()
        print("AP is " ,row2[0] , "UID" , row2[1], "pwd " , row2[2] )
        self.assertTrue(row2[0] == "password_db")
        self.assertTrue(row2[1] == "rduval")
        self.assertTrue(row2[2] == "reddog")
        cursor.close()
        db.close()
        
    def test_password_columns(self):
        columns = ["ap","uid","pwd"]
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select * from active_passwords where ap in ('password_db');"
        cursor.execute(statement)
        row2 = cursor.fetchone()
        sequence = cursor.column_names
        for i in sequence:
            print(i)
            self.assertTrue(i in columns)
        cursor.close()
        db.close()       
  '''


if __name__ == "__main__":
    unittest.main()
    
    '''
    Finding files... done.
    Importing test modules ... done.
    
    ap
    uid
    pwd
    AP is  password_db UID rduval pwd  reddog
    Row is  40

    '''