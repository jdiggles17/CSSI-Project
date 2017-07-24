from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    date = ndb.DateProperty()
    
