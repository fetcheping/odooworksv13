from odoo import fields, api, models, _


class LaboPatient(models.Model):
    _name = 'labo.patient'

    # ce sont les champs de la table patient
    name = fields.Char(string='Nom et Prenom', required=True)
    tel = fields.Integer(string='Numero de telephone')
    numero = fields.Char(string="Numero", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: _('New'))

    # cette fonction permet la creation d'un patient , elle hérite la fonction native 'create' d'odoo
    @api.model
    def create(self, vals):
        if vals.get('numero', _('New')) == _('New'):
            vals['numero'] = self.env['ir.sequence'].next_by_code('patient.sequence') or _('New')
            result = super(LaboPatient, self).create(vals)
        return result
