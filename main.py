import spotipy
import spotipy.util as util

token = util.prompt_for_user_token(username='mars3725',
                scope='user-top-read',
                client_id='1e86238a2330483fad99b6c952b9c874',
                client_secret='ecbe8234150b4c518940eaee14f8ff36',
                redirect_uri='http://localhost/')

if token:
    sp = spotipy.Spotify(auth=token)
    likedArtists = sp.current_user_top_artists(time_range='long_term')
    relatedArtists = []
    for likedArtist in likedArtists['items']:
        newArtists = sp.artist_related_artists(likedArtist['id'])
        for newArtist in newArtists['artists']:
            relatedArtists.append(newArtist)
else:
    print("Can't get token")