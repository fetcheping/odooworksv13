from odoo import fields, models


class LaboTypeExamen(models.Model):
    _name = 'labo.type.examen'

    name = fields.Char(string='Nom', required=True)
    prix = fields.Float(string='Prix', required=True)
