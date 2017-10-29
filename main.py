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

authorization_url = requests.get('https://api.instagram.com/oauth/authorize/',
                 params={'client_id': instagramClientID, 'redirect_uri': redirectUri, 'response_type': 'token', 'scope': 'public_content'}).url

print('Authorize Instagram at ', authorization_url)

instagramAccessCode = input('Enter access code here: ')

print(instagramAccessCode)

res = requests.get('https://api.instagram.com/v1/tags/search', params={'access_token': instagramAccessCode, 'q': 'birds'})

print(res)