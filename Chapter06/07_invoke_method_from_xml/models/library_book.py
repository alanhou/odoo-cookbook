import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'date_release desc, name'
    # _rec_name = "short_name"
    name = fields.Char('Title', required=True, index=True)
    short_name = fields.Char('Short Title', translate=True, index=True)
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        'State', default="draft")
    description = fields.Html('Description', sanitize=True, strip_style=False)
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of Pages',
                           groups='base.group_user',
                           states={'lost': [('readonly', True)]},
                           help='整书页数', company_dependent=False)
    reader_rating = fields.Float(
        'Reader Average Rating',
        digits=(14, 4),  # 可选精度 (total, decimals),
    )
    author_ids = fields.Many2many('res.partner', string='Authors')
    cost_price = fields.Float('Book Cost', digits='Book Price')
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary('Retail Price') # 可选属性currency_field='currency_id'，在币种字段使用currency_id之外的名称时使用
    publisher_id = fields.Many2one(
        'res.partner', string='Publisher',
        # optional:
        ondelete='set null', context={}, domain=[],
    )
    category_id = fields.Many2one('library.book.category')

    def name_get(self):
        """本方法用于自定义记录的显示名称"""
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result

    @api.model
    def _update_book_price(self):
        # 注：真实场景可能会很复杂，这里我们仅对成本价加10
        _logger.info('Method update_book_price called from XML')
        all_books = self.search([])
        for book in all_books:
            book.cost_price += 10


class ResPartner(models.Model):
    _inherit = 'res.partner'
    published_book_ids = fields.One2many(
        'library.book', 'publisher_id',
        string='Published Books',
    )
    authored_book_ids = fields.Many2many(
        'library.book',
        string='Authored Books',
        # relation='library_book_res_partner_rel' #optional
    )