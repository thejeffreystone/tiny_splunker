#!/usr/bin/env python3
###############################################################################
#   @author         :   Jeffrey Stone 
#   @date           :   03/08/2019
#   @script        	:   toHecWitIt.py
#   @description    :   Simple Python script to send events to Splunk when envoked. AKA Tiny Splunker. 
###############################################################################

import os
import time
import sys
import argparse
import json
import requests
from splunk_http_event_collector import http_event_collector
from dotenv import load_dotenv
load_dotenv()

app_mode = os.getenv("app_mode")

http_event_collector_key = os.getenv("splunk_hec_key")
http_event_collector_host = os.getenv("splunk_server")
http_event_collector_ssl = os.getenv("splunk_hec_ssl")
http_event_collector_port = int(os.getenv("splunk_hec_port"))
splunk_host = os.getenv("splunk_host")
splunk_version = os.getenv("splunk_version")
splunk_source = os.getenv("splunk_source")
splunk_sourcetype = os.getenv("splunk_sourcetype")
splunk_index = os.getenv("splunk_index")

parser = argparse.ArgumentParser(prog='toHecWitIt',epilog='toHecWitIt is part of Tiny Splunker',description='Python based Splunk HEC logger')
parser.add_argument('-i','--idx',help='Splunk Index', required=False)
parser.add_argument('-s','--src',help='Source of Event', required=False)
parser.add_argument('-st','--srctype',help='Event Sourcetype', required=False)
parser.add_argument('-e','--event',help='Event to be logged in json', type=json.loads, required=True)
args = parser.parse_args()

if http_event_collector_ssl == "False":
	http_event_collector_ssl = False
else:
	http_event_collector_ssl = True


# Get Args
if args.idx:
	splunk_index = args.idx
else:
	splunk_index = os.getenv("splunk_index")

if args.src:
	splunk_source = args.src
else:
	splunk_source = os.getenv("splunk_source")

if args.srctype:
	splunk_sourcetype = args.srctype
else:
	splunk_sourcetype = os.getenv("splunk_sourcetype")

def splunkIt():
	# Splunk it
	payload = {}
	payload.update({"index":splunk_index})
	payload.update({"sourcetype":splunk_sourcetype})
	payload.update({"source":splunk_source})
	payload.update({"host":splunk_host})
	payload.update({"event":args.event})

	if splunk_version == 'enterprise':
		logevent = http_event_collector(http_event_collector_key, http_event_collector_host, http_event_port = http_event_collector_port, http_event_server_ssl = http_event_collector_ssl)
		logevent.popNullFields = True
		try:
			logevent.sendEvent(payload)
		except Exception as e:
			print(e)
			sys.exit()
		logevent.flushBatch()

	if splunk_version == 'cloud':
		# Will just post it
		headers = {'Authorization': 'Splunk {}'.format(http_event_collector_key),}
		data = payload
		response = requests.post(http_event_collector_host, headers=headers, data=data)
		print(response)

	print(payload)

def main():
	splunkIt()

if __name__ == "__main__":
    main()

