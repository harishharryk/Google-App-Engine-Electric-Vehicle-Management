import webapp2
import os
import jinja2
#from google.cloud import bigquery
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class DisplayCars(webapp2.RequestHandler):
        def post(self):
        # self.response.write("Hello, webapp2!")
            self.response.headers['Content-Type'] = 'text/html'
            Message = "Welcome page"
            template_values = {
            'message' : Message
            }

            template = JINJA_ENVIRONMENT.get_template('Display.html')
            self.response.write(template.render(template_values))
