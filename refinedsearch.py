import webapp2
import os
import jinja2
#from google.cloud import bigquery
from google.appengine.ext import ndb
from google.appengine.api import users
from ev import EV
from Display import DisplayCars

#
# from main import MainPage

JINJA_ENVIRONMENT = jinja2.Environment(
loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions = ['jinja2.ext.autoescape'],
autoescape = True
)

class RefinedSearch(webapp2.RequestHandler):
    #def get(self):
        # self.response.write("Hello, webapp2!")
        #self.response.headers['Content-Type'] = 'text/html'
        #Message = "Welcome to the search page"
        #self.response.write('Cars with less than range<br/>')
        #query = EV.query(EV.evWLTPrangemin < 'car_range').fetch()
        #for i in query:
            #self.response.write(i.evName + '<br/>')
        #self.response.write('cars less or higher with  four attempts<br/>')
        #query1 = EV.query(EV.evWLTPrangemin >= 'car_range').fetch(keys_only=True)
        #query2 = EV.query(EV.evWLTPrangemin < 'car_range').fetch(keys_only=True)
        #total_query = ndb.get_multi(set(query1).intersection(query2))
        #for i in total_query:
            #self.response.write(i.evName + '<br/>')
    def get(self):
        # self.response.write("Hello, webapp2!")
        self.response.headers['Content-Type'] = 'text/html'
        Message = "Welcome to the search page"
        template_values = {
        'message' : Message
        }

        template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
        self.response.write(template.render(template_values))

        #template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
        #self.response.write(template.render(template_values))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        action=self.request.get('button')
        query_list = EV.query()
                #action = self.request.get('name_search')

                #check=EV.query()
        if action=='Search':
            name_search=self.request.get('name_search')
            man_search=self.request.get('man_search')
            #datetime.strptime(self.request.get('evDateIssued'),'%Y')
            yr_min_search=self.request.get('yr_min_search')
            yr_max_search=self.request.get('yr_max_search')
            Bat_min_search=self.request.get('Bat_min_search')
            Bat_max_search=self.request.get('Bat_max_search')
            Wltp_min_search=self.request.get('Wltp_min_search')
            Wltp_max_search=self.request.get('Wltp_max_search')
            Cost_min_search=self.request.get('Cost_min_search')
            Cost_max_search=self.request.get('Cost_max_search')
            Power_min_search=self.request.get('Power_min_search')
            Power_max_search=self.request.get('Power_max_search')
            query_list = EV.query()
            if name_search:
                query_list=query_list.filter(EV.evName == name_search)

            if man_search:
                query_list=query_list.filter(EV.evManufacturer == man_search)

            if yr_min_search and yr_max_search:
                query_list=query_list.filter(EV.evDateIssued >= yr_min_search and EV.evDateIssued < yr_max_search)

            if Bat_min_search and Bat_max_search:
                query_list=query_list.filter(EV.evBatterysize >= Bat_min_search and EV.evBatterysize < Bat_max_search)
                        #if Bat_search:
                        #    query_list=query_list.filter(EV.evManufacturer == Bat_search).fetch(keys_only=True)
            if Wltp_min_search and Wltp_max_search:
                query_list=query_list.filter(EV.evWLTPrange >=Wltp_min_search  and EV.evWLTPrange < Wltp_max_search)

            if Cost_min_search and Cost_max_search:
                query_list=query_list.filter(EV.evCost >=Cost_min_search  and EV.evCost < Cost_max_search)

            if Power_min_search and Power_max_search:
                query_list=query_list.filter(EV.evPower >= Power_min_search and EV.evPower < Power_max_search)


            template_values ={
            'all_keys':query_list
            }
            template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
            self.response.write(template.render(template_values))

        elif action == 'CANCEL':
            self.redirect('/')
        else:
            message = "fail"
            template_values= {'message':message}
            template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
            self.response.write(template.render(template_values))






                    #if self.request.get('name_search'):
                    #    action=self.request.get('name_search')
                    #    check=EV.query().filter(EV.evName == action).fetch(keys_only=True)
                    #elif self.request.get('man_search'):
                    #    action=self.request.get('man_search')
                    #    check=EV.query().filter(EV.evManufacturer == action).fetch(keys_only=True)
                    #elif self.request.get('Bat_search'):
                    #    action=self.request.get('Bat_search')
                    #    check=EV.query().filter(EV.evBatterysize == action).fetch(keys_only=True)
                    #elif self.request.get('Wltp_min_search') and self.request.get('Wltp_max_search'):
                    #    x=self.request.get('Wltp_min_search')
                    #    y=self.request.get('Wltp_max_search')
                        #action=self.request.get('Wltp_min_search')
                    #    check=EV.query().filter(EV.evWLTPrange >= x and EV.evWLTPrange < y ).fetch(keys_only=True)
                    #elif self.request.get('Wltp_max_search'):
                    #    action=self.request.get('Wltp_max_search')
                    #    check=EV.query().filter(EV.evWLTPrange < action).fetch(keys_only=True)
                    #elif self.request.get('Cost_search'):
                        #action=self.request.get('Cost_search')
                        #check=EV.query().filter(EV.evCost <= action).fetch(keys_only=True)
                    #else:
                        #action=self.request.get('Power_search')
                        #check=EV.query().filter(EV.evPower <= action).fetch(keys_only=True)

                    #form=refinedSearch.FieldStorage()
                    #searchterm=form.getvalue('search')
                    #action = self.request.get('search')
                    #check = EV.query().filter(ndb.GenericProperty("evName") == action).get()
                        #check=EV.query().filter(EV.evName == action).fetch(keys_only=True)---------------"take this"-----------------


                    #if len(check) == 0:
                    #        message = "fail"
                            #self.response.write('populating<br/>')
                            #self.initDB()
                    #        template_values= {'message':message}
                    #        template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
                    #        self.response.write(template.render(template_values))
                    #else:
                    #        PAGE_SIZE=50
                    #        list=EV.query().fetch_page(PAGE_SIZE)
                    #        search_key = ndb.Key('EV',check[0].id())
                    #        searched_profile = search_key.get()
                    #        message = "success"
                            #template_values= {'search':action,'message':message,'EV':searched_profile}
                    #        template_values= {'list':list,'check':check,'message':message,'EV':searched_profile}
                    #        template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
                    #        self.response.write(template.render(template_values))
                ######################################################################################

                        #if action == 'search':

                        #        query_list = EV.query()
                        #        query_list = query_list.filter(EV.evName)
                        #        template_values = {
                        #        'all_keys': query_list
                        #        }

                        #        template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
                        #        self.response.write(template.render(template_values))

                        #else:
                        #        message = "fail"
                        #        template_values= {'message':message}
                        #        template = JINJA_ENVIRONMENT.get_template('refinedSearch.html')
                        #        self.response.write(template.render(template_values))

                            #search_key=ndb.key('EV','action')
                            #searched=search_key.get()
                            #message = "success"
                            #template_values ={
                            #'search': action,'message':message,'EV':searched
                            #    }


                        #if action == 'CANCEL':
                        #    self.redirect('/')
