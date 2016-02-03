from flask import Flask, render_template,flash, g, session, redirect, url_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine
app = Flask(__name__)
app.config.from_object('config')
Session = sessionmaker()
engine = create_engine('mysql+mysqldb://root:password@localhost/db?charset=utf8&use_unicode=0')
Session.configure(bind=engine)

sess = Session()
Base = declarative_base()
from app.auth_module.controllers import  mod_auth as auth_module
app.register_blueprint(auth_module)


@app.route('/')
def welcome():
	return render_template("welcome.html")

