from django.conf import settings
import requests
import logging
from .encode import make_signature, http_date
import environ
# from .bot import Bot
import os
logger = logging.getLogger(__name__)

API_URL = os.environ.get('API_URL')
API_KEYWORD = os.environ.get('API_KEYWORD')
API_ID = os.environ.get('API_ID')
API_SECRET = os.environ.get('API_SECRET')



def _request(method, uri, **kwargs) -> dict:
    request_date = http_date().encode()
    signature = make_signature(API_SECRET, request_date)
    headers = {
        'Authorization': f'{API_KEYWORD} {API_ID}:{signature}',
        'User-Agent': 'PostmanRuntime/7.26.1',
        'DATE': request_date,
        'HOST': 'ops-api.baifu-tech.net',
        'content-type': 'application/json'
    }
    try:
        url = f"{API_URL}/{uri}"
        logger.debug(url)
        data = requests.api.request(method=method, url=url, timeout=300, headers=headers, **kwargs)
        return data.json()
    except Exception as e:
        logger.error(f'失敗 {e}')
        # Bot.error(f'失敗 {e}')
        return dict(code='1', data='', message=e)




def get(url, params=None, **kwargs) -> dict:
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('get', url, params=params, **kwargs)


def post(url, data=None, json=None, **kwargs) -> dict:
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('post', url, data=data, json=json, **kwargs)


def put(url, data=None, **kwargs) -> dict:
    r"""Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('put', url, data=data, **kwargs)

def delete(url, **kwargs):
    r"""Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('delete', url, **kwargs)
