from fastapi.responses import PlainTextResponse

from .settings import settings
from .whatsapp_send_message import send_whatsapp_message
from .request_processing import request_processing


def whatsapp_webhook_get(request):
    try:
        WHATSAPP_VERIFY_TOKEN = settings.WHATSAPP_VERIFY_TOKEN
        mode = request.get('hub.mode')
        token = request.get('hub.verify_token')
        challenge = request.get('hub.challenge')
        print(f'whatsapp_webhook_get: mode={mode}, token={token}, challenge={challenge}')
        if mode and token and mode == 'subscribe' and token == WHATSAPP_VERIFY_TOKEN:
            print('HTTPResponse(challenge, status=200)')
            return PlainTextResponse(content=challenge, status_code=200)
        else:
            print(f"mode == 'subscribe': {mode == 'subscribe'}")
            print(f'token == WHATSAPP_VERIFY_TOKEN: {token == WHATSAPP_VERIFY_TOKEN}')
            print(f'WHATSAPP_VERIFY_TOKEN: {WHATSAPP_VERIFY_TOKEN}')
            print('HTTPResponse(\'error\', status=403)')
            return PlainTextResponse(content='error', status_code=403)
    except Exception as err:
        print(f'ERROR: whatsapp_webhook_get() -> {str(err)}')


def whatsapp_webhook_post(data):
    try:
        webhook_response = 'success'
        status_code = 200

        # print('Paso por aca 1')

        if not data or not data.object or not data.entry:
            webhook_response = 'No object and/or entry data'

        # print('Paso por aca 2')

        if data and data.object != 'whatsapp_business_account':
            webhook_response = 'object is not "whatsapp_business_account":' + \
                f" {data.object}"

        # print('Paso por aca 3')

        if webhook_response != 'success':
            print(f'IGNORED: whatsapp_webhook_post() -> {webhook_response}')
            return PlainTextResponse(
                content=webhook_response,
                status_code=status_code
            )

        # print('Paso por aca 4')

        for entry in data.entry:
            if 'contacts' not in entry['changes'][0]['value']:
                break
            # phone_number = entry['changes'][0]['value']['metadata']['display_phone_number']
            # phone_id = entry['changes'][0]['value']['metadata']['phone_number_id']
            # profile_name = entry['changes'][0]['value']['contacts'][0]['profile']['name']
            whatsapp_id = entry['changes'][0]['value']['contacts'][0]['wa_id']
            # from_id = entry['changes'][0]['value']['messages'][0]['from']
            # messages_id = entry['changes'][0]['value']['messages'][0]['id']
            # timestamp = entry['changes'][0]['value']['messages'][0]['timestamp']
            text = entry['changes'][0]['value']['messages'][0]['text']['body']

            # print('Paso por aca 5')

            message = f'RE: {str(text)} was received from {str(whatsapp_id)}'
            print(f'Message: {message}')
            message = request_processing(whatsapp_id, text)

            swm_response = send_whatsapp_message(whatsapp_id, message)
            print(f'>>--> swm_response: {swm_response}')

    except Exception as err:
        webhook_response = str(err)
        status_code = 500
        # raise Exception(err)

    print('whatsapp_webhook_post() ->' +
          f' webhook_response: {webhook_response},' +
          f' status_code: {status_code}'
          )

    return PlainTextResponse(
        content=webhook_response,
        status_code=status_code
    )
