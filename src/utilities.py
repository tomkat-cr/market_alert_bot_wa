import datetime


def get_formatted_date():
    date_format = "%Y-%m-%d %H:%M:%S UTC"
    formatted_date = datetime.date.strftime(
        datetime.datetime.utcnow(), date_format
    )
    return formatted_date


def get_api_standard_response():
    standard_response = dict()
    standard_response['error'] = False
    standard_response['error_message'] = ''
    standard_response['data'] = dict()
    return standard_response
