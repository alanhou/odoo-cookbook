# -*- coding: utf-8 -*-
from odoo import models, fields, _
from odoo.exceptions import UserError


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    state = fields.Selection(
        [('available', 'Available'),
         ('borrowed', 'Borrowed'),
         ('lost', 'Lost')],
        'State', default="available")
    color = fields.Integer()

    def make_available(self):
        self.ensure_one()
        self.state = 'available'

    def make_lost(self):
        self.ensure_one()
        self.state = 'lost'
