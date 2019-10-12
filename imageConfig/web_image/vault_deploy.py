#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - Running api for Vault Container 

import hvac
import sys
from typing import Sequence, Dict
import urllib3
urllib3.disable_warnings()

globals() ["vault_server"]=""
globals() ["root_token"]=""

globals() ["vault_server"]= 'https://vault:8200'
# root token has to be taken from terminal
globals() ["root_token"]="s.sxOXt8RvsWsdrU9ha8K3f0Iw"


# keys = ["mfv4ri9bwMd+tRsVX1Zvu/WALChlxSB1VRRZTpbUYXJJ","/RVUmPb4nV8BifuNZjxSNQ11qCoV7bBNa4U4gi3usUDp","ST6P7z6ielMPuZy59zYAMVAL5LNKgHpj2a5h/zZXzLRD"]
keys = ["b4a434e234172f391bc407d9db6697550fe9facfb93d8ef917ac67b81c19e741"]
def release_keys(client,keyss):
    response = client.sys.submit_unseal_key(keyss[0])
    return 200 if response['sealed'] == False else 300

def unseal_vault(keys,client):
    if client.sys.is_initialized():
        if release_keys(client,keys) == 200:
            print("vault is unsealed")
        else:
            print("vault is not unsealed")
        

def create_mount_point(client):
    try:
        response = client.enable_secret_backend("kv",mount_point="gos")
    except:
        return "Client Authentication Failed!"
        # print()
    if "204" in str(response):
        print("secret created successfully")
    else:
        print("unable to create secret")
    
def configure_mount_point(client):
    response = client.secrets.kv.v2.configure(max_versions=20,mount_point='gos')
    if "204" in str(response):
        print("mount point configured successfully")
    else:
        print("unable to configure mount point")

def enable_userpass(client):
    response = client.sys.enable_auth_method('userpass')
    print(response,"**********enable response*************")
    if "204" in str(response) :
        print("userpass enabled successfully")
    else:
        print("unable to enable user pass")
    
def create_user(username,password):
    client = hvac.Client(url=globals() ["vault_server"],token=globals() ["root_token"],cert=("cert.pem","key.pem"),verify=False)
    try:
        response = client.create_userpass(username=str(username),password=str(password),mount_point="userpass",policies=["sudo","read","update","create"])
        if "204" in str(response) :
            print("User and password created successfully")
            return 200
        else:
            print("Unable to create user")
            return 400

    except Exception as e:
        print(e,"************")
        return "Client Authentication Failed!"
    
def authenticate_user_pass(username,password):
    client = hvac.Client(url=globals() ["vault_server"],token=globals() ["root_token"],cert=("cert.pem","key.pem"),verify=False)
    response = client.auth_userpass(username=str(username),password=str(password),mount_point="userpass",use_token=True)
    print(response)
    if response:
        print("User is validated successfully")
        client_token = response["auth"]["client_token"]
        return client_token
    else:
        print("Unable to validate user")
        return 400

def on_page_load():
    client = hvac.Client(url=globals() ["vault_server"],token=globals() ["root_token"],cert=("cert.pem","key.pem"),verify=False)

    unseal_vault(keys,client)
    create_mount_point(client)
    configure_mount_point(client)
    enable_userpass(client)






