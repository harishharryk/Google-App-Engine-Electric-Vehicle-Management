from google.appengine.ext import ndb
class EV(ndb.Model):
    evName = ndb.StringProperty()
    evManufacturer = ndb.StringProperty()
    evDateIssued = ndb.DateProperty()
    evBatterysize = ndb.StringProperty()
    #evBatterysize = ndb.number()
    evWLTPrangemin = ndb.StringProperty()
    evWLTPrangemax = ndb.StringProperty()
    evCost = ndb.StringProperty()
    evPower = ndb.StringProperty()
    # evID = ndb.StringProperty()
    #evFeature = ndb.StructuredProperty(GPUFeatures)
