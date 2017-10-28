import oauth2
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix
import facebook

#Login Info
spotifyClient = '1e86238a2330483fad99b6c952b9c874'
spotifySecret = 'ecbe8234150b4c518940eaee14f8ff36'
redirect_uri = 'https://localhost/'
facebookClient = '294072021106314'
facebookSecret = 'de82f75a2cd78c875479920b877'

oauth = OAuth2Session(spotifyClient, redirect_uri=redirect_uri, scope='user-top-read')
authorization_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize')

print('Authorize Spotify at ', authorization_url)
authorization_response = input('Enter the full callback URL: ')

# OAuth endpoints given in the Facebook API documentation
authorization_base_url = 'https://www.facebook.com/dialog/oauth'
token_url = 'https://graph.facebook.com/oauth/access_token'

fb = facebook_compliance_fix(OAuth2Session(facebookClient, redirect_uri=redirect_uri))

# Redirect user to Facebook for authorization
authorization_url, state = fb.authorization_url(authorization_base_url)
print('Authorize Facebook at ', authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

# Fetch the access token
facebook.fetch_token(token_url, client_secret=facebookSecret, authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
r = facebook.get('https://graph.facebook.com/me?')
print(r.content)
