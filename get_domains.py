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
resource = '/config/domain_management/domains'



thing = QRadar_functions.get_stuff(console_url, api_token, resource, '?fields=id,name,description', 'items=0-10')
print(json.dumps(thing, indent=4))

