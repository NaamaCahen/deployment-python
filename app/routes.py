from app import flask_app


@flask_app.route('/')
def index():
    return 'wow! its working!'

@flask_app.route('/health')
def health():
    return 'ok'