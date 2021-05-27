# -*- coding: utf-8 -*-
from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _inherit = ['website.seo.metadata', 'website.multi.mixin']

    _order = 'date_release desc, name'

    name = fields.Char('Title', required=True)
    short_name = fields.Char('Short Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many('res.partner', string='Authors')
    image = fields.Binary(attachment=True)
    html_description = fields.Html()
    book_issue_ids = fields.One2many('book.issue', 'book_id')
    restrict_country_ids = fields.Many2many('res.country')

    def _default_website_meta(self):
        res = super(LibraryBook, self)._default_website_meta()
        res['default_opengraph']['og:image'] = self.env['website'].image_url(self, 'image')
        res['default_twitter']['twitter:image'] = self.env['website'].image_url(self, 'image')
        return res

    def name_get(self):
        """ This method used to customize display name of the record """
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result


class LibraryBookIssues(models.Model):
    _name = 'book.issue'
    _inherit = ['utm.mixin']

    book_id = fields.Many2one('library.book', required=True)
    submitted_by = fields.Many2one('res.users')
    issue_description = fields.Text()