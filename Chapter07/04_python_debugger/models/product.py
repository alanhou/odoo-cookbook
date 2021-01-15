from os.path import join
from odoo import models, exceptions, api
import logging

EXPORT_DIR = '/srv/exports'
_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def export_stock_level(self, stock_location):
        import pdb; pdb.set_trace()
        products = self.with_context(
            location=stock_location.id).search([])
        fname = join(EXPORT_DIR, 'stock_level.txt')
        try:
            with open(fname, 'w') as fobj:
                for prod in products:
                    fobj.write('%s\t%f\n' %(prod.name, prod.qty_available))
        except IOError:
            raise exceptions.UserError('unable to save file')
