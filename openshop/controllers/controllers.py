# -*- coding: utf-8 -*-
from odoo import http


class Openshop(http.Controller):
    @http.route('/openshop/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/openshop/products/', auth='public')
    def list(self, **kw):
        return http.request.render('openshop.list', {
            'root': '/openshop/',
            'objects': http.request.env['openshop.products'].search([]),
        })

    @http.route('/openshop/products/<model("openshop.products"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('openshop.object', {
            'object': obj
        })
