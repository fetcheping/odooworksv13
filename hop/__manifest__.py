# -*- coding: utf-8 -*-
{
    'name': "hopital",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/type_examen.xml',
        'views/prescripteur.xml',
        'views/report_templates.xml',
        'wizards/reherche.xml',
        'views/patient.xml',
        'views/examen.xml',
        'report/report.xml',
        'report/fiche_examen.xml',
        'report/test.xml',
        'report/bilan.xml',
        'report/bilan_financier.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/sequence_pres.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
