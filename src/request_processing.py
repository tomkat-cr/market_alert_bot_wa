import os
import sys
import requests
from utilities import get_api_standard_response


def send_tg_message(user_id, message):
    bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    # Send the message
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + user_id + '&text=' + str(message)
    response = requests.get(url)
    print(response.content)
    return response


def report_error_to_tg_group(api_response):
    if not api_response['error']:
        return
    return send_tg_message(os.environ['TELEGRAM_CHAT_ID'], {
        'type': 'ERROR in a Mediabros API',
        'app_name': os.environ.get('APP_NAME'),
        'server_name': os.environ.get('SERVER_NAME'),
        'calling_func': sys._getframe(1).f_code.co_name,
        'error_message': api_response['error_message'],
    })


def veb_bcv_api_raw():
    api_response = get_api_standard_response()
    url = 'https://bcv-exchange-rates.vercel.app/get_exchange_rates'
    try:
        response = requests.get(url)
    except Exception as err:
        api_response['error'] = True
        api_response['error_message'] = str(err)
    else:
        if response.status_code == 200:
            result = response.json()
            api_response['data'] = result
            if result['error']:
                api_response['error'] = True
                api_response['error_message'] = result['error_message']
        else:
            api_response['error'] = True
            api_response['error_message'] = 'ERROR reading BCV official' + \
                ' USD/Bs API'
    report_error_to_tg_group(api_response)
    return api_response


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
    report_error_to_tg_group(api_response)
    return api_response


def cop_api():
    return str(cop_api_raw())


def veb_bcv_api():
    return str(veb_bcv_api_raw())


def request_processing(phone_number, message):
    if message == '/cop':
        return cop_api()
    if message == '/bs':
        return veb_bcv_api()
    return f'ERROR: Invalid option: {message} from {phone_number}'
