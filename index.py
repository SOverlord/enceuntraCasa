import webapp2
from webapp2_extras import sessions
import crearSesion
import session_module
import models
from google.appengine.ext import db

#recibe la sesion y webapp2
class principal(session_module.BaseSessionHandler, webapp2.RequestHandler):
	def get(self): 
		#Sino existe una sesion redireccionamos al controler main.py
		if not self.session.get('usuario'):
			self.redirect("/")
		#si existe la sesion, imprimos que sesion es
		else:
			self.response.out.write('Usuario = ' + self.session['usuario'])

#controler, clase, sesion, debug
application = webapp2.WSGIApplication([('/principal', principal),], config = session_module.myconfig_dict, debug=True)
