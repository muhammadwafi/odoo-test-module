# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class openshop(models.Model):
#     _name = 'openshop.openshop'
#     _description = 'openshop.openshop'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Products(models.Model):
    _name = 'openshop.products'
    _description = 'Products'
    _order = 'id DESC'
    
    # Selection fields
    PRODUCT_CATS = [
        ('t-shirt', 'T-Shirt'),
        ('tank-top', 'Tank Top'),
        ('polo-shirt', 'Polo Shirt'),
        ('long-sleeves', 'Long Sleeves'),
    ]
    PRODUCT_SIZE = [
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
    ]

    name        = fields.Char(string="Name", required=True, size=140)
    image       = fields.Image(string="Image", attachment=True, max_width=1920, max_height=1920)
    description = fields.Text(string="Description", required=True)
    category    = fields.Selection(PRODUCT_CATS, string="Categories", required=True)
    size        = fields.Selection(PRODUCT_SIZE, string="Size", required=True)
    price       = fields.Float(string="Price", required=True)
    is_active   = fields.Boolean(string="Active", default=True)
    
    
    
    def _truncate_text(self, str, size):
        if len(str) <= size:
            return str
        return str[0:size]
    
    @api.onchange('name')
    def _onchange_name(self):
        if self.name > 140:
            raise ValidationError(_("Products name cannot be longer than 140 characters: %s" % self.name))
    
    @api.constrains('name')
    def _constrain_name(self):
        if len(self.name) > 140:
            # return self._truncate_text(self.name, 140)
            raise ValidationError(_('Products name cannot be longer than 140 characters'))