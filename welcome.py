# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

HEADERS = {"Authorization": "Bearer %s" % os.getenv('WRIKE_ACCESS_TOKEN')}

@app.route('/')
def welcome():
    """display ibmcode challenge status"""

    # Found project IDs by querying https://www.wrike.com/api/v3/folders -- but
    # saved them as environment variables instead of performing the same query
    # a bunch of times
    journey_url = 'https://www.wrike.com/api/v3/folders/%s/tasks' % os.getenv("JOURNEY_ID")
    completed_journeys = 0
    previously_completed_journeys = 58  # Number when challenge started

    data = requests.get(journey_url, headers=HEADERS).json()['data']
    for entry in data:
        if entry['status'] == 'Completed':
            completed_journeys += 1

    completed_challenge_journeys = completed_journeys - previously_completed_journeys

    howto_url = 'https://www.wrike.com/api/v3/folders/%s/tasks' % os.getenv("HOWTO_ID")
    completed_howtos = 0
    data = requests.get(howto_url, headers=HEADERS).json()['data']
    for entry in data:
        if entry['status'] == 'Completed':
            completed_howtos += 1

    return render_template('index.html', completed_challenge_journeys=completed_challenge_journeys,
                                         completed_howtos=completed_howtos)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
