# -*- coding: utf-8 -*-
# from odoo import http


# class LoiNguyen(http.Controller):
#     @http.route('/loi_nguyen/loi_nguyen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loi_nguyen/loi_nguyen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('loi_nguyen.listing', {
#             'root': '/loi_nguyen/loi_nguyen',
#             'objects': http.request.env['loi_nguyen.loi_nguyen'].search([]),
#         })

#     @http.route('/loi_nguyen/loi_nguyen/objects/<model("loi_nguyen.loi_nguyen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loi_nguyen.object', {
#             'object': obj
#         })
