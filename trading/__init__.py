
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY']='65e7a9e3b83e640f5374a70ce09d0c91'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_site.db'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'laviagrawal117@gmail.com'
app.config['MAIL_PASSWORD'] = 'chahat@1971'
mail = Mail(app)


from trading import routes 