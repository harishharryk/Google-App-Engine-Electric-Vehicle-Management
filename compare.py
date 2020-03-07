import webapp2
import os
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV
#
# from main import MainPage

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class Compare(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        all_keys = EV.query().fetch(keys_only=True)
        template_values = {
        'all_keys':all_keys
        }
        template = JINJA_ENVIRONMENT.get_template('compare.html')
        self.response.write(template.render(template_values))
