import spotipy
import spotipy.util as util

scope = 'user-library-read'

token = util.prompt_for_user_token(username='mars3725',
            scope='user-library-read',
            client_id='1e86238a2330483fad99b6c952b9c874',
            client_secret='ecbe8234150b4c518940eaee14f8ff36',
            redirect_uri='http://localhost:8888/callback')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print("Can't get token")