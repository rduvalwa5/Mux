'''
Created on Feb 27, 2018
@author: rduvalwa2
    def pay_song(self,path='',song=''):

        https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/afplay.1.html
        OSXAir:The Billie Holiday Story Volume II rduvalwa2$ afplay

        Audio File Play
        Version: 2.0
        Copyright 2003-2013, Apple Inc. All Rights Reserved.
        Specify -h (-help) for command options

        Usage:
        afplay [option...] audio_file

        Options: (may appear before or after arguments)
        {-v | --volume} VOLUME
        set the volume for playback of the file
        {-h | --help}
        print help
        { --leaks}
        run leaks analysis
        {-t | --time} TIME
        play for TIME seconds
        {-r | --rate} RATE
        play at playback rate
        {-q | --rQuality} QUALITY
        set the quality used for rate-scaled playback (default is 0 - low quality, 1 - high quality)
        {-d | --debug}
        debug print output
        
        OSXAir:The Billie Holiday Story Volume II rduvalwa2$ afplay "01 The Other Spring.mp3"
        OSXAir:The Billie Holiday Story Volume II rduvalwa2$ afplay -t 5 "01 The Other Spring.mp3"
        OSXAir:The Billie Holiday Story Volume II rduvalwa2$ afplay -t 15 "01 The Other Spring.mp3"
        OSXAir:The Billie Holiday Story Volume II rduvalwa2$ 
        '''
import os
        
class Play_Song:
    def play_song(self,songPath,song):
#        songPath = '/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Billie Holiday/The Best Of Billie Holiday/'
#        song = 'Body & Soul.mp3'
        self.aPath = songPath
        self.aSong = song
        print(self.aPath)
        self.songAndPath =   "\"" + self.aPath + self.aSong + "\"" 
        print("song path is ",self.songAndPath)
        self.comd = "afplay "  + self.songAndPath
        print("command is ",self.comd)
        os.system(self.comd)


if __name__  == '__main__':
    myPath = "/Users/rduvalwa2/Music/iTunes/iTunes Music/Music/Billie Holiday/The Best Of Billie Holiday/"
    mySong = "Body & Soul.mp3"
    x = Play_Song()
    x.play_song(myPath, mySong)