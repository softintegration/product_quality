# -*- coding: utf-8 -*- 


{
    'name': 'Product quality',
    'author': 'Soft-integration',
    'application': False,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Product',
    'demo': [],
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/product_quality_views.xml'
    ],
    'license': 'LGPL-3',
}
