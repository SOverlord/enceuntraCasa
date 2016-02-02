import jinja2
import os
import webapp2
import models

from webapp2_extras import sessions
import crearSesion
import session_module

from google.appengine.ext import blobstore
from google.appengine.api import users
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import db

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))

class CargarArchivo(session_module.BaseSessionHandler, blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        #iniciamos esta variable que almacenara el key del objeto blob
        blob_key = ''
        #'upload' es el nombre de la variable html que recibe el archivo
        for blob_info in self.get_uploads('upload'):
            #almacenamos la key obtenida
            blob_key = blob_info.key()
            #guardamos el archivo en un objeto userupload
            upload = models.UserUpload(blob = blob_key)
            upload.put()
            #buscamos el archivo en la base de datos, objeto userupload
            
            key_blob = 'x'
            myblob = db.Query(models.UserUpload).filter("blob", key_blob)
            myb = myblob.get()
            key_blob = upload.key()
            archivo = self.request.get('file')
            if archivo == "fotoperfil":
                myFlyer = db.Query(models.Usuario).filter("str_email", self.session['usuario'])
                flyer = myFlyer.get()
                flyer.str_urlFotoPerfil = str(key_blob)
                flyer.put()
                self.redirect("/configuracionForaneo")
        
application = webapp2.WSGIApplication([('/cargarArchivo', CargarArchivo)], config = session_module.myconfig_dict, debug=True)