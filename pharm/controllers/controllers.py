# -*- coding: utf-8 -*-
# from odoo import http


# class Pharm(http.Controller):
#     @http.route('/pharm/pharm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pharm/pharm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pharm.listing', {
#             'root': '/pharm/pharm',
#             'objects': http.request.env['pharm.pharm'].search([]),
#         })

#     @http.route('/pharm/pharm/objects/<model("pharm.pharm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pharm.object', {
#             'object': obj
#         })
