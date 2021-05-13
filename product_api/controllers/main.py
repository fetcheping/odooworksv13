import logging

from addons.http_routing.models.ir_http import slug
from odoo.exceptions import UserError, AccessError
from odoo.http import request, route
from odoo import http, tools, _

_logger = logging.getLogger(__name__)


class ServiceRequest(http.Controller):
    @http.route(['/createslide'], type='http', auth="user", website=True)
    def get_all_channel(self):
        channels = request.env['slide.channel'].search([])

        values = {

            'channels': channels

        }

        return request.render("project_test.request_form", values)

    @http.route(['/deleteslide'], type='http', auth="user", website=True)
    def get_delete_slide(self):
        slides = request.env['slide.slide'].search([])

        values = {

            'slides': slides

        }

        return request.render("project_test.request_form_delete", values)

    @http.route(['/editslide'], type='http', auth="user", website=True)
    def get_all_slide(self):
        slides = request.env['slide.slide'].search([])

        values = {

            'slides': slides

        }

        return request.render("project_test.request_form_edit", values)

    @http.route(['/slides/add_slide'], type='http', auth='user', methods=['POST'], website=True)
    def create_sli(self, *args, **kw):
        print(http.request)
        print(kw)
        create_slide = request.env['slide.slide'].sudo().create(
            {
                'name': kw.get('name'),
                'channel_id': int(kw['channel_id']),
                'slide_type': kw.get('slide_type'),
            })
        print(create_slide)

        return request.render("project_test.thanks_create", {})

    @route(['/delete/channel'], auth='user', csrf=False, methods=['POST'], website=True)
    def delete_channel(self, **kw):
        """if channel_id:
            domain = [('id', '=', channel_id)]
        else:
            domain = []"""
        slide_rec = request.env['slide.slide'].sudo().search([('id', '=', int(kw.get('id')))])
        delete_record = slide_rec.unlink()
        return request.render("project_test.thanks_delete", {})

    @route(['/update/channel/<int:channel_id>'], auth='user', csrf=False, methods=['GET'], website=True)
    def update_channel(self, channel_id=None):
        if channel_id:
            domain = [('id', '=', channel_id)]
        else:
            domain = []
        single_slide = request.env['slide.slide'].sudo().search(domain)
        channels = request.env['slide.channel'].search([])
        values = {

            'slides': single_slide,
            'channels': channels

        }

        return request.render("project_test.request_form_update", values)

    @route(['/updatechannel'], auth='user', csrf=False, methods=['POST'], website=True)
    def update(self, **kw):
        slide_rec = request.env['slide.slide'].sudo().search([('id', '=', int(kw.get('id')))])
        for record in slide_rec:
            record.write(
                {
                    'name': kw.get('name'),
                    'channel_id': int(kw['channel_id']),
                    'slide_type': kw.get('slide_type'),
                }
             )
            print(record)
        return request.render("project_test.thanks_update", {})
