# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    product_quality_id = fields.Many2one('product.quality', string='Quality',compute='_compute_product_quality_id',store=True)

    @api.depends('product_id')
    def _compute_product_quality_id(self):
        for each in self:
            each.product_quality_id = each.product_id.product_quality_id and each.product_id.product_quality_id.id or False

