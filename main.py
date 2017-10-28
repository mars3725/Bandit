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
        for relatedArtist in relatedArtists:
            relatedArtistNames.append(relatedArtist['name'])
        genres.append(likedArtist['genres'])
else:
    print("Can't get token")

artistFreq = Counter(relatedArtistNames).most_common(5)
genreFreq = Counter(sum(genres, [])).most_common(5)

print(artistFreq)
print(genreFreq)

searchQueries = []

for item, freq in artistFreq:
    searchQueries.append(item)
for item, freq in genreFreq:
    searchQueries.append(item)

print(searchQueries)