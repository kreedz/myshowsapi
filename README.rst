API wrapper for api.myshows.me (v2)
===================================

To get auth data for OAuth 2.0 please contact with email that shown at api.myshows.me (v2).

API methods are described `here <https://api.myshows.me/shared/doc/>`_.

Requirements
------------

python 3.4+

Installation
------------

pip3 install myshowsapi

Usage
-----

.. code:: python

    >>> import myshowsapi

    # Getting token within Client Credentials Grant
    >>> session = myshowsapi.Session(client_id='<CLIENT_ID>',
                                     client_secret='<CLIENT_SECRET>')

    # Getting token within Authorization Code Grant
    >>> # session = myshowsapi.Session(client_id='<CLIENT_ID>',
    #                                  client_secret='<CLIENT_SECRET>', code='<CODE>',
    #                                  redirect_uri='<REDIRECT_URI>',
    #                                  grant_type='authorization_code')
    # You can receive the <CODE> in response headers after authorization at
    # https://myshows.me/oauth/authorize?response_type=code&client_id=<CLIENT_ID>
    # &scope=basic

    >>> api = myshowsapi.API(session)
    >>> api.profile.Get(login='user')
    {'stats': {'remainingDays': 2.5,
      'remainingEpisodes': 154,
      'remainingHours': 60.5,
      'totalDays': 65,
      'totalEpisodes': 2640,
      'totalHours': 1560.7,
      'watchedDays': 62.5,
      'watchedEpisodes': 2486,
      'watchedHours': 1500.2},
     'user': {'avatar': 'https://api.myshows.me/shared/img/fe/default-user-avatar-normal.png',
      'gender': 'm',
      'isPro': False,
      'login': 'bwn',
      'wastedTime': 1502}}

