import webapp2
from webapp2_extras import sessions
import session_module
import models

from google.appengine.ext import db

#Recibe como parametro la sesion
class cerrarSesion(session_module.BaseSessionHandler):
	def get(self): 
		#Si se encontro la variable de sesion 'usuario'
		if self.session.get('usuario'):
			print 'Sesion Cerrada'
			#borramos la sesion
			del self.session['usuario']
			#nos redirigimos al controlador main.py
			self.redirect("/")

		#Si no existia esa sesion
	  	else:
			self.response.out.write("No se puede cerrar sesion porque no existia una sesion")
			self.redirect("/")

#nombre del controlador, clase a la que pertenece, la sesion y el debug
application = webapp2.WSGIApplication([('/cerrarSesion', cerrarSesion),], config = session_module.myconfig_dict, debug=True)
