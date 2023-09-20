# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductQuality(models.Model):
    _name = 'product.quality'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code',required=True)
    description = fields.Text('Description')