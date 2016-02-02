import datetime
import jinja2
import os
import webapp2
import models
from google.appengine.ext import blobstore
from google.appengine.api import users
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import db 

template_env = jinja2.Environment(
  loader = jinja2.FileSystemLoader(os.getcwd()))

class mostrar(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        #user = users.get_current_user()
        upload_key_str = self.request.params.get('key') 
        upload = None
        if upload_key_str:
            upload = db.get(upload_key_str)  
        if (not upload): 
            self.error(404)
            return 

        self.send_blob(upload.blob)

application = webapp2.WSGIApplication([('/mostrar', mostrar)], debug=True)

