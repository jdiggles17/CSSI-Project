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


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write('Hello world!')
class MapHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("This is the Maps Page")
class CreateHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event( event_name = self.request.get('name'),
                           date = self.request.get('date'),
                           time = self.request.get('time'),
                           email = self.request.get('email'),
                           address = self.request.get('address'),
                           user = self.request.get('username'),
                           description = self.request.get('description'),
                           tags = self.request.get('tag')

        )

        self.response.write("this is the Create Events Page")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/map', MapHandler),
    ('/createevent', CreateHandler)
], debug=True)
