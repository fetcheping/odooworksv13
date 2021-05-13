
from odoo import models, fields, api, _


class PontBasculeDetails(models.Model):
    _name = 'pontbascule.details'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Nom du conducteur', required=True)
    matricule = fields.Char(string="Matricule de l'engin", required=True)
    poidin = fields.Float(string="Poid d'entrée")
    poidout = fields.Float(string="Poid de sortie")
    uom_id = fields.Many2one('uom.uom', string='unité de mesure', required=True)
    note_field = fields.Html(string='Comment')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('pontbascule.details') or 'New'
        return super(PontBasculeDetails, self).create(vals)
