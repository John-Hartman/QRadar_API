#!/usr/bin/python3

import requests
import urllib3
import json
import creds
from qradar_functions import QRadar_functions
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import logger_utility
from logger import Logger

################################
# Starting the logger
logger_utility.setup_logging()
logger = Logger().logger

################################
# Starting Variables
console_url = creds.console
api_token = creds.token
resource = '/config/event_sources/log_source_management/log_sources'



thing = QRadar_functions.get_stuff(console_url, api_token, resource, '?fields=id,name,description,status&filter=status(status)=ERROR and internal=false', 'items=0-5000')
print(json.dumps(thing, indent=4))

