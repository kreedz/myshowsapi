import requests

from .exceptions import MyShowsRetrieveTokenErrorException


class Session:
    TOKEN_URL = 'https://myshows.me/oauth/token'

    def __init__(self, client_id, client_secret, code=None, redirect_uri=None,
                 grant_type='client_credentials'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.code = code
        self.redirect_uri = redirect_uri
        self.grant_type = grant_type

    def load_token(self):
        token_data = requests.post(self.TOKEN_URL,
                                   data=self.get_dict_of_self_fields())
        response = token_data.json()
        if token_data.status_code == 200:
            self.token = response['access_token']
        else:
            raise MyShowsRetrieveTokenErrorException(
                    response['error_description']
            )

    def get_dict_of_self_fields(self):
        d = {}
        for p, v in vars(self).items():
            d[p] = v
        return d
