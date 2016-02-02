import jinja2
import os
import webapp2
import models
from webapp2_extras import sessions
import crearSesion
import session_module

from google.appengine.api import users
from google.appengine.ext import db

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))

#Recibimos lo de la sesion_module
class eliminarFotoPerfil(session_module.BaseSessionHandler):
  def post(self):
     #obtener al usuario de la base de datos por medio de la variable de la sesion
    myuser = self.session['usuario']
    miUsuario = db.Query(models.Usuario).filter("str_email", myuser)
    usuario = miUsuario.get()

	#quitamos la url de la foto y ponemos un 0 que significa que no tiene foto y en el html habra una condicion para saber que otra cosa mostrar
    usuario.str_urlFotoPerfil = "0"
    usuario.put()
	#nos redirigimos a configuracion indicando que se hizo una actualizacion
    self.redirect("/configuracionForaneo")

#nombre del controler, clase a la que pertenece, lo de la variable sesion, y ell debug
application = webapp2.WSGIApplication([('/eliminarFotoPerfil', eliminarFotoPerfil)],config = session_module.myconfig_dict,debug=True)
