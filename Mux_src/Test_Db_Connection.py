'''
Created on Jan 25, 2018

@author: rduvalwa2
'''
'''
Created on Nov 10, 2016
This code is a Python port of a program that I wrote in Java in 2006
It attempts to find the music files on a server and put them into a data base.
@author: rduvalwa2

mysql -u root -b music -p
mysql -u rduvalwa2 -b music -p

'''
# from MusicFile import musicFile
import unittest
import pymysql


class TestMusicDb(unittest.TestCase):

      def test_connection_Artist_Albums_os_rduvalwa2_music_Albums_Rows(self):
 #       db = MySQLdb.connect(host='localhost', user='root', password='blu4jazz', db='Music')
#        conn = pymysql.connect(**login_info_osx)
        db = pymysql.connect(host='localhost', user='rduvalwa2', password='blu4jazz', db='Music')
        cursor = db.cursor()
        statement = "select count(*) from Music_Test.artist_albums;"
        expected = 1430
        try:
            cursor.execute(statement)
            row = cursor.fetchone()
            print("Row is " , row[0])
            self.assertEqual(row[0], expected)
            cursor.close()
            db.close()
        except db.Error as err:
                print("Exception is ", err)
#        db.close()

      def test_connection_Artist_Table_As_Root_localhost(self):
        db = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music')
        cursor = db.cursor()
        expected = 655
#        statement = "select uid from active_passwords where ap in ('password_db');"
        statement = "select count(*) from Music_Test.Artist;"
        try:
            cursor.execute(statement)
            row = cursor.fetchone()
            print("Row is " , row[0])     
            self.assertTrue(row[0] == expected)
            cursor.close()
        except db.Error as err:
            print("Exception is ", err)
#        db.close()
    
      def test_select_song_type_MusicSongs_By_Criteria(self):
        db = pymysql.connect(host='localhost', user='root', password='blu4jazz', db='Music')
        print(" test select song by type ********")
        cursor = db.cursor()
        expected = 'Maggie May.mp3'  # 'Kansas City.mp3'
        statement = 'select song from Music_Test.album2songs where album2songs.medium = \'tape\' and artist like \'Rod Stewart\';'
        try:
            cursor.execute(statement)
            rows = cursor.fetchall()
            print("Fetsted rows ******", rows)
            print("length ", len(rows))
            print("is this maggie may",rows[0])
            self.assertTrue(rows[0][0] == expected)
        except db.Error as err:
            print("Exception is ", err)
        
        
if __name__ == "__main__":
    unittest.main()
    
