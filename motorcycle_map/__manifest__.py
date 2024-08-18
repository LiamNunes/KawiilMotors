{
    'name': "motorcycle_map",
    'summary': "Module that shows where registered motorcycles are",
    'author': "Liam Nunes",
    'website': "https://github.com/LiamNunes/KawiilMotors/compare/main...17.0-motorcycle-registry",
    'category': 'Kawiil/Custom Modules',
    'version': '0.0.1',
    'license':'OPL-1',
    'depends': ['base','motorcycle_registry'],
    'data': [
        'security/ir.model.access.csv',
        'views/motorcycle_map_views.xml',
    ],
    'auto_install': True,
    'application': False,
}