from odoo import models, fields, api, _
from datetime import datetime, timedelta


class TransactionDetails(models.Model):
    _name = 'transaction.details'

    name = fields.Char(string='ID', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    transaction_number = fields.Char(string="Transaction Number", required=True)
    type = fields.Selection([
        ("payment", "Payment"),
        ("refund", "Refund"),
        ("transfert", "Transfert"),
    ],
        "Type",
        default="payment")
    date = fields.Datetime(string='Date', default=lambda self: fields.datetime.now() + timedelta(days=0), required=True)
    currency_id = fields.Many2one('res.currency', 'Currency',
                                  default=lambda self: self.env.user.company_id.currency_id.id, required=True)
    amount = fields.Float(string="Amount", required=True)
    # charge = fields.Integer(string="Charge")
    net_amount = fields.Monetary(string="Net Amount", compute='net_to_pay')
    sender = fields.Char(string="Sender")
    phonesender = fields.Char(string="Phone Sender")
    receiver = fields.Char(string="Receiver")
    phonereceiver = fields.Char(string="Phone Receiver")
    bank = fields.Many2one("account.journal", string="Bank")
    status = fields.Selection([
        ("success", "success"),
        ("inprogress", "Inprogress"),
        ("failed", "Failed")
    ],
        "Status",
        default="inprogress")

    def net_to_pay(self):
        for record in self:
            record['net_amount'] = record['amount'] - (0.03 * record['amount'])

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('transaction.details') or 'New'
            return super(TransactionDetails, self).create(vals)
