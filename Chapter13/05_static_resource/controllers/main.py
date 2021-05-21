# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/demo_page', type='http', auth='none')
    def demo_page(self):
        image_url = '/my_library/static/src/image/bug.jpg'
        html_result = """<html>
            <body>
                <img src="%s"/>
            </body>
        </html>""" % image_url
        return html_result
