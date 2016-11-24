'''
this file provides user info for login
@author: rduval
'''
USERNAME="rduvalwa2"
PASSWORD="blu4jazz"
#HOST="OSXAir.home.home"
HOST= "localhost"
DATABASE="Music"
PORT=3306

login_info = {
              'host': HOST,
              'user': USERNAME,
              'password': PASSWORD,
              'database': DATABASE,
              'port':PORT
              }


'''
On C1246895-J
CREATE USER 'rduvalwa2'@'C1246895-Air.ftrdhcpuser.net' IDENTIFIED BY 'reddog';

GRANT ALL ON password.* TO 'rduvalwa2'@'C1246895-Air.ftrdhcpuser.net';
commit;

select * from mysql.user;
'''

login_info2 = {
              'host': "localhost",
              'user': "root",
              'password': "blu4jazz",
              'database': "password",
              'port':"3306"
              }

login_info_xps = {
              'host': "c1246895-xps",
              'user': "rduvalwa2",
              'password': "blu4jazz",
              'database': "Music",
              'port':"3306"
              }