import jinja2
import os
import webapp2
import models
import datetime
from google.appengine.ext import db

class Validar_inicio_sesion(webapp2.RequestHandler):
	def post(self):
		try:
		    #Asociamos las variables del HTML que se encuentran en el atributo name de los input con variables locales
		    email = self.request.get('email')
		    contrasena  = self.request.get('password')
		    #Hacemos una busqueda del correo y la contrasena. filter recibe primero el nombre de la variable de la base de datos entre comillas
		    #y despues la variable local.
		    usuario = db.Query(models.Usuario).filter("str_email", email).filter("str_password", contrasena)

		    #Almacenamos los resultados en esta variable
		    data = usuario.get()

		    #Si se encontro, vamos a la pagina que se especifica a continuacion.
		    if data:
		        self.redirect("/crearSesion?user=" + data.str_email + "&py=validar" )

		    #Si no se encontro
		    else:

		        template = jinja2.Environment(
		        loader = jinja2.FileSystemLoader(os.getcwd()))
		        anoActual = datetime.datetime.now().year

		        #Cargamos la pagina en la que se avisara del error
		        template = template.get_template('index.html')

		        #Enviamos variables que desplegaran informacion en el html
		        context = {
				  'errorValidar': "1",
				  'cadena': "show",
				  'anoActual': anoActual
		        }
                    	self.response.out.write(template.render(context))

		except ValueError:
            		pass
 
 #Aqui se escribe la liga con la que se llamara a todo este archivo, ira dentro de un atributo llamado action del form
application = webapp2.WSGIApplication([('/validar_inicio_sesion', Validar_inicio_sesion)],debug=True)