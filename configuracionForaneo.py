# coding= utf-8
# coding= ascii
import jinja2
import os
import webapp2
from webapp2_extras import sessions
import crearSesion
import session_module
from google.appengine.ext import blobstore
import models
from google.appengine.ext import db

#recibe la sesion y webapp2
class configuracionForaneo(session_module.BaseSessionHandler, webapp2.RequestHandler):
    def get(self): 
        #Sino existe una sesion redireccionamos al controler main.py
        if not self.session.get('usuario'):
            self.redirect("/")
            #si existe la sesion, imprimos que sesion es
        else:
            usr = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
            tipo = usr.get().str_tipo
            print(tipo)

            if (tipo == "foraneo"):
                nombreS = usr.get().str_email
                nombre = usr.get().str_nombre
                print(nombreS)
                print(nombre.encode('utf-8'))

                template = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
                template = template.get_template("configuracion.html")
                
                upload_url = blobstore.create_upload_url('/cargarArchivo?file=fotoperfil')
                context = {
                    'nombre': 'Bienvenido, ' + nombre,
                    'correo': usr,
                    'upload_url': upload_url
                }
                #self.response.out.write('Bienvenido, ' + nombre)
                self.response.out.write(template.render(context))
                #self.response.out.write('Usuario = ' + self.session['usuario'])
            else:
                self.redirect("/inicioArrendador")
            
#controler, clase, sesion, debug
application = webapp2.WSGIApplication([('/configuracionForaneo', configuracionForaneo),], config = session_module.myconfig_dict, debug=True)
