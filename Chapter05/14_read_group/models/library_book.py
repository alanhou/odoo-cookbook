import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    date_release = fields.Date('Release Date')
    cost_price = fields.Float('Book Cost')
    category_id = fields.Many2one('library.book.category')
    author_ids = fields.Many2many('res.partner', string='Authors')

    def grouped_data(self):
        data = self._get_average_cost()
        _logger.info('Grouped Data %s' %data)

    def _get_average_cost(self):
        grouped_result = self.read_group(
            [('cost_price', '!=', False)], # Domain
            ['category_id', 'cost_price:avg'], # Fields to access
            ['category_id'] # group by
        )
        return grouped_result


class BookCategory(models.Model):
    _name = 'library.book.category'
    _description = 'Library Book Category'

    name = fields.Char('Category')
    description = fields.Text('Description')
