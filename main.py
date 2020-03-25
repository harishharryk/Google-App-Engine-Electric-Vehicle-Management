import webapp2
import jinja2
import random
from datetime import datetime
from refinedsearch import RefinedSearch
from Display import DisplayCars
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from ev import EV
from ev import RV
from edit import Edit_Cars
from compare import Compare
from comparecars import CompareCars
from review import Review
from info import Info
import os

JINJA_ENVIRONMENT = jinja2.Environment(
loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],
autoescape=True
)

class MainPage(webapp2.RequestHandler):
        def get(self):
            self.response.headers['Content-Type'] = 'text/html'
            user = users.get_current_user()
            if user == None:
                template_values = {
                'login_url' : users.create_login_url(self.request.uri)
                }
                template = JINJA_ENVIRONMENT.get_template('first_mainpage.html')
                self.response.write(template.render(template_values))
                return
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            if myuser == None:
                myuser = MyUser(id=user.user_id(),username=user.email(),email_address=user.email())
                myuser.put()
            #all_keys = EV.query().fetch(keys_only = True)
            template_values = {
                'logout_url' : users.create_logout_url(self.request.uri),
                'username':user,
                #'all_keys' : all_keys,
                'message':"Add EVs"
                }
            #self.response.headers['Content-Type'] = 'text/html'
            # URL that will contain a login or logout link
            # and also a string to represent this
            #url = ''
            #url_string = ''
            # pull the current user from the request
            #user = users.get_current_user()

            #if user:
                #url = users.create_logout_url(self.request.uri)
                #url_string = 'logout'
            #else:
                #url = users.create_login_url(self.request.uri)
                #url_string = 'login'
    # generate a map that contains everything that we need to pass to the template
            #template_values = {
            #'url' : url,
            #'url_string' : url_string,
            #'user' : user
            #}
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
                #evDateIssued = datetime.strptime(self.request.get('evDateIssued'),'%Y')
                evDateIssued = self.request.get('evDateIssued')
                evBatterysize = self.request.get('evBatterysize')
                evWLTPrange = self.request.get('evWLTPrange')
                #evWLTPrangemax = self.request.get('evWLTPrangemax')
                evCost = self.request.get('evCost')
                evPower = self.request.get('evPower')


                myev_key = ndb.Key('EV',evName)
                myev = myev_key.get()
                if myev == None:
                    #,id=evName
                    new_ev = EV(evName=evName,id=evName,evManufacturer=evManufacturer,evDateIssued=evDateIssued,evBatterysize=evBatterysize,evWLTPrange=evWLTPrange,evCost=evCost,evPower=evPower)
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

app = webapp2.WSGIApplication([('/',MainPage),('/refinedSearch',RefinedSearch),('/Display',DisplayCars),('/edit',Edit_Cars),('/compare',Compare),('/compareCars',CompareCars),('/review',Review),('/info',Info)],debug = True)
