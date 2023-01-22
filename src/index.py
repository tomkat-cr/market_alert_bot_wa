import sys
from typing import Union, Any

from fastapi import FastAPI, Request
from pydantic import BaseModel
from a2wsgi import ASGIMiddleware

from whatsapp_webhook import whatsapp_webhook_get, whatsapp_webhook_post
from whatsapp_send_message import send_whatsapp_message, send_whatsapp_template
from utilities import get_formatted_date


def get_command_line_args():
    params = dict()
    params['mode'] = 'api'
    params['config_filename'] = '.env'
    if len(sys.argv) > 1:
        params['mode'] = sys.argv[1]
    if len(sys.argv) > 2:
        params['config_filename'] = sys.argv[2]
    return params


params = get_command_line_args()
if params['mode'] == 'cli':
    apiResponse = whatsapp_webhook_post(params.get('body'))
    print(apiResponse)

api = FastAPI()
app = ASGIMiddleware(api)


# EndPoints


class Body(BaseModel):
    object: Union[str, None] = None
    entry: Union[Any, None] = None


@api.get("/data/")
async def api_data(request: Request):
    print('---------')
    print(get_formatted_date())
    print('/data')
    api_response = request.query_params
    print(api_response)
    return api_response


@api.get("/webhook")
async def webhook_get(request: Request):
    print('---------')
    print(get_formatted_date())
    print(f'webhook_get: request = {request.query_params}')
    api_response = whatsapp_webhook_get(request.query_params)
    print(f'webhook_get: api_response = {api_response}')
    return api_response


@api.post("/webhook")
async def webhook_post(body: Body):
    print('---------')
    print(get_formatted_date())
    print(f'webhook_post: body = {str(body)}')
    api_response = whatsapp_webhook_post(body)
    print(f'webhook_post: api_response = {api_response}')
    return api_response


@api.get("/send_template")
def send_template(phone, template='hello_world'):
    print('---------')
    print(get_formatted_date())
    print('send_template')
    print(f'phone_number = {phone}')
    print(f'template = {template}')
    print('send_whatsapp_template - Begin...')
    api_response = send_whatsapp_template(phone, template)
    print('send_whatsapp_template - End...')
    print(api_response)
    return api_response


@api.get("/send_message")
def send_message(phone, message):
    print('---------')
    print(get_formatted_date())
    print('send_message')
    print(f'phone_number = {phone}')
    print(f'message = {message}')
    api_response = send_whatsapp_message(phone, message)
    return api_response
