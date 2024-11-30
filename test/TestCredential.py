from .context import one_key
from one_key.Credential import Credential

import unittest


class TestCredential(unittest.TestCase):
    def test_init(self):
        c = Credential('x.com', 'hbrt', 'pswd')
        self.assertEqual(c.get_website(), 'x.com')
        self.assertEqual(c.get_username(), 'hbrt')
        self.assertEqual(c.get_password(), 'pswd')

        c = Credential('x123.com', 'h123brt', '123')
        self.assertEqual(c.get_website(), 'x123.com')
        self.assertEqual(c.get_username(), 'h123brt')
        self.assertEqual(c.get_password(), '123')

        with self.assertRaises(ValueError):
            Credential('', '', '')

        with self.assertRaises(ValueError):
            Credential(' ', ' ', ' ')

        with self.assertRaises(ValueError):
            Credential('   ', '   ', '    ')

        with self.assertRaises(ValueError):
            Credential('', 'name', '  ')

    def test_eq(self):
        c1 = Credential('x.com', 'hbrt', 'pswd')
        c2 = Credential('x.com', 'hbrt', 'pswd')
        self.assertTrue(c1 == c2)

        c2.set_website('y.com')
        self.assertFalse(c1 == c2)

        c2 = Credential('x.com', 'hbrt', 'diff')
        self.assertFalse(c1 == c2)

        c2 = Credential('x.com', 'asdf', 'pswd')
        self.assertFalse(c1 == c2)

    def test_str(self):
        c = Credential('x.com', 'hbrt', 'pswd')
        self.assertEqual(
            c.__str__(), 'Website: x.com; Username: hbrt; Password: pswd')

        c = Credential('x123.com', 'h123brt', '123')
        self.assertEqual(
            c.__str__(), 'Website: x123.com; Username: h123brt; Password: 123')
