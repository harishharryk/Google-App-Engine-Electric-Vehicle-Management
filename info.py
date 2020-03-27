import webapp2
import os
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV
from myuser import MyUser
from ev import RV

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class Info(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        Message = "Welcome to the search page"
        template_values = {
        'message' : Message
        }

        template = JINJA_ENVIRONMENT.get_template('info.html')
        self.response.write(template.render(template_values))
        #all_keys = EV.query().fetch(keys_only=True)

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action=self.request.get('button')
        query_list = EV.query(EV.evReview.rvRating>1).fetch()
        if action=='Retrive':
            query_list = EV.query().fetch()
            #max_review = max(EV.evReview.rvRating)
            #rv_Avg=Sum(query_list)/len(query_list)

            #for ev in query_list:
                #self.response.write(ev.rvName + '<br/>')

        template_values ={
        'all_rv_keys':query_list
        #'all_rv_keys':ev.evReview

        }
        template = JINJA_ENVIRONMENT.get_template('info.html')
        self.response.write(template.render(template_values))
