# -*- coding: utf-8 -*-
{
    'name': "todo_user",

    'summary': 'Extend the To-Do app to multiuser.',

    'description': """
        Long description of module's purpose
    """,

    'author': "ROC systems c.a.",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['todoroc_app', 'mail'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/todo_user_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
