from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ReservationDetails(models.Model):
    _name = "reservation.details"
    _inherit = 'room.details'

    _sql_constraints = [
        (
            "ref_uniq",
            "unique(ref)",
            "La Référence du contrat doit etre unique!",
        )
    ]

    name = fields.Char(string='ID', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    chambre_id = fields.Many2one('room.details', string="Chambre")
    #chambre_id = fields.Many2one('room.details')
    lieu = fields.Char(related='chambre_id.emplacement', store=True)
    client = fields.Many2one('res.partner', string="Client")
    date_in = fields.Date(string="Date d'entrée")
    date_out = fields.Date(string="Date de sortie prévue")
    period = fields.Char(string='Periode', compute='compute_period')
    note_field = fields.Html(string='Comment')
    # price_room = fields.Many2one('room.details')
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.user.company_id.id, index=1)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    price = fields.Monetary(string="Montant percue")
    price_net = fields.Monetary(string="Montant A Payé", compute='net_to_pay')
    price_res = fields.Monetary(string="Montant Restant", compute='price_remind')
    state_room = fields.Selection(string="Etat", related="chambre_id.status", readonly=False, store=True, required=False)
    price_room = fields.Integer(related="chambre_id.price", readonly=False, store=True, required=False)
    reservation_cf_line = fields.One2many('reservation.cf.lines', 'reservation_cf_lines_id',
                                          'cf')
    caution = fields.Monetary(string="Caution")
    amount_total_cf = fields.Monetary(compute='_amount_montant', string='Montant CF', store=True)
    ref = fields.Char(string='Ref. Contrat')

    @api.depends('reservation_cf_line.amount_total')
    def _amount_montant(self):
        for order in self:
            price_tt = 0.0
            for line in order.reservation_cf_line:
                price_tt += line.amount
                order.update({
                    'amount_total_cf': price_tt
                })

    def price_remind(self):
        for record in self:
            record['price_res'] = record['price_net'] - record['price']

    def net_to_pay(self):
        amount_cf = self._amount_montant
        for record in self:
            dtein = fields.Datetime.from_string(record.date_in)
            dteout = fields.Datetime.from_string(record.date_out)
            delta = relativedelta(dteout, dtein)
            record['price_net'] = record['price_room'] * (delta.years * 12 + delta.months) + record['amount_total_cf'] + record['caution']

    def compute_period(self):
        for data in self:
            if data.date_in:
                dtein = fields.Datetime.from_string(data.date_in)
                dteout = fields.Datetime.from_string(data.date_out)
                delta = relativedelta(dteout, dtein)
            data.period = str(delta.years) + ' Ans ' + str(delta.months) + ' Mois ' + str(delta.days) + ' Jours'

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('reservation.details') or 'New'
            return super(ReservationDetails, self).create(vals)


class ReservationChargeFixe(models.Model):
    _name = 'reservation.cf.lines'
    name = fields.Many2one('fixe.charge.details', string="Charges Fixes")
    reservation_cf_lines_id = fields.Many2one('reservation.details', string="Type Product ID")
    amount = fields.Float(string='montant')
    amount_total = fields.Float(string='Total CF')

    @api.depends('amount')
    def calculer_montant(self):
        for line in self:
            line.update({
                'amount_total': sum(line.amount)
            })
