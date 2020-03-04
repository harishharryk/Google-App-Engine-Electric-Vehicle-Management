import webapp2
import jinja2
import random
from datetime import datetime
from refinedsearch import RefinedSearch
from Display import DisplayCars
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV
import os

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class MainPage(webapp2.RequestHandler):
        def get(self):
            self.response.headers['Content-Type'] = 'text/html'
            # URL that will contain a login or logout link
            # and also a string to represent this
            url = ''
            url_string = ''
            # pull the current user from the request
            user = users.get_current_user()

            if user:
                url = users.create_logout_url(self.request.uri)
                url_string = 'logout'
            else:
                url = users.create_login_url(self.request.uri)
                url_string = 'login'
    # generate a map that contains everything that we need to pass to the template
            template_values = {
            'url' : url,
            'url_string' : url_string,
            'user' : user
            }
            # pull the template file and ask jinja to render
    # it with the given template values
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))


        def post(self):
            self.response.headers['Content-Type'] = 'text/html'
            action = self.request.get('button')
            if action == 'Add EV':
                evName = self.request.get('evName')
                evManufacturer = self.request.get('evManufacturer')
                evDateIssued = datetime.strptime(self.request.get('evDateIssued'),'%Y-%m-%d')
                evBatterysize = self.request.get('evBatterysize')
                evWLTPrangemin = self.request.get('evWLTPrangemin')
                evWLTPrangemax = self.request.get('evWLTPrangemax')
                evCost = self.request.get('evCost')
                evPower = self.request.get('evPower')


                myev_key = ndb.Key('EV',evName)
                myev = myev_key.get()
                if myev == None:
                    #,id=evName
                    new_ev = EV(evName=evName,id=evName,evManufacturer=evManufacturer,evDateIssued=evDateIssued,evBatterysize=evBatterysize,evWLTPrangemin=evWLTPrangemin,evWLTPrangemax=evWLTPrangemax,evCost=evCost,evPower=evPower)
                    new_ev.put()
                    message = "EV Added!!"
                else:
                    message = "EV already exists!!"

            template_values = {
                'message': message,
                'all_keys': EV.query().fetch(keys_only=True)
                }
            template = JINJA_ENVIRONMENT.get_template('main.html')
            self.response.write(template.render(template_values))






#app = webapp2.WSGIApplication([
#                ('/', MainPage),
#                ('/refinedSearch',RefinedSearch)
#                ], debug=True)

app = webapp2.WSGIApplication([('/',MainPage),('/refinedSearch',RefinedSearch),('/Display',DisplayCars)],debug = True)
