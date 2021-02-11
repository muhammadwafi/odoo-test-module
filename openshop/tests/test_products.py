from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

def gen_str(length):
    import random
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(allowed_chars) for i in range(length))


class TestProducts(TransactionCase):
    
    def test_products_name(self):
        record = self.env['openshop.products'].create({
            'name': 'Products 001',
            'description': 'Some description',
            'price': 24.0,
            'size': 'm',
            'category': 't-shirt',
        })
        self.assertTrue(len(record.name) < 140)
        
    def test_same_len_products_name(self):
        """ Should be fine """
        record = self.env['openshop.products'].create({
            'name': gen_str(140),
            'price': 34.0,
            'size': 'l',
            'category': 't-shirt',
            'description': 'Some desc',
        })
        if self.assertRaises(ValidationError, msg="Name is at max chars"):
            record._truncate_text(record.name, 140)
    
    def test_long_chars_products_name(self):
        """ Should be failed """
        record = self.env['openshop.products'].create({
            'name': gen_str(144),
            'price': 34.0,
            'size': 'l',
            'category': 't-shirt',
            'description': 'Some desc',
        })
        with self.assertRaises(ValidationError, msg="Name is more than 140 chars"):
            record._truncate_text(record.name, 140)
    
    def test_products_active_by_default(self):
        """ Should be failed """
        record = self.env['openshop.products'].create({
            'name': 'Products 002',
            'price': 34.0,
            'size': 'l',
            'category': 't-shirt',
            'description': 'Some desc',
        })
        self.assertEqual(record.is_active, 1)