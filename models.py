from google.appengine.ext import db
from google.appengine.ext import blobstore

class Usuario(db.Model):
#GENERALES
    str_nombre = db.StringProperty()
    str_apellidos = db.StringProperty()
    str_email = db.StringProperty()
    str_password = db.StringProperty()
    #PARA DECIDIR SI FORANEO O ARRENDADOR
    str_tipo = db.StringProperty()
    
    int_nuevo = db.IntegerProperty()
    
    #FORANEO
    str_urlFotoPerfil = db.StringProperty(default = "0")
    int_yearNacimiento = db.StringProperty()
    int_edad = db.StringProperty()
    str_sexo = db.StringProperty()

    str_paisProcedencia = db.StringProperty(default="")
    str_estadoProcedencia = db.StringProperty(default="")
    str_ciudadProcedencia = db.StringProperty(default="")
    
    str_nuevoPais = db.StringProperty(default="")
    str_nuevoEstado = db.StringProperty(default="")
    str_nuevaCiudad = db.StringProperty(default="")

    #ARRENDADOR
    str_nombrePension = db.StringProperty()
    
class Lugar(db.Model):
    str_urlLogo = db.StringProperty(default = "0")
    str_nombrePension = db.StringProperty(required=True)
    str_descripcion = db.StringProperty(required=True)
    
    str_direccion = db.StringProperty(required=True)
    int_telefonoCasa = db.PhoneNumberProperty()
    int_int_telefonoCelular = db.PhoneNumberProperty()
    
    str_urlFotos = db.StringProperty(required=True)
    int_rating = db.IntegerProperty()

class Comentario(db.Model):
    str_foraneo = db.StringProperty(required=True)
    str_arrendador = db.StringProperty(required=True)
    
class UserUpload(db.Model):
    blob = blobstore.BlobReferenceProperty()
