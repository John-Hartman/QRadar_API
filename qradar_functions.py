#!/usr/bin/python3

import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import logger_utility
from logger import Logger

# Starting the logger
logger_utility.setup_logging()
logger = Logger().logger

class QRadar_functions:

	def get_stuff(console_url, creds, resource, params, range_num):
		url = f"https://{console_url}/api{resource}{params}"
		payload={}
		headers = {
		  'Accept': 'application/json',
		  'Range': range_num,
		  'SEC': creds
		}
		response = requests.request("GET", url, headers=headers, data=payload, verify=False)
		json_text = response.text
		parsed = json.loads(json_text)
		return parsed

	def post_stuff(console_url, creds, resource, params, in_payload):
		url = f"https://{console_url}/api{resource}{params}"
		payload= in_payload
		headers = {
		  'Content-Type': 'application/json',
		  'Accept': 'application/json',
		  'SEC': creds
		}
		response = requests.request("POST", url, headers=headers, data=payload, verify=False)
		json_text = response.text
		parsed = json.loads(json_text)
		if response.status_code == 201:
			id_num = parsed['id']
			return id_num
		else:
			err_msg = response.text
			this_stuff = json.loads(err_msg)
			msg = (f"ERROR {response.status_code} - {this_stuff['message']}")
			return msg

	def put_stuff(console_url, creds, resource, params, in_payload):
		url = f"https://{console_url}/api{resource}{params}"
		payload= in_payload
		headers = {
		  'Content-Type': 'application/json',
		  'Accept': 'application/json',
		  'SEC': creds
		}
		response = requests.request("PUT", url, headers=headers, data=payload, verify=False)
		json_text = response.text
		parsed = json.loads(json_text)
		return parsed

	
