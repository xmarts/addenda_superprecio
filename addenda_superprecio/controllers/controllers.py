# -*- coding: utf-8 -*-
from odoo import http

# class AddendaSuperprecio(http.Controller):
#     @http.route('/addenda_superprecio/addenda_superprecio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addenda_superprecio/addenda_superprecio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addenda_superprecio.listing', {
#             'root': '/addenda_superprecio/addenda_superprecio',
#             'objects': http.request.env['addenda_superprecio.addenda_superprecio'].search([]),
#         })

#     @http.route('/addenda_superprecio/addenda_superprecio/objects/<model("addenda_superprecio.addenda_superprecio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addenda_superprecio.object', {
#             'object': obj
#         })