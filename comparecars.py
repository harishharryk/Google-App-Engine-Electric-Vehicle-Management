import webapp2
import os
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class CompareCars(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        ev_key2 = ndb.Key('EV',str(self.request.params.items()[1][1]))
        ev2 = ev_key2.get()

        ev_key1 = ndb.Key('EV',str(self.request.params.items()[0][1]))
        ev1 = ev_key1.get()

        if ev1 == None:
            ev1 = ev_key2.get()

        ev1_evPower_color=ev2_evPower_color=ev2_Batterysize_color=ev1_Batterysize_color=ev2_evWLTPrange_color=ev1_evWLTPrange_color="black"
        ev2_evCost_color=ev1_evCost_color="black"

        if ev2.evBatterysize < ev1.evBatterysize:
            ev2_Batterysize_color="red"
            ev1_Batterysize_color="green"
        elif ev2.evBatterysize > ev1.evBatterysize:
            ev2_Batterysize_color="green"
            ev1_Batterysize_color="red"
        else:
            ev1_Batterysize_color=ev2_color="black"

        if ev2.evWLTPrange < ev1.evWLTPrange:
            ev2_evWLTPrange_color="red"
            ev1_evWLTPrange_color="green"
        elif ev2.evWLTPrange > ev1.evWLTPrange:
            ev2_evWLTPrange_color="green"
            ev1_evWLTPrange_color="red"
        else:
            ev1_evWLTPrange_color=ev2_color="black"

        if ev2.evPower < ev1.evPower:
            ev2_evPower_color="red"
            ev1_evPower_color="green"
        elif ev2.evPower > ev1.evPower:
            ev2_evPower_color="green"
            ev1_evPower_color="red"
        else:
            ev1_evPower_color=ev2_evPower_color="black"

        if ev2.evCost < ev1.evCost:
            ev2_evCost_color="green"
            ev1_evCost_color="red"
        elif ev2.evCost > ev1.evCost:
            ev2_evCost_color="red"
            ev1_evCost_color="green"
        else:
            ev1_evCost_color=ev2_evCost_color="black"


        template_values = {
        'ev1':ev1,
        'ev2':ev2,
        'ev1_Batterysize_color':ev1_Batterysize_color,
        'ev2_Batterysize_color':ev2_Batterysize_color,
        'ev1_evWLTPrange_color':ev1_evWLTPrange_color,
        'ev2_evWLTPrange_color':ev2_evWLTPrange_color,
        'ev1_evPower_color':ev1_evPower_color,
        'ev2_evPower_color':ev2_evPower_color,
        'ev1_evCost_color':ev1_evCost_color,
        'ev2_evCost_color':ev2_evCost_color
        }
        template = JINJA_ENVIRONMENT.get_template('CompareCars.html')
        self.response.write(template.render(template_values))
