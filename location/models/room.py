from odoo import models, fields, api, _


class RoomDetails(models.Model):
    _name = 'room.details'

    name = fields.Char(string='Nom', required=True)
    capacity = fields.Integer(string="Capacité")
    price = fields.Integer(string="Prix")
    emplacement = fields.Char(string="Lieu")
    status = fields.Selection([("available", "Disponible"), ("occupied", "Occupée")], "Status", default="available")
    note_field = fields.Html(string='Comment')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('room.details') or 'New'
        return super(RoomDetails, self).create(vals)

