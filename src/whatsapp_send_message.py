import requests
from settings import settings
from utilities import get_api_standard_response


# Documetation:
# https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages


def send_whatsapp_message_generic(phone_number, message_payload):
    response = get_api_standard_response()
    try:
        headers = {
            "Authorization": 'Bearer ' + settings.WHATSAPP_TOKEN,
            "Content-Type": "application/json"
        }
        payload = dict(message_payload)
        payload["messaging_product"] = "whatsapp"
        payload["to"] = phone_number

        print(
            '>>--> SEND MESSAGE TO WHATSAPP:',
            f'url: {settings.WHATSAPP_URL}',
            f'headers: {headers}',
            f'payload: {payload}',
        )

        response_post = requests.post(
            settings.WHATSAPP_URL,
            headers=headers,
            json=payload
        )
        response['data'] = response_post.json()
    except Exception as err:
        response['error'] = True
        response['error_message'] = 'ERROR: send_whatsapp_message_generic:' + \
            f' {str(err)}'
        print(response['error_message'])
    return response


def send_whatsapp_template(phone_number, name, lang="en_US"):
    response = get_api_standard_response()
    try:
        message_payload = {
            "type": "template",
            "template": {
                "name": name,
                "language": {
                    "code": lang
                }
            }
        }
        response['data'] = send_whatsapp_message_generic(
            phone_number, message_payload
        )
    except Exception as err:
        response['error'] = True
        response['error_message'] = f'ERROR: send_whatsapp_template: {str(err)}'
        print(response['error_message'])
    return response


def send_whatsapp_message(phone_number, message):
    response = get_api_standard_response()
    try:
        message_payload = {
            "type": "text",
            "text": {
                "body": message
            }
        }
        response['data'] = send_whatsapp_message_generic(
            phone_number, message_payload
        )
    except Exception as err:
        response['error'] = True
        response['error_message'] = f'ERROR: send_whatsapp_message: {str(err)}'
        print(response['error_message'])
    return response
