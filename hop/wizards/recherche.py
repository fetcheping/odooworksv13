from odoo import models, fields


class LaboExamen(models.Model):
    _name = 'recherche'

    date1 = fields.Date(string="date de fin")
    date2 = fields.Date(string="date de fin")
    type_examen = fields.Many2one('labo.type.examen', string="Examen")

    # prescripteur = fields.Many2one('labo.pres', string="prescripteur")
    # patient = fields.Many2one('labo.patient', string="patient")
    # date1 = fields.Date(string="date de debut")

    def imprimer_rapport(self):
        data = {
            'model': 'recherche',
            'form': self.read()[0]
        }
        return self.env.ref('hop.report_recherche').report_action(self, data=data)
