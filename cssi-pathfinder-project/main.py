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

env=jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #event_list = Event.query().order(date_time)
        template = env.get_template('events.html')
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
      for term in dummy_dictionary:
          master_dictionary.append(term)

        self.response.write(master_dictionary)
class MapHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the Maps Page")
class CreateHandler(webapp2.RequestHandler):
    def get(self):
        # new_event = Event( event_name = self.request.get('name'),
        #                    date = self.request.get('date'),
        #                    time = self.request.get('time'),
        #                    email = self.request.get('email'),
        #                    address = self.request.get('address'),
        #                    user = self.request.get('username'),
        #                    description = self.request.get('description'),
        #                    tags = self.request.get('tag')

        self.response.write("this is the Create Events Page")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/map', MapHandler),
    ('/createevent', CreateHandler)
], debug=True)
