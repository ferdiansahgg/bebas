# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mrp_lot(models.Model):
    _name = 'mrp.production'
    _inherit = 'mrp.production'
    
    @api.model
    def create(self, values):
        res = super(mrp_lot,self).create(values)
        lot_data = {
            'name': res.name,
            'product_id': res.product_id.id
        }
        self.env['stock.production.lot'].create(lot_data)
        return res