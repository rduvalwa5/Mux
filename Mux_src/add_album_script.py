'''
Created on Mar 16, 2017

@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :    
    mux =  musicGet_Functions()
    print(mux.get_count('artist_albums', ''))
    albumList = [("Anthology Kenny Rogers & The First Edition","Kenny Rogers & The First Edition","Rock","Download")]
    for album in albumList:
        mux.add_album(album[0], album[1],album[2],album[3])
    print(mux.get_count('artist_albums', ''))
    

#    albumList = [("Seals & Crofts/Seals & Crofts Greatist Hits","Seals & Crofts","Rock","CD"),("Lost Treasures_ Rare & Unreleased","Herb Alpert & The Tijuana Brass","Alternative","CD"),("Joni Mitchell Hits","Joni Mitchell","Rock","CD")] 
#    albumList = [("Oh My Heart - Single","R.E.M.","Rock","Download"),("In Time - The Best of R.E.M. 1988-2003","R.E.M.","Rock","Download"),("Collapse Into Now","R.E.M.","Rock","CD")] 
#    albumList = [("Aladdin Sane","David Bowie","Rock","CD"),("Best of Bowie","David Bowie","Rock","Download"),("The Best of David Bowie 1980_1987","David Bowie","Rock","Download")] #,("In The Dark","The Grateful Dead","Rock","CD")]          
