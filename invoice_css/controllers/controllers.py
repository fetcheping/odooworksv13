# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleVide(http.Controller):
#     @http.route('/module_vide/module_vide/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_vide/module_vide/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_vide.listing', {
#             'root': '/module_vide/module_vide',
#             'objects': http.request.env['module_vide.module_vide'].search([]),
#         })

#     @http.route('/module_vide/module_vide/objects/<model("module_vide.module_vide"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_vide.object', {
#             'object': obj
#         })
