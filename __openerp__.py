# -*- coding: utf-8 -*-
##############################################################################
#
##############################################################################
{
    'name': 'Website Sales commissions',
    'version': '1.0',
    'author': 'Cyrus Waithaka',
    "category": "Sales Management",
    'description': """
This module enables you to offer sales commissions on ecommerce sales.
This means that you can configure commissions in such a way that a sales
agent gets a commission every time their customer makes an order from the
website.
    """,
    'license': 'AGPL-3',
    'price': 10,
    'depends': [
        'sale_commission','website_sale'
    ],
    "data": [
    ],
    "demo": [
    ],
    "installable": True
}
