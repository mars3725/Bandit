import requests

params = {'client_id': '1e86238a2330483fad99b6c952b9c874', 'response_type': 'code', 'redirect_uri': 'http://localhost:8888/callback'}
authResponse = requests.get('https://accounts.spotify.com/authorize', params=params, headers=None)

print(authResponse)
params = {'grant_type': 'authorization_code', 'code': ''}
requests.post('https://accounts.spotify.com/api/token', params=params)