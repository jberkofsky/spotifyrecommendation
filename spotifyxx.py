import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#Get the username from terminal
username = sys.argv[1]

#username = berkofskyj3

####export SPOTIPY_CLIENT_ID='902d7d740e6f4132b5d48e260dd6e305'
####export SPOTIPY_CLIENT_SECRET='53df201ca86a4a9e96c2a57f2dbea4d4'
####export SPOTIPY_REDIRECT_URI='https://google.com/'
####python3 spotifyxx.py berkofskyj3
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

#Create our spotifyObject

spotifyObject = spotipy.Spotify(auth=token)

user=spotifyObject.current_user()


displayName= user['display_name']
followers = user['followers']['total']

while True:
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    choice = input("Your choice: ")


    #search for an artist
    if choice == "0" :
        print("0")
        searchQuery = input("Ok, what's their name?: ")
        print()

        #Get search results
        searchResults = spotifyObject.search(searchQuery, 1, 0, "artist")
        #print(json.dumps(searchResults, sort_keys=True, indent=4))

        #artist details
        artist=searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers.")
        print(artist['genres'][0])
        print()
        #webbroswer.open(artist['images'][0]['url'])
        artistID= artist['id']
        

        #album and track details
        trackURIs = []
        trackArt=[]
        z=0

        #Extract ALbum data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults=albumResults['items']
        #print(json.dumps(albumResults, sort_keys=True, indent=4))
        print(len(albumResults))

        for item in albumResults:
            print("ALBUM: " + item['name'])
            albumID=item['id']
            albumArt=item['images'][0]['url']

            #Extract track data from each album
            trackResults=spotifyObject.album_tracks(albumID)
            trackResults=trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        #See album art...
            #video 7 online
            #songselection= input("Choose a song, x to exit: ")
            #if songselection == 'x':
               # break
            

            

        #end program
    if choice == "1":
        break

    
    




#print(json.dumps(VARIABLE, sort_keys=True, indent=4))


