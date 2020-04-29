__author__ = 'jslvtr'

import os

URL = os.environ.get('url')
API_KEY = os.environ.get('api')
FROM = os.environ.get('sender_id')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"