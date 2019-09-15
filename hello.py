#!/usr/bin/python
# -*- coding: latin-1 -*-

from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def accueil():
	secretHash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
	titre = "D�couvrez le code secret!!!"
	
	if request.method == 'POST':
		answer = request.form.get('ans')
		mode = request.form.get('algorithmes')
		theURL = request.form.get('algorithmes')
		hashed = hashThisShit(answer, mode)
		if hashed == secretHash:
			verdict = "correspond"
		else:
			verdict = "ne correspond pas"
			
		return render_template('accueil.tpl', titre = titre, result = hashed, mode = mode, verdict = verdict)
		
	else :
		return render_template('accueil.tpl', titre = titre)

@app.errorhandler(404)
def myErrorHandle(e):
	titre = "Erreur 404!  Page non trouv�e!"
	message = "La page " + request.base_url + " n'existe pas!"
	return render_template('page404.tpl', titre = titre, message = message)
	
		
def hashThisShit(ans, mode):
	print(mode)
	switcher={
		"md5": hashlib.md5(),
		"sha1": hashlib.sha1(),
		"sha224": hashlib.sha224(),
		"sha256": hashlib.sha256(),
		"sha384": hashlib.sha384(),
		"sha512": hashlib.sha512()
	}
	
	hashMode = switcher.get(mode, "Error!!!")
	hashMode.update(ans.encode('utf-8'))
	return hashMode.hexdigest()
	
	
if __name__ == '__main__':
	app.run(ssl_context=('travail2_cert.crt', 'travail2_pv.key'))