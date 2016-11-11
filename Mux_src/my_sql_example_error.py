'''
Created on Fixed Jan 27 2015
http://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
@author: rduvalwa2
'''

import unittest
import mysql.connector
from db_info import login_info
from db_info import login_info2

class TestPassword(unittest.TestCase):
    
    
    def test_OSError(self):
#        self.assertRaises(TimeoutError,Error,mysql.connector.Connect(**login_info2))
        try:
            mysql.connector.Connect(**login_info2)
            
        except OSError  as e:
            print(" e is ", str(e))

        except  mysql.connector.errors.InterfaceError as err:
            print(" err is ", str(err))
            self.assertTrue(err.errno == 2003)          
           
#            self.assertRaises(OSError,mysql.connector.Connect(**login_info2))
  
    def test_password_UnreadResultError(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select * from active_passwords where ap in ('password_db');"
        cursor.execute(statement)            
        try:
            cursor.close()
        except mysql.connector.Error as e:
            print("e ",e)
            self.assertEqual(str(e),"Unread result found.")
        db.close()  
        
    def test_password_badQueryError(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select * from active_passwords where apWrong in ('password_db');"
        try:
                cursor.execute(statement)
        except mysql.connector.errors.ProgrammingError as e:
                print("e ",e)
                self.assertEqual(str(e),"1054 (42S22): Unknown column 'apWrong' in 'where clause'")
        cursor.close()
        db.close()
    '''
        See # http://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
    '''        
    def test_password_badQueryError2(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        statement = "select * from active_passwords where apWrong in ('password_db');"
#        self.assertRaisesRegex(expected_exception, expected_regex, callable_obj)
#        self.assertRaises(self,Error, cursor.execute(statement))
# http://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
        try:
                cursor.execute(statement)
        except mysql.connector.Error as e:
                print("e2 ",e,"errno ", e.errno)
                self.assertEqual(str(e),"1054 (42S22): Unknown column 'apWrong' in 'where clause'")
                self.assertEqual(e.errno,1054)
        cursor.close()
        db.close()
        


if __name__ == "__main__":
    unittest.main()
    
    '''
     Finding files... done.
    Importing test modules ... done.
    
     err is  2003: Can't connect to MySQL server on '192.168.1.2:3306' (60 Operation timed out)
    e  Unread result found.
    e  1054 (42S22): Unknown column 'apWrong' in 'where clause'
    e2  1054 (42S22): Unknown column 'apWrong' in 'where clause' errno  1054
    ----------------------------------------------------------------------
    Ran 4 tests in 75.181s
    
    OK
    '''