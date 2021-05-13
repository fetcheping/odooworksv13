from odoo import api, fields, _, models
from odoo.exceptions import ValidationError, RedirectWarning, UserError


class ContactInventoryInherit(models.Model):
    _inherit = 'product.template'

    partner_id = fields.Many2one("res.partner")
    contact = fields.Char("contact", related="partner_id.name")


