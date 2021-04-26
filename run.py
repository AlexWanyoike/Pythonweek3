from app import app
from app import create_app
from flask_script import Manager, Shell , Server

if __name__ == '__main__':
    app.run(debug=True)