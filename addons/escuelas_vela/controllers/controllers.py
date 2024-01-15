# -*- coding: utf-8 -*-
# from odoo import http


# class EscuelasVela(http.Controller):
#     @http.route('/escuelas_vela/escuelas_vela', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escuelas_vela/escuelas_vela/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escuelas_vela.listing', {
#             'root': '/escuelas_vela/escuelas_vela',
#             'objects': http.request.env['escuelas_vela.escuelas_vela'].search([]),
#         })

#     @http.route('/escuelas_vela/escuelas_vela/objects/<model("escuelas_vela.escuelas_vela"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escuelas_vela.object', {
#             'object': obj
#         })
