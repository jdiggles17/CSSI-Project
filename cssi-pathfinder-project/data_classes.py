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
    user_latitude = ndb.FloatProperty()
    user_longitude = ndb.FloatProperty()
    #user_info = ndb.KeyProperty(user)
    description = ndb.StringProperty()
    tags = ndb.StringProperty(repeated = True)

    @classmethod
    def future_event_query(cls, now):
        return cls.query(cls.date_time >= now).order(cls.date_time)
