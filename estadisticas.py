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
class estadisticas(session_module.BaseSessionHandler, webapp2.RequestHandler):
		def get(self):
			h = db.Query(models.Usuario).filter("str_sexo", "masculino")
			muj = db.Query(models.Usuario).filter("str_sexo", "femenino")
			proc = db.Query(models.Usuario).filter("str_estadoProcedencia", "Veracruz")
			fora = db.Query(models.Usuario).filter("str_tipo", "foraneo")
			arr = db.Query(models.Usuario).filter("str_tipo", "arrendador")
			fot = db.Query(models.Usuario).filter("str_urlFotoPerfil", "0")
	
			self.response.out.write("<h1>Estadisticas en EncuentraCasa</h1><br>")
			
			i = 0
			for foraneo in fora:
				i = i + 1
			self.response.out.write("No. de foraneos: " + str(i) + "<br>");
			i = 0
			for arrendador in arr:
				i = i + 1
			self.response.out.write("No. de arrendadores: " + str(i) + "<br>");
			self.response.out.write("------------------------------------------<br><br>");
			i = 0
			for hombres in h:
				i = i + 1
			self.response.out.write("No. de hombres: " + str(i) + "<br>");
			i = 0
			for mujeres in muj:
				i = i + 1
			self.response.out.write("No. de mujeres: " + str(i)+ "<br>");
			self.response.out.write("------------------------------------------<br><br>");
			i = 0
			for veracruz in proc:
				i = i + 1
			self.response.out.write("No. de personas procedentes de Veracruz: " + str(i) + "<br>");
			i = 0
			self.response.out.write("------------------------------------------<br><br>");
			for foto in fot:
				if not foto.str_urlFotoPerfil == "0":
					i = i + 1
			self.response.out.write("No. de blobs: " + str(i)+ "<br>");
#controler, clase, sesion, debug
application = webapp2.WSGIApplication([('/estadisticas', estadisticas),], config = session_module.myconfig_dict, debug=True)
