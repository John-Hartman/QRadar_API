#!/usr/bin/python3

import requests
import urllib3
import json
import creds
import os
import pandas as pd
from datetime import datetime
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
item_range = 'items=0-10'
# Put in whatever IDs you want for the parameter
params = 'fields=name,id,average_eps,status(status,messages(text))&filter=id IN (1, 2, 3, 4)'
out_file = '/Directory_of_your_choice/log_source_status - '+datetime.now().strftime("%m%d%Y-%I%M%p")+'.csv'

################################
# Doing the stuff
thing = QRadar_functions.get_stuff(console_url, api_token, resource, params, item_range)
thing_json = (json.dumps(thing, indent=4))
load_json = json.loads(thing_json)
json_body = pd.json_normalize(load_json)
#df=pd.read_json("thing_json")

json_body.to_csv(out_file, encoding='utf-8', index=False)



