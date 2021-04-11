#!/usr/bin/env python

import json
import urllib2

METADATA_URL = "http://169.254.169.254/latest/meta-data/"

_data = {}

# Function returns the content os a given URL
def _get_metadata_from_url(url):
    contents = urllib2.urlopen(url).read()
    return contents

# Function loops through the text content and convert to a python dict
def _format(url):
    contents = _get_metadata_from_url(url)

    for key in contents.split('\n'):
        sub_url = '{0}{1}'.format(url, key)
        if key.endswith('/'):
            sub_key = key.split('/')[-2]
            _format(sub_url)
        else:
            contents = _get_metadata_from_url(sub_url)
            try:
                _data[key] = json.loads(contents)
            except ValueError:
                _data[key] = contents

def _format_json(d):
    print(json.dumps(d, sort_keys=True, indent=4))

_format(METADATA_URL)
_format_json(_data)


# For example if you need a value of specific key, this can easily be ported as user input or a cli utility
print("The value of the choosen key info/AccountId is " + _data["info"].get("AccountId"))
