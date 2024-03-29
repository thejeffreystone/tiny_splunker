# To Hec Wit It - Tiny Splunker

tohecwitit.py is a tiny python script with the single job of publishing a log event to Splunk's HTTP Event Collector.

## Installation
* Clone this repo
 - `git clone https://github.com/thejeffreystone/tiny_splunker`
* cd to dir `tiny_splunker`
* install required python libraries
 - `pip install -r requirements.txt`
 - `pip install git+git://github.com/georgestarcher/Splunk-Class-httpevent.git`
* cp env-sample to .env
 - `cp env-sample .env`
* Modify .env to match your environmnt:
```
# Splunk Version:
splunk_version:enterprise
# Splunk Server:
splunk_server=192.168.1.20
# Splunk HEC Port - Default is 8088:
splunk_hec_port=8088
# Splunk Hec SSL:
splunk_hec_ssl=False
# Splunk HEC Token:
splunk_hec_key=
# Splunk sourcetype:
splunk_sourcetype=tiny_splunker
# Splunk index:
splunk_index=main
# Splunk Source:
splunk_source=
# Splunk host:
splunk_host=jarvis
```

## Splunk Setup

If you are using Splunk Enterprise, you just need the ip or the domain of your splunk server without the "http://"

If you are using Splunk cloud, set `splunk_version=cloud` and for splunk_server this should be your HEC Endpoint which will be something like `https://http-inputs-mycompany.splunkcloud.com/services/collector/event`

## Usage

Just call tohecwitit.py and pass arguments:

```
usage: tohecwittt [-h] [-i IDX] [-s SRC] [-st SRCTYPE] -e EVENT

Python based Splunk HEC logger

required arguments:
  -e EVENT, --event EVENT			Event to be logged in json

optional arguments:
  -h, --help            			show this help message and exit
  -i IDX, --idx IDX     			Splunk Index you want to send the event to
  -s SRC, --src SRC     			Source of Event
  -st SRCTYPE, --srctype SRCTYPE 	Event Sourcetype 
```
Event is expected to be in json. Since the log event is passed to the Splunk HTTP Event Collector as json, the sourcetype can be anything. Splunk will auto-extract the key value pairs.

If none of the optional requirements are passed the script will use the values set in the .env file.

### Example:

`./tohecwitit.py -i main -e '{"log_level":"info","action":"Update","message":"User has been added"}'`

## Compatibility

This script was written and tested using python 3.7.2


