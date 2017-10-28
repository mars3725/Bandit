from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
import facebook as fb
import requests
from oauthlib.oauth2 import BackendApplicationClient

#Login Info
spotifyClient = '1e86238a2330483fad99b6c952b9c874'
spotifySecret = 'ecbe8234150b4c518940eaee14f8ff36'
redirect_uri = 'https://localhost/'
facebookClient = '294072021106314'
facebookSecret = 'de82f75a2cd78c875479920b877'

spotify = OAuth2Session(spotifyClient, redirect_uri=redirect_uri, scope=['user-top-read'])
authorization_url, state = spotify.authorization_url('https://accounts.spotify.com/authorize')
print('Authorize Spotify at ', authorization_url)
authorization_response = input('Enter the full callback URL: ')

client = BackendApplicationClient(client_id=spotifyClient)
spotify = OAuth2Session(client=client)
token = spotify.fetch_token('https://accounts.spotify.com/api/token', client_id=spotifyClient, client_secret=spotifySecret)
usersArtists = spotify.request('GET', url='https://api.spotify.com/v1/me/top/{type}',
                               data={'type': 'artists', 'limit': 5, 'time_range': 'long_term'})
print(usersArtists)
