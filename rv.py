from google.appengine.ext import ndb
class RV(ndb.Model):
    rvName = ndb.StringProperty()
    rvUserreview= ndb.StringProperty()
    rvRating = ndb.StringProperty()
