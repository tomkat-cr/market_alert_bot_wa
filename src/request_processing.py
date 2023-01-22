from .mediabros_exchange_apis import usdcop, usdveb, veb_cop, crypto


def request_processing(phone_number, message):
    param_separated = message.split(" ")
    command = param_separated[0]
    debug = False
    if len(param_separated) > 1 and param_separated[1] == 'debug':
        debug = True
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
