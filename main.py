import spotipy
import spotipy.util as util
from collections import Counter
from requests_oauthlib import OAuth2Session
import requests

spotifyClientId = '1e86238a2330483fad99b6c952b9c874'
spotifySecret = 'ecbe8234150b4c518940eaee14f8ff36'
instagramClientID = '9caf0ebad9a4442e8a9df86eee419679'
instagramSecret = '8f68502c508e4bacade9d61fe9f9d438'
redirectUri = 'https://localhost/'

token = util.prompt_for_user_token(username='mars3725',
                scope='user-top-read',
                client_id=spotifyClientId,
                client_secret=spotifySecret,
                redirect_uri=redirectUri)

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

searchQueries = []

for item, freq in artistFreq:
    searchQueries.append(item)
for item, freq in genreFreq:
    searchQueries.append(item)

print(searchQueries)

oauth = OAuth2Session(client_id=instagramClientID, redirect_uri=redirectUri,
                          scope='basic')
authorization_url, state = oauth.authorization_url(
    'https://api.instagram.com/oauth/authorize/',)

print('Authorize Instagram at ', authorization_url)
authorization_code = input('Enter callback code: ')

token = requests.post('https://api.instagram.com/oauth/access_token',
              {'client_id': instagramClientID, 'client_secret': instagramSecret,
               'grant_type': 'authorization_code', 'redirect_uri': redirectUri,
               'code': authorization_code})

print(token)