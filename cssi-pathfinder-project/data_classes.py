from google.appengine.ext import ndb
class location(ndb.Model):
    pass



class user(ndb.Model):
  pass

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    date_time = ndb.DateTimeProperty()
    email = ndb.StringProperty()
    address = ndb.StringProperty()
    #use GeoPTProperty() when gmaps is set up
    #user_info = ndb.KeyProperty(user)
    description = ndb.StringProperty()
    tags = ndb.StringProperty(repeated = True)
