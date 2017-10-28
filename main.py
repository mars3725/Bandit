import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(username='mars3725',
            scope='user-top-read',
            client_id='1e86238a2330483fad99b6c952b9c874',
            client_secret='ecbe8234150b4c518940eaee14f8ff36',
            redirect_uri='http://localhost:8888/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_top_artists(time_range='long_term', limit=10)
    relatedArtists = []
    for i, item in enumerate(results['items']):
        relatedArtists.append(sp.artist_related_artists(item['id']))
    print(relatedArtists)
else:
    print("Can't get token")