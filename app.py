from flask import Flask

from app.api import api

app = Flask(__name__, static_folder='static', static_url_path='/', template_folder='templates')
app.register_blueprint(api.api_blueprint, url_prefix='/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2137)
