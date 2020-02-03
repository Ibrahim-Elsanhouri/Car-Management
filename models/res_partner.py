# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    #     _description = 'my_first_module.my_first_module'

    mynote1 = fields.Char(string='Custome MyNote 1')
    mynote2 = fields.Char(string='Custome MyNote 2')
    mynote3 = fields.Char(string='Custome MyNote 3')

