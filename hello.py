from cgi import parse_qs, escape

def wsgi_application(environ, start_response):
    # бизнес-логика
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    body = ''
    for key in parameters:
            body += key + '=' + parameters[key][0] + '\n'
    print(parameters)
    body = str.encode(body)
    start_response(status, headers )
    return [ body ]


