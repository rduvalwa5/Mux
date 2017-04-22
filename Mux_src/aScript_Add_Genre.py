'''
Created on Apr 21, 2017

@author: rduvalwa2
'''
from Music_Load import musicLoad_Functions
        
if __name__ == "__main__" :    
    genreLoad = musicLoad_Functions()
    genreList = ['Alternative','BlueGrass','Blues','Classic','Country','Folk','Holiday',\
                            'Jazz','Latino','Pop','Regae','Rock','RockaBilly','Soul','Talk', \
                            'TestGenre','TexMex','Traditional','World',"NewGenre"]
    genreLoad.set_genre_genre(genreList)
    