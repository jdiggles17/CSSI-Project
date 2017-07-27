#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
from data_classes import Event
import datetime
import logging

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #event_list = Event.query().order(date_time)
        template = env.get_template('events.html')
        data = {'events':[{'event_name':'email','address','date_time':},  {'event_name':'email','event_name': 'address',''}]  }
        dummy_dictionary = {
                            "event_name" : "Mike's Movie Night",
                            "date_time" : "December 24th 2017",
                            "email" : "Mike@google.com",
                            "address" : "superfun street 923842",
                        #use GeoPTProperty() when gmaps is set up
                            "user_info" : "joey@gmail.com",
                            "description" : "This is the description",
                            "tags" : "tags go here"

                           }
        dummy_dictionary2 = {
                            "event_name2" : "Mike's Movie Night-2",
                            "date_time2" : "December 24th 2017-2",
                            "email2" : "Mike@google.com-2",
                            "address2" : "superfun street 923842-2",
                        #use GeoPTProperty() when gmaps is set up
                            "user_info2" : "joey@gmail.com-2",
                            "description2" : "This is the description-2",
                            "tags2" : "tags go here-2"

                           }
        master_dictionary = {"":""}
        master_dictionary.update(dummy_dictionary2)
        master_dictionary.update(dummy_dictionary)

        self.response.write(master_dictionary)
        date_and_time = datetime.datetime(2017,3,22,3,30)
        new_event = Event(event_name = "mike's pool",date_time = date_and_time, email ="scoobydew@gmail.com",address = "3234 street name zip code", description = "here is the description", tags = ["tag1", "tag2" ,"tag3"]  )
        new_event_key = new_event.put()

        self.response.write('<br>')
        self.response.write('<br>')
        self.response.write('<br>')
        self.response.write(new_event_key.get())
        self.response.write(template.render())
    def post(self):
        logging.info(self.request.get("date_test"))
        logging.info(self.request.get("time_test"))
        d = datetime.datetime.strptime( (self.request.get("date_test")+ " " + self.request.get("time_test")), "%Y-%m-%d %H:%M" )
        logging.info(d)
        new_event = Events(     event_name = self.request.get('name_test'),
                               date_time = d,

                               email = self.request.get('email_test'),
                               address = self.request.get('address_test'),
                               user_latitude = float(self.request.get('latitude_test')),
                               user_longitude = float(self.request.get('longitude_test')),
                              # user = self.request.get('username'),
                               description = self.request.get('description_test'),
                               tags = ['tag1','tag2'])
        logging.info(new_event)
        new_event_key = new_event.put()
        #add query here'
#commented out merge
        # data_search = Event.query(new_event.date_time>datetime.datetime.now()).sort("date_time")
        # data_results = data_search.fetch(limit = 4)
        # logging.info(dataresults)
        # results_dict = { "event1": data_results[0],
        #               "event2": data_results[1],
        #               "event3": data_results[2],
        #               "event4": data_results[3]
        #               }
        # for event in results_dict:
        #    logging.info(event)
        #
        # template = env.get_template('events.html')
        # self.response.write(new_event)
        # self.response.write(template.render())
#         data_search = Event.query(date_time>datetime.datetime.now()).sort("date_time")
#         data_results = data_search.fetch(limit = 4)
#         logging.info(data_results)
#
#         template = env.get_template('events.html')
#         self.response.write(new_event)
#         self.response.write(template.render({'events' : data_results}))




class MapHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('map.html')

        self.response.write(template.render())
        if self.request.get('type') == "address":
                    new_address_record = AddressRequest(where_test = self.request.get('where_event'))
                    new_address_record.put()
        else:
                    logging.error("Malformed Request!")
class CreateHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('create.html')


        self.response.write(template.render())
    def post(self):
        ate_and_time = datetime.datetime(self.request.get("date_test"))
        new_event = Event(event_name = self.request.get('name_test'),date_time = date_and_time, email =self.request.get('email_test'),address = self.request.get('where_test'), description = self.request.get('where_test'), tags = ["tag1", "tag2" ,"tag3"]  )
        new_event_key = new_event.put()
        self.response.write('<br>')
        self.response.write('<br>')
        self.response.write('<br>')
        self.response.write(new_event_key.get())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/map', MapHandler),
    ('/createevent', CreateHandler)
], debug=True)
