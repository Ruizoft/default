# -*- coding: utf-8 -*-
from app.auth_module.models import User, Teacher, Admin
from app import sess
from sqlalchemy.dialects.mysql import mysqldb
from sqlalchemy import update, or_
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
#from oauth2client import client, crypt
import json

def to_json(pack, prepend=False):
	if prepend:
		outputDict = dict()
		for obj in pack:
			output = dict()
			theID = getattr(obj, 'user_id')
			for field in dir(obj):
				if not field.startswith('_') and field != "metadata" and not field.startswith("child") and not field.startswith('D') and not field.startswith('to'):
					output[field] = getattr(obj, field)
				elif field.startswith('D') and getattr(obj, field) != None:
					output[field] = getattr(obj, field).isoformat()
			outputDict[theID] = output
		return outputDict
	else:
		outputList = list()
		for obj in pack:
			output = dict()
			for field in dir(obj):
				theID = getattr(obj, 'id')
				if not field.startswith('_') and field != "metadata" and not field.startswith("child") and not field.startswith('D') and not field.startswith('to'):
					output[field] = getattr(obj, field)
				elif field.startswith('D') and getattr(obj, field) != None:
					output[field] = getattr(obj, field).isoformat()
			outputList.append(output)
		return outputList

mod_auth = Blueprint('auth', __name__)
"""CLIENT_ID = "52982340847-0ese8t6k4tstva6412htlekat6cp78it.apps.googleusercontent.com"
WEB_CLIENT_ID = "52982340847-0ese8t6k4tstva6412htlekat6cp78it.apps.googleusercontent.com"
APPS_DOMAIN_NAME = "http://localhost:8080"
"""


@mod_auth.route('/signin', methods=['GET', 'POST'])
def signin():
	"""
	if 'error' in session:
		flash('Ingresaste con la cuenta equivocada', 'error-message')
		session.pop('error', None)
	"""
	form = request.form
	if form:
		email = form['email']
		password = form['password']
		user = sess.query(User).filter(User.email == email).first()
		if user and check_password_hash(user.password, password):

			session['user_id'] = user.id
			tipo = user.tipo 
			if tipo == 0:
				return redirect(url_for('mainAdmin'))
			elif tipo == 1:
				return redirect(url_for('mainTeacher'))
			elif tipo == 2:
				return redirect(url_for('mainStudent'))

	return json.dumps('1')  
 

