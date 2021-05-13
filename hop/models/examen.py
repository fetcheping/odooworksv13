from odoo import models, fields, api, _
from datetime import datetime


class LaboExamen(models.Model):
    _name = 'labo.examen'

    # ce sont les champs de la table examen
    name = fields.Char(string="Numero", required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    labo_type_examen_lines = fields.One2many('labo.type.examen.line', 'labo_type_examen_id', 'examen')
    patient_id = fields.Many2one('labo.patient', string='Nom du patient', required=True)
    date_examen = fields.Date(string="Date de l'examen", default=datetime.today())
    prescripteur = fields.Many2one('labo.pres', string='Prescripteur')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    amount_total = fields.Monetary(compute='_amount_montant', string='Montant total', store=True)
    avance = fields.Float(string="Avance")
    rest_to_pay = fields.Float(string="Reste à payer", compute="reste_a_payer", store=True)
    disponible = fields.Selection(string="Résutat disponible", selection=[('oui', 'Oui'), ('non', 'Non')],
                                  default='non')

    # cette fonctionne permet de calculer le montant restant à payer
    @api.depends('amount_total', 'avance')
    def reste_a_payer(self):
        tt = self.amount_total - self.avance
        self.update({'rest_to_pay': tt})

    # cette fonction permet la creation d'un patient , elle hérite la fonction native 'create' d'odoo
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('examen.sequence') or _('New')
            result = super(LaboExamen, self).create(vals)
        return result

    @api.depends('labo_type_examen_lines.price_total')
    def _amount_montant(self):
        for order in self:
            price_tt = 0.0
            for line in order.labo_type_examen_lines:
                price_tt += line.prix
                order.update({
                    'amount_total': price_tt
                })


# cette classe concerne les lignes d'examen du patient lors de l'enregistrement d'un nouveau examen
class LaboTypeExamenLine(models.Model):
    _name = 'labo.type.examen.line'

    # ce sont les champs de la table ligne d'examen
    name = fields.Many2one('labo.type.examen', string='Examen')
    prix = fields.Float(string="Prix")
    labo_type_examen_id = fields.Many2one('labo.examen', string="Type Examen ID")
    price_total = fields.Float(string='Total')
    p = fields.Char(related='labo_type_examen_id.name')

    # cette fonction permet de préremplir le montant de l'examen choisis par l'utilisateur
    @api.onchange('name')
    def set_unit_price(self):
        if self.name:
            self.prix = self.name.prix

    # cette fonction permet de calculer le montant totale des examens choisis
    @api.depends('prix')
    def calculer_montant(self):
        for line in self:
            line.update({
                'price_total': sum(line.prix)
            })
