# -*- coding: utf-8 -*-
import json
import random
import requests

server_url = 'http://192.168.50.143:8069'
db_name = 'odoo-test'
username = 'admin'
password = 'admin'

json_endpoint = '%s/jsonrpc' % server_url
headers = {"Content-Type": "application/json"}


def get_json_payload(service, method, *args):
    return json.dumps({
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": service,
            "method": method,
            "args": args
        },
        "id": random.randint(0, 100000000)
    })


payload = get_json_payload("common", "login", db_name, username, password)
response = requests.post(json_endpoint, data=payload, headers=headers)
user_id = response.json()['result']

if user_id:
    # 对图书 id 进行搜索和读取
    search_domain = ['|', ['name', 'ilike', 'odoo'], ['name', 'ilike', 'sql']]
    payload = get_json_payload("object", "execute_kw",
                               db_name, user_id, password,
                               'library.book', 'search_read', [search_domain, ['name', 'date_release']], {'limit': 5})
    res = requests.post(json_endpoint, data=payload, headers=headers).json()
    print('Books data:', res)
else:
    print("Failed: wrong credentials")
