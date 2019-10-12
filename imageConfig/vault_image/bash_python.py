#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - Test vault application 
import os
import subprocess
import requests
import logging
import json


logger = logging.basicConfig(filename="log.txt",level=logging.DEBUG)
def get_required_paths():
    # with open("config/config.json", "r") as f:
    #     config = json.load(f)
    globals()['base_url'] = "https://127.0.0.1:8200/v1/"
    # globals()['cert_path'] = config["certPath"]
    # globals()['base_path'] = config["basePath"]
    globals()['max_ttl'] = "30s"


def request_post_call(url, data, headers):
    return requests.post(url, data=json.dumps(data), headers=headers)


def request_put_call(url, data, headers):
    return requests.post(url, data=json.dumps(data), headers=headers)
