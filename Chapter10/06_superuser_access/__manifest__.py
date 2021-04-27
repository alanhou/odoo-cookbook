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
    'depends': ['base_setup'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/security_rules.xml',
        'views/res_config_settings.xml',
        "views/library_book.xml",
    ],
    # 'demo': ['demo.xml'],
}
