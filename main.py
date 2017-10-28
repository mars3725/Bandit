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

import facebook
accessToken = 'EAAELdPpbPooBAB2Oea8GQFHautZCaUgknOVeNxo4b43xsA37nYaB5nazj1w8VsXbcYZBnjrZCm6o4ZCZAoV0x2YyXk9gE1yXH1kiFNtWvvqmyt7mQaZCZBwZBxDABHqh6lZCRwCDbh5ZAZAcd9Kf2NtoB8Dy3hotZA1I0VX9IyyQbRpKGAYYY2Msr12tCWKS2GvwtF8ZD'
graph = facebook.GraphAPI(access_token=accessToken, version="2.10")

app_id = 1231241241
canvas_url = 'https://domain.com/that-handles-auth-response/'
perms = ['manage_pages','publish_pages']
fb_login_url = graph.auth_url(app_id, canvas_url, perms)
print(fb_login_url)