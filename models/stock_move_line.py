# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    product_quality_id = fields.Many2one('product.quality', string='Quality',related='product_id.product_quality_id',store=True)


