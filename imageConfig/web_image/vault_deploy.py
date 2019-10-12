import hvac
import sys
from typing import Sequence, Dict
import urllib3
urllib3.disable_warnings()

globals() ["vault_server"]=""
globals() ["root_token"]=""
# vault_server = 'http://localhost:8200'

globals() ["vault_server"]= 'https://vault:8200'
# root token has to be taken from terminal
globals() ["root_token"]="s.sxOXt8RvsWsdrU9ha8K3f0Iw"
# # root token has to be taken from terminal
# root_token="s.Fo8fQhZBBs1ztjnLtDk7q3G3"
# client = hvac.Client(url=vault_server,token=root_token) # root token has to be taken from terminal
# # root token has to be taken from terminal

# cert_path=""
# key_path=""
# cert_path = "./cert.pem"
# key_path = "./key.pem"
# client.sys.is_initialized()
shares = 1
threshold = 1

# vault_token = "s.oTV6FQI3oZRfxlHqiictAPJi"

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
        # client.
# globals() username = ""
# globals() password = ""

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

# def get_username_password(username,password):
#     globals() username = username
#     globals() password = password
    
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
    # vault_server = 'http://localhost:8200'
    # # root token has to be taken from terminal
    # root_token="s.Fo8fQhZBBs1ztjnLtDk7q3G3"
    # root token has to be taken from terminal

    client = hvac.Client(url=globals() ["vault_server"],token=globals() ["root_token"],cert=("cert.pem","key.pem"),verify=False)

    unseal_vault(keys,client)
    create_mount_point(client)
    configure_mount_point(client)
    enable_userpass(client)

# on_page_load()

# print(sys.argv[1:2])
# username = sys.argv[1]
# password = sys.argv[2]
# # print(user/)
# print(username,password)
# create_user(username,password)
# client_token = authenticate_user_pass(username,password)
# print(client_token)



# get_username_password(vault_server,client,vault_token)

# def check_user_login(client,username):
#     # vault = hvac.Client(url=vault_server, token=vault_token)
#     response = client.read("secret/data/"+username)
#     token = response["resquest_id"]
#     return token

# def store_user_password(client,username,password):
#     reponse = client.write(path="secret/data/imaya/",data=dict(foo1="bar1"),lease="30s")

    # print(vault)
    # result = {
    #     'username': vault.read('secret/imaya')['data']['value'],
    #     # 'password': vault.read('secret/something')['data']['value'],
    # }
    # return result



# def config_secrets(client):
#     response = client.read("secret/imaya")
#     result = {
#         'username': vault.read('kv/CSR_USERNAME')['data']['value'],
#         'password': vault.read('kv/CSR_PASSWORD')['data']['value'],
#     }
    # client.kv.default_kv_version = 1
    # response = client.read('kv/imaya')['data']["value"]
    # print(response)
    # reponse = client.secrets.kv.v2.configure(mount_point='kv')
    # print(reponse)
    # client.secrets.kv.v2.configure()

# def register_user(client):
    
# def get_secrets():
# config_secrets(client)  

    

# print(root_token)
# print(keys)
# print(val)






# import requests
# import netmiko
# import hvac
# import decouple
# from netmiko import ConnectHandler
# from concurrent.futures import ThreadPoolExecutor
# from functools import partial

# from typing import Sequence, Dict

# HOSTS = [
#     '10.48.18.26',
#     '10.48.18.30'
# ]

# PARAMS = {
#     'device_type': 'cisco_ios'
# }

# COMMANDS = [
#     'show version',
#     'show ip int brief',
#     'show plat soft status control-processor brief'
# ]

# VAULT_SERVER = 'http://localhost:8200'

# # device_conn = ConnectHandler(**device_params)
# #
# # parsed_values = dict()
# # parsed_values.update(parse_show_version(device_conn.send_command('show version')))
# # parsed_values.update(
# #     parse_show_ma c_address_table(device_conn.send_command('show mac address-table')))
# #
# # result = '{hostname} MAC address table:\n{mac_address_table}'.format(**parsed_values)
# # device_conn.disconnect()
# # return result

# def form_device_params(host: str, params: Dict[str, str]) -> Dict[str, str]:
#     return {'host': host, **params, **PARAMS}


# def get_username_password(vault_server, vault_token: str) -> Dict[str, str]:
#     vault = hvac.Client(url=vault_server, token=vault_token)
#     result = {
#         'username': vault.read('kv/CSR_USERNAME')['data']['value'],
#         'password': vault.read('kv/CSR_PASSWORD')['data']['value'],
#     }
#     return result


# def get_outputs(device_info: Dict[str, str], commands: Sequence[str]) -> Dict[str, str]:
#     result = {}
#     with ConnectHandler(**device_info) as device_conn:
#         for command in commands:
#             result[command] = device_conn.send_command(command)
#     return result


# def main():
#     params = get_username_password(VAULT_SERVER, decouple.config('VAULT_TOKEN'))
#     worker = partial(get_outputs, commands=COMMANDS)
#     devices_params = (form_device_params(host, params) for host in HOSTS)
#     with ThreadPoolExecutor(2) as pool:
#         results = pool.map(worker, devices_params)

#     for host, result in zip(HOSTS, results):
#         print('===== Device: {host} =====')
#         for command, output in result.items():
#             print('=== output from {command!r} ===')
#             print(output, end='\n=========\n')



# if __name__ == '__main__':
#     main()