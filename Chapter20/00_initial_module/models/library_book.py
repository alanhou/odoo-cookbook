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
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State', default="available")
    color = fields.Integer()

    def make_available(self):
        self.write({'state': 'available'})
        return True

    def make_lost(self):
        self.write({'state': 'lost'})
        return True
