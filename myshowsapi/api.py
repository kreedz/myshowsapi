import requests

from .exceptions import MyShowsException, MyShowsRetrieveTokenErrorException


class API:
    API_URL = 'https://api.myshows.me/v2/rpc/'

    def __init__(self, session):
        self.session = session
        self.session.load_token()

    def __getattr__(self, method_name):
        return Request(self, method_name)

    def make_request(self, request):
        header_token = 'Bearer {0}'.format(self.session.token)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Language': 'en',
            'Authorization': header_token,
        }
        json = {
            'jsonrpc': '2.0',
            'id': 1,
            'method': request.method_name,
            'params': request.method_args
        }
        response = requests.post(
            self.API_URL, headers=headers, json=json
        )
        response_json = response.json()
        if response.status_code == 200:
            try:
                return response_json['result']
            except KeyError:
                raise MyShowsException(response_json['error'])
        else:
            raise MyShowsRetrieveTokenErrorException(
                    response_json['error_description']
            )


class Request:
    def __init__(self, api, method_name):
        self.api = api
        self.method_name = method_name

    def __getattr__(self, method_name):
        return Request(self.api, self.method_name + '.' + method_name)

    def __call__(self, **method_args):
        self.method_args = method_args
        return self.api.make_request(self)
