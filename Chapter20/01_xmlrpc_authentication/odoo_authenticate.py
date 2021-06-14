# -*- coding: utf-8 -*-
from xmlrpc import client


server_url = 'http://localhost:8069'
db_name = 'odoo-test'
username = 'admin'
password = 'admin'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

if user_id:
    print('Success: User id is', user_id)
else:
    print('Failed: wrong credentials')