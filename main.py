import json
import requests
name = input("Enter a song name for getting lyrics: ")
lyrics = requests.get(f'https://some-random-api.ml/lyrics?title={name}')
lyricsdata = lyrics.json()
songname = (str(lyricsdata['title']))
songauthor = (str(lyricsdata['author']))
songlyrics = (str(lyricsdata['lyrics']))
print('\n\n')
print(f'Song name is ---- {songname}.\nThe author is ---- {songauthor}\n\n And the lyrics are :-\n\n {songlyrics}\n')
