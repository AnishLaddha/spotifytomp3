# spotifytomp3

Hi everyone. spmp3 is a simple script that allows you to convert your spotify playlist to a mp3 library. You can also account for updates to playlists, by just running the progam again. It would be useful for home media servers, and it lets you use the amazing spotify UI. It doesnt force you to listen to adds or be beholden to a single platform.

### NOW INCLUDING META DATA, CLEAN FILE NAMES, AND COVER ART!!!

## Getting Started/Setup

Install homebrew [here](https://brew.sh/)
Install python3 after home brew, by typing
```
brew install python
```

run the script.sh file (download + run)

You next need to go to https://developer.spotify.com/dashboard/applications
there, get a create a client id, for the name, description, say whatever
for the website just put google.com
make sure to choose non commercial

```
then we run it by doing 
```
python3 spotifytomp3.py --username="" --playlist="'
```
your done


## Updating playlists
whenever you update your spotify playlist run this
```
cd 
python3 spotifytomp3.py --username="" --playlist="'
```


## Built With

* [Spotipy](https://github.com/plamere/spotipy) - The spotify stuff, plus metadata
* [youtube-dl](https://github.com/ytdl-org/youtube-dl) - Youtube downloading
* [youtube_search](https://github.com/joetats/youtube_search) - used to search for the video on youtube
* [eyed3](https://github.com/nicfit/eyeD3) - Metadata editing
* [click](https://github.com/pallets/click/) - adding the 

## Contributing

play around with this stuff, and help make it better. pm me or email me at anishladdha03@gmail.com if you comeup with a new feature

## Acknowledgments

all the authors of the libraries are amazing
