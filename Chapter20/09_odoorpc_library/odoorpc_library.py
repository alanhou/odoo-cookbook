# -*- coding: utf-8 -*-
import odoorpc

db_name = 'odoo-test'
user_name = 'admin'
password = 'admin'

# 准备对服务端的连接
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login(db_name, user_name, password)

# 用户信息
user = odoo.env.user
print(user.name)  # 连接的用户
print(user.company_id.name)  # 用户的公司名
print(user.email)  # 用户的email

BookModel = odoo.env['library.book']
search_domain = ['|', ['name', 'ilike', 'odoo'], ['name', 'ilike', 'sql']]
books_ids = BookModel.search(search_domain, limit=5)
for book in BookModel.browse(books_ids):
    print(book.name, book.date_release)

# 创建图书并更新状态
book_id = BookModel.create({'name': 'Test book', 'state': 'draft'})
book = BookModel.browse(book_id)
print('Book state before make_available:', book.state)
book.make_available()
book = BookModel.browse(book_id)
print("Book state after make_available:", book.state)