# -*- coding: utf-8 -*-
{
    'name': "OBHosptial Management",

    'sequence': -100,

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
        Long description of module's purpose
    """,

    'author': "Omar Elbayoumi",
    'website': "#",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menus.xml',
        'views/patient_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'oba_hospital/static/src/css/**',
            'oba_hospital/static/src/js/**',
        ],
        'web.assets_backend': [
            'oba_hospital/static/src/css/**',
            'oba_hospital/static/src/js/**',
        ],
    },
}

