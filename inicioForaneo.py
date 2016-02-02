# coding= utf-8
# coding= ascii
import jinja2
import os
import webapp2
from webapp2_extras import sessions
import crearSesion
import session_module
import models
from google.appengine.ext import db

#recibe la sesion y webapp2
class inicioForaneo(session_module.BaseSessionHandler, webapp2.RequestHandler):
    def get(self): 
        #Sino existe una sesion redireccionamos al controler main.py
        if not self.session.get('usuario'):
            self.redirect("/")
            #si existe la sesion, imprimos que sesion es
        else:
            correo = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
            tipo = correo.get().str_tipo
            print(tipo)

            if (tipo == "foraneo"):     #Validamos que ingrese el tipo correcto de usuario
                nombreS = correo.get().str_email
                nombre = correo.get().str_nombre
                
                template = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
                template = template.get_template("inicioForaneo.html")
                print(nombreS)
                print(nombre.encode('utf-8'))
                context = {
                    'nombre': 'Bienvenido, ' + nombre
                }
                #self.response.out.write('Bienvenido, ' + nombre)
                self.response.out.write(template.render(context))
                #self.response.out.write('Usuario = ' + self.session['usuario'])
            
            else:
                self.redirect("/inicioArrendador")
                #print ("There are not your domains. Go back to where you are.")

#controler, clase, sesion, debug
application = webapp2.WSGIApplication([('/inicioForaneo', inicioForaneo),], config = session_module.myconfig_dict, debug=True)
