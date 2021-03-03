{
    'name': "My library",
    'summary': "轻松管理图书",
    'description': """
Manage Library
==============
Description related to library.
     """,
    'author': "Alan Hou",
    'website': "https://alanhou.org",
    'category': 'Uncategorized',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book.xml',
        'views/library_book_categ.xml',
        'views/library_book_rent.xml',
        'wizard/library_book_rent_wizard.xml',
        'wizard/library_book_return_wizard.xml',
    ],
    # 'demo': ['demo.xml'],
}
