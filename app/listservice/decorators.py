import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('static/api_key_files/server.crt', 'static/api_key_files/server.key')

# The actual decorator function
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('static/api_key_files/api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        #if request.args.get('key') and request.args.get('key') == key:
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            #abort(401)
            return jsonify ({
                                'msg': '401:Unauthorized, API key is missing !'
                            })
    return decorated_function