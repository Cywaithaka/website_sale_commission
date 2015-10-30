# -*- coding: utf-8 -*-
##############################################################################
#
#
##############################################################################
from openerp import SUPERUSER_ID,models,api, fields
class SaleOrder(models.Model):
    _inherit = "sale.order"
    def _website_product_id_change(self, cr, uid, ids, order_id, product_id, qty=0, line_id=None, context=None):
        res = super(SaleOrder,self)._website_product_id_change(cr, uid, ids, order_id, product_id, qty=qty, line_id=line_id, context=None)
        if qty==1:#if 'agents' not in res: #Only do this for the first item
            line = self.pool.get('sale.order.line').browse(cr, SUPERUSER_ID, line_id, context=context)
            res.update({'agents': line.set_agents(cr, uid, line.order_partner_id.id,context=context)})
        return res

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def set_agents(self, cr, uid, partner_id, context=None):
        agents = []
        if partner_id:
            partner = self.pool.get('res.partner').browse(cr, uid, partner_id, context=context)
            for agent in partner.agents:
                agents.append({'agent': agent.id,
                               'commission': agent.commission.id})
        return [(0, 0, x) for x in agents]