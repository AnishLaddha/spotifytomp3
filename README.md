# spotifytomp3

Hi everyone. spmp3 is a simple script that allows you to convert your spotify playlist to a mp3 library. You can also account for updates to playlists, by just running the progam again. It would be useful for home media servers, and it lets you use the amazing spotify UI. It doesnt force you to listen to adds or be beholden to a single platfor.
## Getting Started/Setup

THE SETUP IS A LITTLE COMPLICATED, USING IT IS SUPER EASY

use terminal and:

Install homebrew [here](https://brew.sh/)
Install python3 after home brew, by typing
```
brew install python
```
update pip3, by doing
```
pip3 update
```
then do the following:
```
pip3 install spotipy
pip3 install youtube-search
pip3 install ffmpeg
brew install youtube-dl
brew install ftransc
```

You next need to go to https://developer.spotify.com/dashboard/applications
there, get a create a client id, for the name, description, say whatever
for the website just put google.com
make sure to choose non commercial

now to get the code:
```
git clone https://github.com/AnishLaddha/spotifytomp3.git
```
then to finder, find the spotifytomp3.py file, and drag it to a new folder in your desktop(trust me its a lot easier) that will hold your music
then navigate to it using this:
```
cd 
cd Desktop
cd "Whatever your folder name is just make sure to put it in quotes"

```
then we run it by doing 
```
python3 spotifytomp3.py 'whatever you r username is dont put it in quotes'
```
your done


## Updating playlists
whenever you update your spotify playlist run this
```
cd 
cd Desktop
cd "Whatever your folder name is just make sure to put it in quotes"
python3 spotifytomp3.py 'whatever your username is dont put it in quotes'
```


## Built With

* [Spotipy](https://github.com/plamere/spotipy) - The spotify stuff
* [youtube-dl](https://github.com/ytdl-org/youtube-dl) - Youtube downloading
* [youtube_search](https://github.com/joetats/youtube_search) - used to search for the video on youtube

## Contributing

Please play around with this stuff, and help make it better. pm me or email me at anishladdha03@gmail.com if you comeup with a new feature

## Acknowledgments

all the authors of the libraries are amazing
