import webapp2
from webapp2_extras import sessions
import session_module
import models
from google.appengine.ext import db

#recibimos el sesion_module
class crearSesion(session_module.BaseSessionHandler):
    def get(self): 
        #si se intenta crear una sesion y ya existe la variable de una sesion solo imprimimos cual es el usuario de la sesion
        if self.session.get('usuario'):
            print 'Sesion abierta'
            usuario = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
            print ('Nombre Usuario = ' + usuario.get().str_email)
            print ('Nombre = ' + usuario.get().str_nombre.encode('utf-8'))
            print ('Tipo = ' + usuario.get().str_tipo)
        #si no existia, creamos la sesion
        else:
            print 'Sesion creada - Variable de sesion: Usuario'
            #creacion de esa variable, obtenemos que usuario inicio sesion por medio de la variable user que se obtuvo del url
            self.session['usuario'] = self.request.get('user')
            print 'Username session = ' + self.session['usuario']
        #obtenemos la variable py de la url
        py = self.request.get('py')
        #si py es validar, significa que obtuvimos la solicitud de iniciar sesion. redirigimos a la pagina principal
        usuario = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
        if py == "validar":
            if (usuario.get().str_tipo == "foraneo"):
                self.redirect("/inicioForaneo")
            elif (usuario.get().str_tipo == "arrendador"):
                self.redirect("/inicioArrendador")
        elif py == "registrarforaneo":
            self.redirect("/inicioForaneo")
        elif py == "registrararrendador":
            self.redirect("/inicioArrendador")
#End of MainHandler Class
#nombre del controlador, clase a la que pertenece, lo de la sesion y el debug
application = webapp2.WSGIApplication([('/crearSesion', crearSesion),], config = session_module.myconfig_dict, debug=True)