#!/usr/bin/env python
# coding: utf-8

import requests
import os
import json
import time

bearer_token = os.environ.get('TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}

api_base = "https://api.twitter.com/2"
userid = os.environ.get(USERID)

get_usertweet_endpoint = api_base + "/users/{}/tweets".format(userid)

query_params = {
        'max_results': 100,
        'next_token': {},
        }

def connect_to_endpoint(url, headers, params = {}, next_token = None):
    params['next_token'] = next_token
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    # TODO: handle pagination
    return response.json()

json_response = connect_to_endpoint(url=get_usertweet_endpoint, headers=headers, params=query_params )

print(json.dumps(json_response))

# TODO: create more descriptive name and account for pagination
with open('data.json', 'w') as f:
    json.dump(json_response, f)



