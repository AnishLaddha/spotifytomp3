import spotipy
import sys
import json
import pprint
import requests
import os
import urllib.request
from youtube_search import YoutubeSearch
import conv
import fnmatch



from spotipy.oauth2 import SpotifyClientCredentials




client_credentials_manager = SpotifyClientCredentials(client_id='2528e9e7f4fa492aaecfc9e07c18f444',
                                                      client_secret='c1595dd6fe0a406ca075ba7e5733ec79')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
pp = pprint.PrettyPrinter(indent=4)

if len(sys.argv) > 1:
    usr = ' '.join(sys.argv[1:])

else:
    usr = ''

##sp.trace = True # turn on tracing
##sp.trace_out = True # turn on trace out

user = sp.user(usr)

playlists = sp.user_playlists(usr)

print("Hello " + user['display_name']+" !")
n = playlists['items']
print("your playlists: ")
for i in n:
	print(i['name'])
usrpl = input("Choose your playlist: ")
for i in n:
	if i['name'] == usrpl:
		pluri = i['uri']
##print(pluri)
results = sp.playlist_tracks(pluri)
##pp.pprint(results)
tracklist = []

filename = usrpl+" list"+".txt"
filewrite = open(filename, "a")
fileread = open(filename, "r")

oldlist = []

for x in fileread:
	oldlist.append(x)

tracks = results['items']
for i in tracks:
	string = ""
	# thingy = i['track']
	# pp.pprint(thingy['id'])
	track = i['track']
	string = string + track['name']+" by "
	##print(track['name'] + " by ")
	artists = track['artists']
	for j in artists:
		artist = j['name']
		string = string +artist+" "
	print(string)
	tracklist.append(string)
##print(tracklist)




def downloadaudio(url, title):
	command = "youtube-dl -f m4a "+url
	##print(command)
	os.system(command)

failed = []

##print(oldlist)

for i in tracklist:
	e = i + "\n"
	if e not in oldlist:
		filewrite.write(i+"\n")
		searchresults = YoutubeSearch(i+" audio" , max_results=1).to_dict()
		#print(searchresults)
		try:
			print("trying to download")
			searchresult = searchresults[0]
			searchid = searchresult['id']
			if searchid[0] == "-":
				searchid = searchid[1:]
			downloadaudio(searchid, i)
		except:
			failed.append(i)






print(failed)

#wc7JPaRV5uU

m4as = []
for root, dirs, files in os.walk(os.getcwd()):
    m4as += fnmatch.filter(files, '*.m4a')
##print(m4as)
count = 0
for i in m4as:
	print(i+ " "+str(count))
	count= count +1
	os.system("ftransc -r -q extreme -f mp3 "+"'"+i+"'")
