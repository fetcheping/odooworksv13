from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    rayon = fields.Many2one(string='Rayon', related='product_id.categ_id')
    qte_cmd = fields.Float(string='Qté commandée')
    ug = fields.Float(string="UG")
    price_subtotal = fields.Monetary(compute='_compute_amount', readonly=False)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    amount_total = fields.Monetary(string='Total(avec prélévement)', readonly=False)
    bl_total = fields.Integer(string='Montant du BL', required=True)

    def verify(self):
        for line in self.order_line:
            if line.ug:
                line.product_qty += line.ug

    def button_confirm(self):
        self.verify()
        self.amount_total = self.amount_total + (self.amount_total * 0.02)
        if self.amount_total != self.bl_total:
            raise UserError(_("Le montant total doit correspondre au montant du BL"))
        res = super(PurchaseOrder, self).button_confirm()
        return res
