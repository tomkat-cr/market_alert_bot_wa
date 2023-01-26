from .ext_api_processing import usdcop, usdveb, veb_cop, crypto, openai_api


def request_processing(phone_number, message):
    param_separated = message.split(" ")
    command = param_separated[0]
    param_separated.remove(command)
    debug = 0
    if len(param_separated) >= 1:
        if param_separated[0] == '/debug':
            debug = 1
            param_separated.remove('/debug')
    other_param = ' '.join(param_separated)
    if command in ['/ai', '/codex']:
        return openai_api(command, other_param, debug)
    if command == '/cop':
        return usdcop(debug)
    if command == '/bs':
        return usdveb(debug)
    if command == '/copveb':
        return veb_cop('copveb', debug)
    if command == '/vebcop':
        return veb_cop('vebcop', debug)
    if command == '/btc':
        return crypto('btc', 'usd', debug)
    if command == '/eth':
        return crypto('eth', 'usd', debug)
    return f'ERROR: Invalid option: {message} from {phone_number}'
