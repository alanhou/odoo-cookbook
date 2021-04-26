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
    'category': 'Library',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        "views/library_book.xml",
    ],
    # 'demo': ['demo.xml'],
}
