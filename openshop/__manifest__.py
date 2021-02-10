# -*- coding: utf-8 -*-
{
    'name': "Openshop",

    'summary': """
        openshop module test
    """,

    'description': """
        Openshop odoo module test 
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'application': True,
    'intstallable': True,
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Openshop',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_templates.xml',
        'views/product_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
