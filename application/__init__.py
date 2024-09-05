from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.app_context()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'
app.config['SECRET_KEY'] = "JLKJJJO3IURYoiogfjjuolnohth@€[jojouuoo=5y9y9youjuy952oohhbafdnoglhoho"


db = SQLAlchemy(app)
app.app_context().push()
#with app.app_context():
# # db.create_all()

from application import routes
 

# from application import db
# from application.models import RetailSales