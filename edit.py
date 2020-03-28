import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
from Display import DisplayCars
from ev import EV

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True
        )
class Edit_Cars(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        ev_key = ndb.Key('EV',str(self.request.params.items()[0][1]))
        ev = ev_key.get()
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

        template_values = {
        'url' : url,
        'url_string' : url_string,
        'user' : user,
        'ev': ev
        }

        template = JINJA_ENVIRONMENT.get_template('edit.html')
        self.response.write(template.render(template_values))
        #self.response.headers['Content-Type'] = 'text/html'
        #user = users.get_current_user()
        #myuser_key = ndb.Key('MyUser', user.user_id())
        #myuser = myuser_key.get()
        #template_values = {
        #'myuser' : myuser
        #}
        #template = JINJA_ENVIRONMENT.get_template('edit.html')
        #self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
        id = self.request.params.items()[0][1]
        if action == 'Update':
            #evBatterysize = self.request.get('evBatterysize1')
            evBatterysize1=self.request.get('evBatterysize1')
            evWLTPrange1=self.request.get('evWLTPrange1')
            evCost1=self.request.get('evCost1')
            evPower1=self.request.get('evPower1')

            if evBatterysize1:
                ev_key = ndb.Key('EV',id)
                ev = ev_key.get()
                ev.evBatterysize = self.request.get('evBatterysize1')
                ev.put()
                self.redirect('/')
            if evWLTPrange1:
                ev_key = ndb.Key('EV',id)
                ev = ev_key.get()
                ev.evWLTPrange = self.request.get('evWLTPrange1')
                ev.put()
                self.redirect('/')
            if evCost1:
                ev_key = ndb.Key('EV',id)
                ev = ev_key.get()
                ev.evCost = self.request.get('evCost1')
                ev.put()
                self.redirect('/')
            if evPower1:
                ev_key = ndb.Key('EV',id)
                ev = ev_key.get()
                ev.evPower = self.request.get('evPower1')
                ev.put()
                self.redirect('/')

        elif action == 'CANCEL':
            self.redirect('/')

        elif action == 'Delete':
            ev_key = ndb.Key('EV',id)
            ev = ev_key.delete()
            self.redirect('/')



        ###########################################################################################################################
        #self.response.headers['Content-Type'] = 'text/html'
        #if self.request.get('button') == 'Update':
                #user = users.get_current_user()
                #myuser_key = ndb.Key('MyUser', user.user_id())
                #myuser = myuser_key.get()
                #myuser.name = self.request.get('users_name')
                #myuser.age = int(self.request.get('users_age'))
                #myuser.put()
                #self.redirect('/')
        #elif self.request.get('button') == 'Cancel':
            #    self.redirect('/')
