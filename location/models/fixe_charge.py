from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class FixeChargeDetails(models.Model):
    _name = 'fixe.charge.details'

    name = fields.Char(string='Nom', required=True)
    prix = fields.Float(string='Prix', required=True)

