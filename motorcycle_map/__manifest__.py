# -*- coding: utf-8 -*-
{
    'name': "motorcycle_map",
    'summary': "Module that shows where registered motorcycles are",
    'author': "Liam Nunes",
    'website': "https://github.com/LiamNunes/KawiilMotors/compare/main...17.0-motorcycle-registry",
    'category': 'Kawiil/Custom Modules',
    'version': '0.0.1',
    'license':'OPL-1',
    'depends': ['motorcycle_registry','web_map'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

