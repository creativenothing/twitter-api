
import requests
import os
import json
import time

bearer_token = os.environ.get('TOKEN')
headers = {"Authorization": "Bearer {}".format(bearer_token)}

api_base = "https://api.twitter.com/2"
username = os.environ.get("USERNAME")

get_userid_endpoint = api_base + "/users/by/username/{}".format(username)

def connect_to_endpoint(url, headers, params = {}, next_token = None):
    params['next_token'] = next_token
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

json_response = connect_to_endpoint(get_userid_endpoint, headers)

now = time.strftime("%Y-%m-%d")

with open('./userids/{}-{}.json'.format(username, now), 'w') as f:
    json.dump(json_response, f)



