import os
from app import create_app
from flask_script import Manager, Shell , Server

config_name = os.getenv('APP_SETTINGS')

app = create_app(config_name)
if __name__ == '__main__':
    app.run(debug = True)