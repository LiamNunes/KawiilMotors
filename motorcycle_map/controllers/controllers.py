# -*- coding: utf-8 -*-
# from odoo import http


# class MotorcycleMap(http.Controller):
#     @http.route('/motorcycle_map/motorcycle_map', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/motorcycle_map/motorcycle_map/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('motorcycle_map.listing', {
#             'root': '/motorcycle_map/motorcycle_map',
#             'objects': http.request.env['motorcycle_map.motorcycle_map'].search([]),
#         })

#     @http.route('/motorcycle_map/motorcycle_map/objects/<model("motorcycle_map.motorcycle_map"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('motorcycle_map.object', {
#             'object': obj
#         })

