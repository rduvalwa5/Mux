'''
OUPDATED Feb 27 2018
this file provides user info for login
@author: rduval
'''

# self.conn = MySQLdb.connect(host='OSXAir.home', user='rduval', password='blu4jazz', db='Music')

login_info_default = {'host':'localhost','user': 'root','password': 'blu4jazz','db': 'Music'}

login_info_osxAir = {'host':'osxair.home.home','user': 'rduvalwa2','password': 'blu4jazz','db': 'Music'}

login_info_xps = {'host':'localhost','user': 'root','password': 'blu4jazz','db': 'Music'}

login_info_WIN64_Air = {'host':'osxair.home.home','user': 'rduvalwa2','password': 'blu4jazz','db': 'Music'}

login_info_osx = {'host': 'localhost', 'user': 'root', 'password': 'blu4jazz', 'db': 'Music'}

#for k,v in login_info_osx.items():
#    print(k,v)
    
#print("host is ", login_info_osx['host'])

'''
    >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    >>> for k, v in knights.items():
    ...     print(k, v)
    ...
    gallahad the pure
    robin the brave
'''