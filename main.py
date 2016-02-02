import jinja2
import os
import webapp2
import models
import datetime
from webapp2_extras import sessions
import session_module

from google.appengine.api import users

template_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.getcwd()))

#recibimos la variable de la sesion
class MainPage(session_module.BaseSessionHandler, webapp2.RequestHandler):
	def get(self):
		#si no existia una sesion
		if not self.session.get('usuario'):
			#Recibe como argumento el archivo html que sera tu pagina principal
			template = template_env.get_template('index.html')
			#variable para saber el ano actual que se utilizara en un select
			anoActual = datetime.datetime.now().year

			#Escribes las variables que mandaras y utilizaras dentro del html (noralmente se encuentran dentro de llaves {{ }})
			context = {
				'errorValidar': "0",
				'cadena': "fade",
				'errorRegistrar': "0",
				'cadena2': "fade",
				'mensajeError': "",
				'anoActual' : anoActual
			}
			#colocamos las variables del context en el html
			self.response.out.write(template.render(context))

		#si existia una sesion nos redirigimos a otra pagina (principal)
		else:
			self.redirect("/")

#nombre del controler, clase a la que pertenece, lo de la variable sesion, debug
application = webapp2.WSGIApplication([('/', MainPage)], config = session_module.myconfig_dict, debug=True)
