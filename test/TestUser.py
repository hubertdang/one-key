from .context import one_key
from one_key.User import User
from one_key.Credential import Credential

import unittest

class TestUser(unittest.TestCase):
    def test_init(self):
        u = User('dina', 'key1')
        u.sign_in('key1')
        self.assertEqual(u.get_username(), 'dina')
        self.assertEqual(u.get_key(), 'key1')
        
        with self.assertRaises(ValueError):
            u = User('', '')

        with self.assertRaises(ValueError):
            u = User('  ', ' ')

        with self.assertRaises(ValueError):
            u = User('', 'k123ey')

        with self.assertRaises(ValueError):
            u = User('dina', '  ')

    def test_eq(self):
        u1 = User('dina', 'key')
        u2 = User('dina', 'key')
        self.assertTrue(u1 == u2)

        u2 = User('bina', 'key')
        self.assertFalse(u1 == u2)

        u2 = User('dina', 'other key')
        self.assertFalse(u1 == u2)

        u2 = User('dina', 'key')
        u1.sign_in('key')
        self.assertFalse(u1 == u2)

        u2.sign_in('key')
        c = Credential('x.com', 'tree', 'secret')
        u1.add_credential(c)
        self.assertFalse(u1 == u2)
        u2.add_credential(c)
        self.assertTrue(u1 == u2)

    def test_sign_in(self):
        u = User('dina', 'key')
        self.assertTrue(u.sign_in('key'))
        self.assertTrue(u.is_signed_in())

        u = User('bob', 'pswd')
        self.assertFalse(u.sign_in('wrongkey'))
        self.assertFalse(u.is_signed_in())
        self.assertFalse(u.sign_in(''))
        self.assertFalse(u.is_signed_in())
        self.assertFalse(u.sign_in('    '))
        self.assertFalse(u.is_signed_in())

    def test_sign_out(self):
        u = User('dina', 'key')
        u.sign_in('key')
        self.assertTrue(u.sign_out())
        self.assertFalse(u.is_signed_in())
        self.assertFalse(u.sign_out())
        self.assertFalse(u.is_signed_in())

    def test_is_signed_in(self):
        u = User('dina', 'key')
        self.assertTrue(u.sign_in('key'))
        self.assertTrue(u.is_signed_in())

        u = User('bob', 'pswd')
        self.assertFalse(u.is_signed_in())

    def test_get_key(self):
        u = User('dina', 'key')
        u.sign_in('key')
        self.assertEqual(u.get_key(), 'key')
        u.sign_out()
        self.assertEqual(u.get_key(), None)

    def test_set_key(self):
        u = User('dina', 'key')
        u.sign_in('key')
        self.assertTrue(u.set_key('new_key'))
        self.assertEqual(u.get_key(), 'new_key')
        u.sign_out()
        self.assertFalse(u.set_key('newer_key'))
        u.sign_in('new_key')
        self.assertTrue(u.set_key('newer_key'))
        self.assertEqual(u.get_key(), 'newer_key')

        self.assertFalse(u.set_key(''))
        self.assertEqual(u.get_key(), 'newer_key')
        self.assertFalse(u.set_key('  '))
        self.assertEqual(u.get_key(), 'newer_key')
        self.assertFalse(u.set_key(None))
        self.assertEqual(u.get_key(), 'newer_key')

    def test_get_username(self):
        u = User('dina', 'key')
        u.sign_in('key')
        self.assertEqual(u.get_username(), 'dina')
        u.sign_out()
        self.assertEqual(u.get_username(), 'dina')

    def test_set_username(self):
        u = User('dina', 'key')
        u.sign_in('key')
        self.assertTrue(u.set_username('bina'))
        self.assertEqual(u.get_username(), 'bina')
        u.sign_out()
        self.assertFalse(u.set_username('pina'))
        self.assertEqual(u.get_username(), 'bina')

    def test_get_credential(self):
        u = User('dina', 'key')

    def test_add_credential(self):
        u = User('dina', 'key')
        u.sign_in('key')

        c1 = Credential('x.com', 'uname', 'pswd')

        self.assertTrue(u.add_credential(c1))
        self.assertEqual(u.get_credential(c1.get_website()), c1)

        c2 = Credential('x.com', 'diff', 'diff')

        self.assertFalse(u.add_credential(c2))
        self.assertEqual(u.get_credential(c2.get_website()), c1)

    def test_remove_credential(self):
        u = User('dina', 'key')
        u.sign_in('key')
        
        self.assertFalse(u.remove_credential('x.com'))

        c1 = Credential('x.com', 'uname', 'pswd')
        u.add_credential(c1)
        self.assertFalse(u.remove_credential('twitter.com'))
        self.assertTrue(u.remove_credential('x.com'))

    def test_get_websites(self):
        self.assertTrue(False)

