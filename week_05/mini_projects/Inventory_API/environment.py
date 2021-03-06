# Python's bundled WSGI server
from wsgiref.simple_server import make_server
from wsgiref.util import guess_scheme
import json
import inventory

# set the encoding
encoding = 'utf-8'

# set port
port = 8000

# create object of MyApp
my_obj = inventory.MyApp()


def application_(environ, start_response):

    try:
        response_text = my_obj.dispatch(environ)

    except Exception as exe:
        status = "500 Internal Server Error"
        response_text = ''
        print(exe)

    status = '200 OK'  # HTTçP Status
    headers = [('Content-type', 'text/plain; charset=' + encoding)]  # HTTP Headers
    start_response(status, headers)

    return [response_text.encode('utf-8')]


httpd = make_server('localhost', port, application_)
print(f"Serving up tasty treats on port {port}...")

# Serve until process is killed
httpd.serve_forever()
