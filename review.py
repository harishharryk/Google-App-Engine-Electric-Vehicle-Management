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
        id=self.request.params.items()[0][1]
        #all_keys = EV.query()


        if action == 'Add Reviews':
            #rvName=id
            rvName = self.request.get('evName1')
            #rvName = self.request.get(str(self.request.params.items()[0][1]))
            #rvUserreview=[]
            rvUserreview = self.request.get('rvUserreview')
            #evDateIssued = datetime.strptime(self.request.get('evDateIssued'),'%Y')
            #rvRating=[]
            rvRating = self.request.get('rvRating')



            #if rvUserreview:
            ev_key = ndb.Key('EV',id)
            ev = ev_key.get()
            new_review=RV(rvName=rvName,rvUserreview=rvUserreview,rvRating=int(rvRating))
            ev.evReview.append(new_review)
            ev.put()

            #rv_key = ndb.Key('RV',id)
            #rv = rv_key.get()
        ##################3
            #i=0
            #for i in ev.evReview.rvRating:
                #if ev.evReview.rvRating >0:
                    #rvAvg=sum(ev.evReview.rvRating)/len(ev.evReview.rvRating)
                    #new_avg=RV(rvAvg=rvAvg)
                    #ev.evReview.append(new_avg)
                    #ev.put()

            #self.redirect('/')

            #if rvRating:
                #ev_key = ndb.Key('EV',id)
                #ev = ev_key.get()
                #new_rating=RV(rvRating=rvRating)
                #ev.evReview.append([new_rating])
                #ev.put()
                #self.redirect('/')

            #all_rv_keys = RV.query()
            #query = RV.query(RV.rvName == 'rvName1').fetch()



        template_values = {
            #'message': message,
            'all_rv_keys':ev.evReview,
            #'all_rv_keys':all_keys,
            'evname':self.request.get(str(self.request.params.items()[0][1]))
            #'all_keys': RV.query().fetch(keys_only=True)
            }
        template = JINJA_ENVIRONMENT.get_template('review.html')
        self.response.write(template.render(template_values))
