from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOutStockInvoicing(models.Model):
    _inherit = 'account.move'

    def verify_stock(self):
        for line in self.invoice_line_ids:
            quantity_on_hand = line.product_id.qty_available
            if quantity_on_hand <= 0 and line.quantity > line.product_id.qty_available:
                raise UserError(_("You cannot issue this invoice because of "
                                  "the following reason: \n you charge " +
                                  str(line.quantity) + " " +
                                  line.product_id.uom_name
                                  + " of " + line.product_id.name +
                                  " but you only have " + str(quantity_on_hand) + " " +
                                  line.product_id.uom_name + " available on hand.\n\n"
                                  "Please update its stock or cancel it from the current invoice"))

    def action_post(self):
        self.verify_stock()
        res = super(SaleOutStockInvoicing, self).action_post()
        return res
