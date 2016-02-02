import jinja2
import os
import webapp2
from webapp2_extras import sessions
import crearSesion
import session_module
import models
from google.appengine.ext import db

#recibe la sesion y webapp2
class publicarNuevo(session_module.BaseSessionHandler, webapp2.RequestHandler):
    def get(self): 
        #Sino existe una sesion redireccionamos al controler main.py
        if not self.session.get('usuario'):
            self.redirect("/")
            #si existe la sesion, imprimos que sesion es
        else:
            correo = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
            tipo = correo.get().str_tipo

            if (tipo == "arrendador"):     #Validamos que ingrese el tipo correcto de usuario
                template = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))            
                nombreS = correo.get().str_email
                nombre = correo.get().str_nombre            
            
                template = template.get_template("publicarNuevo.html")            
                print(nombreS)
                print(nombre.encode('utf-8'))
                print(tipo)
                context = {
                    'nombre': 'Bienvenido, ' + nombre
                }
                #self.response.out.write('Bienvenido, ' + nombre)
                self.response.out.write(template.render(context))
                #self.response.out.write('Usuario = ' + self.session['usuario'])
            else:
                self.redirect("/inicioForaneo")

#controler, clase, sesion, debug
application = webapp2.WSGIApplication([('/publicarNuevo', publicarNuevo),], config = session_module.myconfig_dict, debug=True)
