from google.appengine.ext import ndb
class MyUser(ndb.Model):
    username = ndb.StringProperty()
    
    email_address = ndb.StringProperty()
    user_review = ndb.StringProperty()
