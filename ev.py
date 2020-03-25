from google.appengine.ext import ndb
class RV(ndb.Model):
    rvUserreview= ndb.StringProperty()
    #rvRating = ndb.StringProperty()
    rvRating = ndb.IntegerProperty()
    rvName = ndb.StringProperty()
    rvAvg=ndb.StringProperty()
    #rvSum=ndb.FloatProperty()
    #rvLen=ndb.FloatProperty()

class EV(ndb.Model):
    evName = ndb.StringProperty()
    evManufacturer = ndb.StringProperty()
    evDateIssued = ndb.StringProperty()
    evBatterysize = ndb.StringProperty()
    #evBatterysize = ndb.number()
    evWLTPrange = ndb.StringProperty()
    #evWLTPrangemax = ndb.StringProperty()
    evCost = ndb.StringProperty()
    evPower = ndb.StringProperty()
    evReview=ndb.StructuredProperty(RV,repeated = True)

    #evRating = ndb.StringProperty()
    #evuser_review = ndb.StringProperty()
