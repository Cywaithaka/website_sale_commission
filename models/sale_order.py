# -*- coding: utf-8 -*-
##############################################################################
#
#   
##############################################################################

#from openerp import models, fields, api

from openerp.osv import osv, fields
class SaleOrder(osv.Model):
    _inherit = "sale.order"
    def _website_product_id_change(self, cr, uid, ids, order_id, product_id, qty=0, line_id=None, context=None):
        res = super(SaleOrder,self)._website_product_id_change(cr, uid, ids, order_id, product_id, qty=qty, line_id=line_id, context=None)
        line = self.pool.get('sale.order.line').browse(cr, SUPERUSER_ID, line_id, context=context)
        res['commissions'] = line._default_commissions()
        return res
