from flask import Flask
from application import app
#from application import create_app

#app = Flask(__name__)

#app = create_app()

if __name__ == '__main__':
    app.run(debug=True)