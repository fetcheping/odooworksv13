from odoo import fields, models, api, _


class LaboPres(models.Model):
    _name = 'labo.pres'

    # ce sont les champs de la table prescripteur
    name = fields.Char(string='Nom et Prenom', required=True)
    numero = fields.Char(string="Numéro", required=True, copy=False, readonly=True, index=True,
                         default=lambda self: _('New'))
    tel = fields.Integer(string='Numero de telephone')
    hopital = fields.Char(string='Hopital')
    pres = fields.Integer(compute='count_patient')

    # cette fonction permet la creation d'un patient , elle hérite la fonction native 'create' d'odoo
    @api.model
    def create(self, vals):
        if vals.get('numero', _('New')) == _('New'):
            vals['numero'] = self.env['ir.sequence'].next_by_code('prescripteur.sequence') or _('New')
            result = super(LaboPres, self).create(vals)
        return result

    # cette fonction permet de compter le nombre de patient d'un prescripteur
    def count_patient(self):
        count = self.env['labo.type.examen.line'].search_count([('labo_type_examen_id.prescripteur', '=', self.id)])
        self.pres = count

    def open(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'examens',
            'view_mode': 'tree',
            'res_model': 'labo.type.examen.line',
            'domain': [('labo_type_examen_id.prescripteur', '=', self.id)],
            'context': "{'create':False}",

        }
