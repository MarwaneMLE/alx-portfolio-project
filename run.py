from flask import Flask
from application import app

#app = Flask(__name__)
 
if __name__ == '__main__':
    app.run(debug=True, port=3000)