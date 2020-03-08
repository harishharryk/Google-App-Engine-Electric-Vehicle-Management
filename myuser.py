from google.appengine.ext import ndb
class MyUser(ndb.Model):
    username = ndb.StringProperty()
    # email address of this user
    email_address = ndb.StringProperty()
    user_review = ndb.StringProperty()
    #age = ndb.IntegerProperty()
