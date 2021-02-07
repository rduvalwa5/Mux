'''
Created on Feb 4, 2021

@author: rduvalwa2
'''

import csv, sys
import shutil, os

albumCoversDir = '/Users/rduvalwa2/Code_Projects/eOxigen-workspace/Mux/AlbumCovers/'
CoverBackupDir = '/Users/rduvalwa2/Code_Projects/Album_Cover_Backup/'
filename = '/Users/rduvalwa2/Code_Projects/Album_Cover_Backup/Not_In_Db_Covers.csv'

with open(filename, newline='') as f:
    reader = csv.reader(f)
    
    try:
        rowCount = 0
        for f2 in reader:
#            if rowCount > 0:
                file = albumCoversDir + f2[0]
                print(file)
 #               files = ['file1.txt', 'file2.txt', 'file3.txt']
#                for f in files:
                shutil.move(file, CoverBackupDir)
#            rowCount = rowCount + 1
#            print(rowCount)
    except csv.Error as e:
        sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))