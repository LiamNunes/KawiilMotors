{
    'name': 'Motorcycle Registry',
    'website':'https://github.com/LiamNunes/KawiilMotors',
    'version': '0.0.1',
    'category': 'Kawiil/Custom Modules',
    'summary': 'Manage Registration of Motorcyles',
    'description': """
        Motorcycle Registry
        ===================
        This Module is used to keep track of the Motorcycle Registration and Ownership 
        of each motorcyle of the brand
    """,
    'depends': ['base'],
    'data': [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'security/registry_security.xml',
        'views/registry_menuitems.xml',
        'views/registry_views.xml',
    ],
    'demo':[
        'demo/motorcycle_registry_demo.xml',
    ],
    'application': True,
    'license':"LGPL-3"
}