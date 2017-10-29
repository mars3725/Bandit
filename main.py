import spotipy
import spotipy.util as util
from collections import Counter
import requests

### LOGIN INFO ###
spotifyClientId = '1e86238a2330483fad99b6c952b9c874'
spotifySecret = 'ecbe8234150b4c518940eaee14f8ff36'
instagramClientID = '9caf0ebad9a4442e8a9df86eee419679'
instagramSecret = '8f68502c508e4bacade9d61fe9f9d438'
lastFMKey = 'b0d255523413ef57205bac97cbad36ad'
lastFMSecret = 'd6be19e48f67d480c59a9c5bd3935022'
redirectUri = 'https://localhost/'

### SPOTIFY ###
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
artists = genres = []
for item, freq in artistFreq:
    artists.append(item)
for item, freq in genreFreq:
    genres.append(item)

### LASTFM ###
req = requests.get('http://ws.audioscrobbler.com/2.0/',
                   params={'method': 'artist.search', 'artist':artists[0],
                           'api_key': lastFMKey, 'format': 'json'})
lastFMArtists = req.json()['results']['artistmatches']['artist'][0]['name']

### INSTAGRAM ###
authorization_url = requests.get('https://api.instagram.com/oauth/authorize/',
                 params={'client_id': instagramClientID, 'redirect_uri': redirectUri, 'response_type': 'token', 'scope': 'public_content'}).url
print('Authorize Instagram at ', authorization_url)
instagramAccessCode = input('Enter access code here: ')

instaTags = {''}
for artist in artists:
    instaTags.append(requests.get('https://api.instagram.com/v1/tags/search', params={'access_token': instagramAccessCode, 'q': artist}).json()['data'])
instaTags = sum(instaTags, [])
print(instaTags)