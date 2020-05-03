import spotipy
import os
import json
import pprint
from youtube_search import YoutubeSearch
import youtube_dl
import eyed3
from urllib.request import urlopen
import os.path
import click
from spotipy.oauth2 import SpotifyClientCredentials
from art import *

Art = text2art("SpotifyToMP3")
print(Art)



class Song:
    def __init__(self, sname, sartist, coverart, albname, albartist, spotid):
        self.sname = sname
        self.sartist = sartist
        self.coverart = coverart
        self.albname = albname
        self.albartist = albartist
        self.spotid = spotid
    
    def encode(self):
        return self.__dict__
    


def createDict(tdict):
    tracklist = []
    for i in tdict:
        track = i['track']
        album = track['album']
        albumname = album["name"] ##album name 
        albartists = []
        for i in album["artists"]:
            albartists.append(i["name"]) ##album artists
        albimgs = album["images"]
        try:
            albimgt = albimgs[0]
            albimg = albimgt["url"] ## coverart
        
        except:
            albimg = "https://image.shutterstock.com/image-photo/concert-hall-lit-stage-people-600w-1043460649.jpg"
        
        songname = track["name"] ##songname
        spotid = track["id"] ##spotify id
        artistlist = []
        
        for i in track["artists"]:
            artistlist.append(i["name"]) ##song artists
        newsong = Song(songname, artistlist, albimg, albumname, albartists, spotid)
        tracklist.append(newsong)
    return tracklist
    ## jsontracks = json.dumps(tracklist, default=lambda o: o.encode(), indent=4)


def downloader(url, name):
    ydl_opts = {
        'outtmpl': '',
        'format': 'm4a',
    }
    ydl_opts['outtmpl']= name + ".%(ext)s"
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    

def convertor(name):
    os.system('ftransc -r -q insane -f mp3 '+'"'+name+'.m4a'+'"')
    

def tagger(songdata, file):

    songname = songdata.sname

    songartlist = songdata.sartist
    songartstr = ', '.join(songartlist)

    albumname = songdata.albname

    albartlist = songdata.albartist
    albartstr = ', '.join(albartlist)

    coverarturl = songdata.coverart
    
    audiofile = eyed3.load(file)

    audiofile.tag.artist = songartstr
    audiofile.tag.album = albumname
    audiofile.tag.album_artist = albartstr
    audiofile.tag.title = songname

    response = urlopen(coverarturl)
    imagedata = response.read()

    audiofile.tag.images.remove(u'')
    audiofile.tag.images.set(3, imagedata , "image/jpeg" ,u"Description")

    audiofile.tag.save()


def youtubelink(song, artist):
    i = song +" by "+ artist
    try:
        searchresults = YoutubeSearch(i+" audio" , max_results=1).to_dict()
        searchresult = searchresults[0]
        searchid = searchresult['id']
        if searchid[0] == "-":
           searchid = searchid[1:]
    except:
        searchresults = YoutubeSearch(i+" audio" , max_results=1).to_dict()
        searchresult = searchresults[0]
        searchid = searchresult['id']
        if searchid[0] == "-":
           searchid = searchid[1:]
    return searchid


def songexists(song):
    if os.path.isfile(song+".mp3"):
        return True
    else:
        return False



@click.command()
@click.option('--username', prompt='Your username',
              help='your spotify username')
@click.option('--playlist', prompt='Your public spotify playlist',
              help='The public playlist you want to download')

def run(username, playlist):
    client_credentials_manager = SpotifyClientCredentials(client_id='',
                                                      client_secret='')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    pp = pprint.PrettyPrinter(indent=4)

    usr = username
    if usr[0] == "@":
        usr = usr[1:]



    user = sp.user(usr)

    playlists = sp.user_playlists(usr)

    n = playlists['items']

    usrpl = playlist
    for i in n:
    	if i['name'] == usrpl:
    		pluri = i['uri']


    results = sp.playlist_tracks(pluri)
    tracks = results['items']
    tracklist = createDict(tracks) ##creates the list of songs, works fine
    
    for track in tracklist:
        ##print(track)
        song = track.sname
        if songexists(song) == False:
            artistlist = track.sartist
            artiststr = ', '.join(artistlist)
            
            try:
                link = youtubelink(song, artiststr)
                downloader(link, song)
                convertor(song)
                tagger(track, song+".mp3")
            except:
                print(song)


if __name__ == "__main__":
    run()




