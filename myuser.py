from google.appengine.ext import ndb
class MyUser(ndb.Model):
    name = ndb.StringProperty()
    # email address of this user
    email_address = ndb.StringProperty()
    #age = ndb.IntegerProperty()
