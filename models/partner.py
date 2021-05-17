# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields
from openerp.osv import osv
from openerp.tools.translate import _


class partner_canal(models.Model):
    _name = 'res.partner.canal'
    _description = "Canal"

    name = fields.Char('Canal', required=True, select=True)
    description = fields.Text('Description')

    partner_ids = fields.One2many(
        'res.partner',
        'canal_id',
        'Partners')


class res_partner(models.Model):

    _inherit = 'res.partner'

    canal_id = fields.Many2one(
        'res.partner.canal',
        string='Canal',
        # track_visibility='onchange',
        select=True
    )