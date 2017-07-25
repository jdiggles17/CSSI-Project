from google.appengine.ext import ndb
class location(ndb.Model):
    pass
class tags(ndb.Model):
    pass
class date_and_time(ndb.Model):
    pass
class user(ndb.Model):
    pass

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    date_time = ndb.KeyProperty(date_time)
    email = ndb.StringProperty()
    address = ndb.KeyProperty(location)
    #use GeoPTProperty() when gmaps is set up
    user_info = ndb.KeyProperty(user)
    description = ndb.StringProperty()
    tags = ndb.KeyProperty(tags)
