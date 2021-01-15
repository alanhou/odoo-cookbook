from os.path import join
from odoo import models, exceptions, api
import logging

EXPORT_DIR = '/srv/exports'
_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def export_stock_level(self, stock_location):
        _logger.info('export stock level for %s', stock_location.name)
        products = self.with_context(
            location=stock_location.id
        ).search([])
        products = products.filtered('qty_available')
        _logger.debug('%d products in the location', len(products))
        fname = join(EXPORT_DIR, 'stock_level.txt')
        try:
            with open(fname, 'w') as fobj:
                for prod in products:
                    fobj.write('%s\t%f\n' %(prod.name, prod.qty_available))
        except IOError:
            _logger.exception('Error while writing to %s in %s', 'stock_level.txt', EXPORT_DIR)
            raise exceptions.UserError('unable to save file')
