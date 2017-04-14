'''
Created on Feb 12, 2017

@author: rduvalwa2
'''
package
#from tkinter import *
#import Music_GUI_Get_Album
#import Music_GUI_Get_Song
#import Music_GUI_Get_Artist
#import Music_GUI_GetBy_Id

class musicGet_GUI:
        
    def get_input(self):
        print("Select MUSIC UI")
        print("1  Get ALbum")
        print("2  Get Song")
        print("3  Get Artist")
        print("4  Get By ID")
        print("Q to Quit")
        gui = ''
        print(gui)
        gui = input('Input UI: ')
        print("inpt is ", gui)
        if gui == "1":
            print("Music_GUI_Get_Album")
            Music_GUI_Get_Album             
        elif gui == "2":
            print("Music_GUI_Get_Song ")
            Music_GUI_Get_Song            
        elif gui == "3":
            print("Music_GUI_Get_Artist")
            Music_GUI_Get_Artist
        elif gui == "4":
            print("Music_GUI_GetBy_Id")
            Music_GUI_GetBy_Id
        elif gui == "Q":
            print("Quit")
            exit
        else:
            print("Invalid Input")
            exit
        gui = input('Input UI: ')
        
if __name__  == '__main__':
    musicGet_GUI.get_input(1)
    
    
    

