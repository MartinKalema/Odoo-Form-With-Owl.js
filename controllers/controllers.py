# -*- coding: utf-8 -*-
from odoo import http


class NiraDataEntry(http.Controller):
    @http.route('/nira/apply', auth='user')
    def index(self, **kw):
        return http.request.render('nira_data_entry.nira_data_entry_website_form_template',
                                   {'user_id': http.request.env.user.id})

    @http.route('/nira/owl', auth='user')
    def index_owl(self, **kw):
        return http.request.render('nira_data_entry.owl_form_template', {})


# class NiraDataEntry(http.Controller):
#     @http.route('/nira_data_entry/nira_data_entry', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nira_data_entry/nira_data_entry/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nira_data_entry.listing', {
#             'root': '/nira_data_entry/nira_data_entry',
#             'objects': http.request.env['nira_data_entry.nira_data_entry'].search([]),
#         })

#     @http.route('/nira_data_entry/nira_data_entry/objects/<model("nira_data_entry.nira_data_entry"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nira_data_entry.object', {
#             'object': obj
#         })

