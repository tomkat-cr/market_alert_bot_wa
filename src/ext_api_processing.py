import requests
import urllib.parse

from .general_utilities import get_api_standard_response
from .settings import settings


# Common


def call_mediabros_api(url, api_name):
    print('call_mediabros_api', url, api_name)
    api_response = get_api_standard_response()
    try:
        response = requests.get(url)
    except Exception as err:
        api_response['error'] = True
        api_response['error_message'] = str(err)
    else:
        if response.status_code == 200:
            api_response = response.json()
        else:
            api_response['error'] = True
            api_response['error_message'] = 'ERROR reading ' + \
                f'{api_name} API'
    return str(api_response)


# Exchange APIs


def crypto(symbol, currency, debug):
    currency = currency.upper()
    symbol = symbol.upper()
    url = settings.APIS_COMMON_SERVER_NAME + \
        f'/crypto/{symbol}/{currency}/{str(debug)}'
    return call_mediabros_api(url, 'Crypto Currency Exchange')


def usdveb(debug):
    url = settings.APIS_COMMON_SERVER_NAME + \
        f'/usdvef/{str(debug)}'
    return call_mediabros_api(url, 'Venezuelan Bolivar Exchange')


def usdcop(debug):
    url = settings.APIS_COMMON_SERVER_NAME + \
        f'/usdcop/{str(debug)}'
    return call_mediabros_api(url, 'Colombian Peso Exchange')


def veb_cop(currency_pair, debug):
    url = settings.APIS_COMMON_SERVER_NAME + \
        f'/{currency_pair}/{str(debug)}'
    return call_mediabros_api(
        url, f'Bolivar COP Exchange [{currency_pair}]'
    )

# AI


def openai_api(command, other_param, debug):
    url = settings.APIS_COMMON_SERVER_NAME + \
        f'{command}?debug={str(debug)}&q={urllib.parse.quote(other_param)}'
    return call_mediabros_api(
        url, f'Open AI [{command}]'
    )
