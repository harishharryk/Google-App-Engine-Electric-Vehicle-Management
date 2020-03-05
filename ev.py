from google.appengine.ext import ndb
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
    # evID = ndb.StringProperty()
    #evFeature = ndb.StructuredProperty(GPUFeatures)
