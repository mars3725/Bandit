import spotipy
import spotipy.util as util
import numpy
from collections import Counter

def flatList(list):
    return [item for sublist in list for item in sublist]

token = util.prompt_for_user_token(username='mars3725',
                scope='user-top-read',
                client_id='1e86238a2330483fad99b6c952b9c874',
                client_secret='ecbe8234150b4c518940eaee14f8ff36',
                redirect_uri='http://localhost/')

if token:
    sp = spotipy.Spotify(auth=token)
    items = 20
    likedArtists = sp.current_user_top_artists(time_range='long_term', limit=items)
    relatedArtistNames = []
    genres = []
    for likedArtist in likedArtists['items']:
        relatedArtists = sp.artist_related_artists(likedArtist['id'])['artists']
        relatedArtists.append()
        genres.append(likedArtist['genres'])
else:
    print("Can't get token")

words = "apple banana apple strawberry banana lemon"
freqs = Counter(words.split())
print(freqs)
Counter({'apple': 2, 'banana': 2, 'strawberry': 1, 'lemon': 1})
