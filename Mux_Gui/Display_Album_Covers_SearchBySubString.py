'''
https://stackoverflow.com/questions/16539460/insert-a-jpg-in-a-canvas-with-tkinter-and-python-3-2
'''
import os, sys , platform
from tkinter import Tk, Canvas
from PIL import ImageTk, Image


class show_image():

    def create_Image(self,imagefile):
            root = Tk()
            canvas = Canvas(root, width=400, height=500)
            img = Image.open(imagefile)
            canvas.image = ImageTk.PhotoImage(img)
            canvas.create_image(0, 0, image= canvas.image, anchor='nw')
            canvas.pack()
            root.mainloop()            
            
    def create_array_images(self,con= ""):
            constraint = con
            print("Constraint is ", constraint)
            if platform.uname().node == 'OsxAir.hsd1.wa.comcast.net':
                base = "/Users/rduvalwa2/Code_Projects/eOxigen-workspace/Mux/AlbumCovers/"
            elif platform.uname().node == 'MaxBookPro17OSX.hsd1.wa.comcast.net':
                base = "/Users/rduvalwa2/git/Mux/AlbumCovers/"
            else:
                base =  '/Users/rduvalwa2/Code_Projects/eOxigen-workspace/Mux/AlbumCovers/'
            dirlist = os.listdir(base)
            images = []
            for f in dirlist:
                if f != '.DS_Store' and f != 'Thumbs.db':
                    if constraint == "":
                            images.append(base + f)
                    elif constraint != "":
                        if f.find(constraint) > -1:
#                            print("con find is ", f.find(constraint))
                            images.append(base + f)               
            return images


if __name__  == '__main__':
    '''
    https://www.tutorialspoint.com/python/python_command_line_arguments.htm
    http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/io.html
    '''
    im = show_image()
    img = input('Enter search string: ')
    
    CoverImages2 = im.create_array_images(img)
    for file in CoverImages2:
        print(file)
        im.create_Image(file)
        