# -*- coding: utf-8 -*-
{
    'name': "Rental management",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Innovation Sarl",
    'website': "http://www.innovations-groups.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'license': 'AGPL-3',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/fixecharge.xml',
        'views/reservation.xml',
        'views/bedroom.xml',
        'views/reservation_boss.xml',
        'views/reservation_sequence.xml',
        'views/location_management.xml',
        'report/recu.xml',
        'report/report.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
