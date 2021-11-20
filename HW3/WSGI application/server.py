from datetime import datetime
from urllib.parse import quote
import json


def app(environ, start_response):

    ur = environ['wsgi.url_scheme'] + '://'

    if environ.get('HTTP_HOST'):
        ur += environ['HTTP_HOST']
    else:
        ur += environ['SERVER_NAME']

        if environ['wsgi.url_scheme'] == 'https':
            if environ['SERVER_PORT'] != '443':
                ur += ':' + environ['SERVER_PORT']
        else:
            if environ['SERVER_PORT'] != '80':
                ur += ':' + environ['SERVER_PORT']

    ur += quote(environ.get('SCRIPT_NAME', ''))
    ur += quote(environ.get('PATH_INFO', ''))
    if environ.get('QUERY_STRING'):
        ur += '?' + environ['QUERY_STRING']

    data = {'time': datetime.now().time().isoformat(), 'url': ur}

    status = '200 OK'
    response_headers = [
        ('Content-type', 'application/json')
    ]
    start_response(status, response_headers)

    return [bytes(json.dumps(data), 'utf-8')]

