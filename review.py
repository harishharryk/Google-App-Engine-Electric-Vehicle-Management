import webapp2
import os
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV
from myuser import MyUser
from rv import RV
#
# from main import MainPage

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class Review(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        ev_key = ndb.Key('EV',str(self.request.params.items()[0][1]))
        #ev_key = ndb.Key('EV',id)
        ev = ev_key.get()
        all_keys = EV.query().fetch(keys_only=True)
        #all_rv_keys = RV.query().fetch(keys_only=True)
        user = users.get_current_user()
        #query_list = EV.query()

        template_values = {
        'all_keys':all_keys,
        'Current_user':user,
        'ev':ev

        }
        template = JINJA_ENVIRONMENT.get_template('review.html')
        self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action = self.request.get('button')
    

        if action == 'Add Reviews':
            rvName = self.request.get('rvName')
            #rvName = self.request.get(str(self.request.params.items()[0][1]))
            rvUserreview = self.request.get('rvUserreview')
            #evDateIssued = datetime.strptime(self.request.get('evDateIssued'),'%Y')
            rvRating = self.request.get('rvRating')

            myrv_key = ndb.Key('RV',rvName)
            myrv = myrv_key.get()
            #all_rv_keys = RV.query()
            if myrv == None:
                #,id=evName
                new_rv = RV(rvName=rvName,rvUserreview=rvUserreview,rvRating=rvRating)
                new_rv.put()
                message = "RV Added!!"
                all_rv_keys = RV.query()
            else:
                #message = "EV already exists!!"
                new_rv = RV(rvName=rvName,rvUserreview=rvUserreview,rvRating=rvRating)
                new_rv.put()
                message = "RV Added!!"
                all_rv_keys = RV.query()

        template_values = {
            'message': message,
            'all_rv_keys':all_rv_keys
            #'all_keys': RV.query().fetch(keys_only=True)
            }
        template = JINJA_ENVIRONMENT.get_template('review.html')
        self.response.write(template.render(template_values))
