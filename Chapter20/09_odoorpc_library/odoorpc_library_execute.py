# -*- coding: utf-8 -*-
import odoorpc

db_name = 'odoo-test'
user_name = 'admin'
password = 'admin'

# 准备对服务端的连接
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login(db_name, user_name, password) # 登录

books_info = odoo.execute('library.book', 'search_read',
                          [['name', 'ilike', 'odoo']], ['name', 'date_release'])
print(books_info)