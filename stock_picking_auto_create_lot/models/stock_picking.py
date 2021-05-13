# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    auto_create_lot = fields.Boolean(string="Auto Create Lot")


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        if self.picking_type_id.auto_create_lot:
            for line in self.move_line_ids.filtered(
                    lambda x: (
                            not x.lot_id
                            and not x.lot_name
                            and x.product_id.tracking != "none"
                            and x.product_id.auto_create_lot
                    )
            ):
                line.lot_id = self.env["stock.production.lot"].create(
                    {"product_id": line.product_id.id, "company_id": line.company_id.id,
                     "life_date": line.life_date, "use_date": line.use_date,
                     "removal_date": line.removal_date, "alert_date": line.alert_date}
                )
        return super().button_validate()


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    life_date = fields.Datetime(string='End of Life Date',
                                help='This is the date on which the goods with this Serial Number may become dangerous and must not be consumed.')
    use_date = fields.Datetime(string='Best before Date',
                               help='This is the date on which the goods with this Serial Number start deteriorating, without being dangerous yet.')
    removal_date = fields.Datetime(string='Removal Date',
                                   help='This is the date on which the goods with this Serial Number should be removed from the stock. This date will be used in FEFO removal strategy.')
    alert_date = fields.Datetime(string='Alert Date')
