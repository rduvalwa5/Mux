'''
Created on Mar 16, 2017

@author: rduvalwa2
'''

from Music_Get_Functions import musicGet_Functions
        
if __name__ == "__main__" :    
    mux =  musicGet_Functions()
    print(mux.get_count('artist_albums', ''))
#    albumList = [("Anthology Kenny Rogers & The First Edition","Kenny Rogers & The First Edition","Rock","Download")]
    albumList = [('Saint-Saens_ Danse Macabre', 'Charles Dutoit','Classic', 'Download') \
,('Chicago Live In Japan [Disc 1]','Chicago', 'Rock', 'CD') \
,('Masked & Anonymous','Various Artist', 'Mixed', 'CD') \
,('Strawberry Letter 23_ The Very Best of the Brothers Johnson','The Brothers Johnson','rock', 'Download') \
,('The Anthology','Chuck Berry' ,'Rock', 'Download') \
,('Hold Tight! - Single','Dave Dee, Dozy, Beaky, Mick & Tich' ,'Rock', 'Download') \
,("Surfers' Choice",'Dick Dale & His Del-Tones','Rock', 'Download')
,('Hollands Glorie','George Baker' ,'Rock', 'Download')
,('Wrote a Song for Everyone','John Fogerty','Rock', 'Download')
,('Live at the Cafe au-Go-Go (and Soledad Prison)','John Lee Hooker', 'Rock', 'Download')
,('Corazon (Deluxe Version)','Santana','TexMex', 'Download')
,('Seals & Crofts Greatist Hits','Seals & Crofts', 'Rock', 'CD')
,('Bomb the Twist - EP',"The 5.6.7.8's", 'Rock', 'Download')
,('The Beatles Songs Pictures And Stories','The Beatles','Rock', 'Vinyl')
,("The Beatles' Second Album",'The Beatles','Rock', 'Vinyl')
,('Bullwinkle Part II','The Centurions','Rock', 'Download')
,('Sounds of Tarantino','The Centurions' ,'Rock', 'Download')
,('Over Under Sideways Down _ Roger the Engineer (Remastered)','The Yardbirds','Rock', 'Download')
,('Test_Album1', 'Test', 'Test','Test')
,('Test_Album2', 'Test', 'Test','Test')]
    for album in albumList:
        mux.add_album(album[0], album[1],album[2],album[3])
    print(mux.get_count('artist_albums', ''))
    

#    albumList = [("Seals & Crofts/Seals & Crofts Greatist Hits","Seals & Crofts","Rock","CD"),("Lost Treasures_ Rare & Unreleased","Herb Alpert & The Tijuana Brass","Alternative","CD"),("Joni Mitchell Hits","Joni Mitchell","Rock","CD")] 
#    albumList = [("Oh My Heart - Single","R.E.M.","Rock","Download"),("In Time - The Best of R.E.M. 1988-2003","R.E.M.","Rock","Download"),("Collapse Into Now","R.E.M.","Rock","CD")] 
#    albumList = [("Aladdin Sane","David Bowie","Rock","CD"),("Best of Bowie","David Bowie","Rock","Download"),("The Best of David Bowie 1980_1987","David Bowie","Rock","Download")] #,("In The Dark","The Grateful Dead","Rock","CD")]          
