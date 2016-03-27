from cgi import parse_qs, escape

def application(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
    parameters = environ.get('QUERY_STRING', '')
    parameters = parameters.split('&')
    body = ''
    for key in parameters:
            body += key + '\n'
    print(parameters)
    body = str.encode(body)
    start_response(status, headers )
    return [ body ]


