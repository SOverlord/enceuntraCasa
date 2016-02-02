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

class actualizarPerfil(session_module.BaseSessionHandler, webapp2.RequestHandler):
    def post(self):
        #Recuperamos la informacion del HTML y la almacenamos en variables locales
        nombre = self.request.get('nombre')
        apellidos = self.request.get('apellidos')
        edad = self.request.get('edad')
        procedencia = self.request.get('estado')
        sexo = self.request.get('sexo')
        
        usr = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
        
        #Almacenamos el contenido de las variables locales en la base de datos
        usuarioF = usr.get()
        usuarioF.str_nombre = nombre
        usuarioF.str_apellidos = apellidos
        usuarioF.int_edad = edad
        usuarioF.str_estadoProcedencia = procedencia
        usuarioF.str_sexo = sexo
        usuarioF.put()
            
        #Despues de haber registrado nos dirigimos al controler de crearSesion (dentro de este se redireccionara a configuracion)
        if usuarioF.str_tipo == "foraneo":
            self.redirect("/inicioForaneo")
        elif usuarioF.str_tipo == "arrendador":
            self.redirect("/inicioArrendador")
	
#controler, clase, debug
application = webapp2.WSGIApplication([('/actualizarPerfil', actualizarPerfil)],config = session_module.myconfig_dict,debug=True)
