"""
OAuth plugin for HTTPie.

"""
from __future__ import print_function
from httpie.plugins import AuthPlugin
import os
import sys
import requests

__version__ = '1.0'
__licence__ = 'BSD'


class OAuth2Plugin(AuthPlugin):
    name = 'OAuth2'
    auth_type = 'oauth2'
    description = 'first export API_KEY, API_SECRET & AUTHORIZATION_URL'

    def get_auth(self, username, password):
        if not os.environ.get('API_KEY') or not os.environ.get('API_SECRET'):
            print('Set your API_KEY &API_SECRET in your environnement')
            sys.exit(2)

        client_id = os.environ.get('API_KEY')
        payload = {
            'grant_type':'password',
            'client_id': client_id,
            'client_secret':os.environ.get('API_SECRET'),
            'username':username,
            'password':password,
        }

        # token_url = "https://api.dailymotion.com/oauth/token"
        token_url = os.environ.get('AUTHORIZATION_URL')
        # r = requests.post(token_url, query_string=payload)
        r = requests.get(token_url, params=payload)
        if r.status_code != 200:
            print('oauth2DM: Invalid status code for token', r.status_code)

        res = r.json()
        if 'error' in res:
            print('oauth2:', res['error_description'])
            sys.exit(2)

        # if 'access_token' not in res or 'uid' not in res:
        if 'access_token' not in res:
            print('oauth2: Invalid token returned')
            sys.exit(2)
        
        from requests_oauthlib import OAuth2 
        # return OAuth2(client_id=res['uid'], token={'access_token':res['access_token'], 'token_type':'Bearer'})
        return OAuth2(client_id=client_id, token={'access_token':res['access_token'], 'token_type':'Bearer'})


