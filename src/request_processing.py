import requests
from utilities import get_api_standard_response


def cop_api_raw():
    api_response = get_api_standard_response()
    url = 'https://cop-exchange-rates.vercel.app/get_exchange_rates'
    try:
        response = requests.get(url)
    except Exception as err:
        api_response['error'] = True
        api_response['error_message'] = str(err)
    else:
        if response.status_code == 200:
            api_response['data'] = response.json()
        else:
            api_response['error'] = True
            api_response['error_message'] = 'ERROR reading ' + \
                'Mediabros\' cop-exchange-rates API'
    # report_error_to_tg_group(api_response)
    return api_response


def cop_api():
    return str(cop_api_raw())


def request_processing(phone_number, message):
    if message == '/cop':
        return cop_api()
    return f'ERROR: Invalid option: {message} from {phone_number}'
