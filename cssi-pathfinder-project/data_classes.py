from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    date = ndb.DateProperty()
    time = ndb.TimeProperty()
    email = ndb.StringProperty()
    address = ndb.GeoPTProperty()
    user = ndb.StringProperty()
    description = ndb.StringProperty()
    tags = ndb.StringProperty(repeated = True)
