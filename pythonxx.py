import sys
import spotipy
import spotipy.util as util
import os


files = os.listdir("SpotifyPublicLibraries")
for file in files:
    print(file)
    if file[0] == '.':
        continue
    with open("SpotifyPublicLibraries/" + file) as f:
        songfile= "songs_" + file
        #print(songfile)
        with open(songfile,'w') as newFile:
            for line in f:
                artistName = line[5:38].strip()
                songName = line[38:].strip()
                d[artistName]=songName
                newFile.write(artistName + " : " + songName + "\n")
                    ##print(artistName, songName)##, file=newFile)



## python way to read through all names of text files in a folder
        ##files = listdir("SpotifyPublicLibraries")
            #for file in files:
            # with open (file) as f:




            ##move first with down
            ## songfile = "songs_" + file
            ##iterate through all files and create a new dictionary and name for newFile every time
            ## store in new folder
