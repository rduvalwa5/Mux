'''
Created on Feb 12, 2017

@author: rduvalwa2
'''

#from tkinter import *
import Music_GUI_Get_Album
import Music_GUI_Get_Song
import Music_GUI_Get_Artist
import Music_GUI_GetBy_Id

class musicGet_GUI:
        
    def get_input(self):
        print("Select MUSIC UI")
        print("1  Get ALbum")
        print("2  Get Song")
        print("3  Get Artist")
        print("4  Get By ID")  
        
        gui = input('Input UI: ')
        print("inpt is ", gui)
        if gui == "1":
            Music_GUI_Get_Album
             
        elif gui == "2":
            Music_GUI_Get_Song            
        elif gui == "3":
            Music_GUI_Get_Artist
        elif gui == "4":
            Music_GUI_GetBy_Id
        else:
            print("Invalid Input")
  
if __name__  == '__main__':
    musicGet_GUI.get_input(1)
    
    
    

