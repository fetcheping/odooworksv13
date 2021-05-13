from odoo import models, fields


class LaboExamen(models.Model):
    _inherit = 'labo.examen'

    date_from = fields.Date(string="De")
    date_to = fields.Date(string="à")
