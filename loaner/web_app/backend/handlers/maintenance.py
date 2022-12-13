# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Maintenance handler."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import webapp2

from loaner.web_app import constants
from loaner.web_app.backend.lib import bootstrap


class MaintenanceHandler(webapp2.RequestHandler):
  """Handler for processing requests when app is in maintenance."""

  def get(self):
    """Process GET, serving a static maintenance page."""
    if constants.MAINTENANCE or not bootstrap.is_bootstrap_completed():
      self.response.headers['Content-Type'] = 'text/html'
      self.response.body_file.write(
          constants.JINJA.get_template('maintenance.html').render(
              {'app_name': constants.APP_NAME}))
    else:
      self.redirect('/user')
