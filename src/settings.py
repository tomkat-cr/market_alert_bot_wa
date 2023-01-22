import os


class settings:
    APP_NAME = os.environ.get('APP_NAME')
    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
    SERVER_NAME = os.environ.get('SERVER_NAME')
    WHATSAPP_PHONE_ID = os.environ.get('WHATSAPP_PHONE_ID')
    WHATSAPP_BUSINESS_ID = os.environ.get('WHATSAPP_BUSINESS_ID')
    WHATSAPP_VERIFY_TOKEN = os.environ.get('WHATSAPP_VERIFY_TOKEN')
    WHATSAPP_TOKEN = os.environ.get('WHATSAPP_TOKEN')
    WHATSAPP_URL = os.environ.get('WHATSAPP_URL')
