import logging

from addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError, AccessError
from odoo.http import request, route
from odoo import http, tools, _

_logger = logging.getLogger(__name__)


class getProduct(http.Controller):
    @http.route('/warehouse', type='json', auth='user')
    def getwarehouse(self):
        warehouse_rec = request.env['stock.warehouse'].search([])
        warehouses = []
        for rec in warehouse_rec:
            vals = {
                'Name': rec.name,
            }
            warehouses.append(vals)
        print('Product List --->', warehouses)
        print('Total products is', len(warehouses))
        data = {'status': 200, 'response': warehouses[0], 'message': 'Done All warehouses Returned'}
        return data

    @http.route('/products', type='json', auth='user', csrf=True)
    def getallproduct(self):
        domain = [
            ('available_in_pos', '=', True)
        ]
        products_rec = request.env['product.template'].search(domain)
        products = []
        for rec in products_rec:
            vals = {
                'Reference Number': rec.default_code,
                'Product Name': rec.name,
                'quantity': rec.qty_available,
                'warehouse location': rec.warehouse_id.name
            }
            products.append(vals)
        print('Product List --->', products)
        print('Total products is', len(products))
        data = {'status': 200, 'response': products, 'message': 'Done All Products Returned'}
        return data
