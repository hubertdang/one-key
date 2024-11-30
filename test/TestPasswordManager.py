from .context import one_key
from one_key.PasswordManager import PasswordManager
from one_key.User import User
from one_key.Credential import Credential

import unittest

class TestPasswordManager(unittest.TestCase):
    def test_init(self):
        pm = PasswordManager()

    def test_add_user(self):
        pm = PasswordManager()

        u1 = User('hbrt', 'key')
        u2 = User('hbrt', 'diff_key')
        u3 = User('saal', 'orange')

        self.assertTrue(pm.add_user(u1))
        self.assertFalse(pm.add_user(u2))
        self.assertFalse(pm.add_user(u1))
        self.assertTrue(pm.add_user(u3))

    def test_remove_user(self):
        pm = PasswordManager()

        u1 = User('hbrt', 'key')
        u2 = User('saal', 'orange')

        self.assertFalse(pm.remove_user('some guy'))
        self.assertFalse(pm.remove_user('hbrt'))

        pm.add_user(u1)

        self.assertFalse(pm.remove_user(u2.get_username()))
        self.assertTrue(pm.remove_user(u1.get_username()))

        pm.add_user(u1)
        pm.add_user(u2)

        self.assertTrue(pm.remove_user(u1.get_username()))
        self.assertTrue(pm.remove_user(u2.get_username()))

    def test_is_valid_user(self):
        pm = PasswordManager()
        
        u1 = User('hbrt', 'key')
        u2 = User('saal', 'orange')

        self.assertFalse(pm.is_valid_user('hbrt'))
        
        pm.add_user(u1)
        self.assertTrue(pm.is_valid_user('hbrt'))

        pm.add_user(u2)
        self.assertTrue(pm.is_valid_user('saal'))
        
        pm.remove_user('hbrt')
        self.assertFalse(pm.is_valid_user('hbrt'))

        pm.remove_user('saal')
        self.assertFalse(pm.is_valid_user('saa'))

    def test_sign_in(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')
        u2 = User('saal', 'orange')

        pm.add_user(u1)
        self.assertTrue(pm.sign_in('hbrt', 'key'))

        pm.add_user(u2)
        self.assertFalse(pm.sign_in('saal', 'wrong'))

        self.assertFalse(pm.sign_in('marko', 'pswd'))

    def test_sign_out(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')

        self.assertFalse(pm.sign_out('hbrt'))
        
        pm.add_user(u1)
        self.assertFalse(pm.sign_out('hbrt'))
        pm.sign_in('hbrt', 'key')
        self.assertTrue(pm.sign_out('hbrt'))

    def test_is_signed_in(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')

        self.assertFalse(pm.is_signed_in('hbrt'))

        pm.add_user(u1)
        self.assertFalse(pm.is_signed_in('hbrt'))

        pm.sign_in('hbrt', 'key')
        self.assertTrue(pm.is_signed_in('hbrt'))

    def test_get_key(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')

        self.assertEqual(pm.get_key('hbrt'), None)
        
        pm.add_user(u1)
        self.assertEqual(pm.get_key('hbrt'), None)

        pm.sign_in('hbrt', 'key')
        self.assertEqual(pm.get_key('hbrt'), 'key')

    def test_set_key(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')

        self.assertFalse(pm.set_key('hbrt', 'new key'))

        pm.add_user(u1)
        self.assertFalse(pm.set_key('hbrt', 'new key'))

        pm.sign_in('hbrt', 'key')
        self.assertTrue(pm.set_key('hbrt', 'new key'))

    def test_set_username(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')

        self.assertFalse(pm.set_username('hbrt', 'new username'))

        pm.add_user(u1)
        self.assertFalse(pm.set_username('hbrt', 'new username'))

        pm.sign_in('hbrt', 'key')
        self.assertTrue(pm.set_username('hbrt', 'new username'))

    def test_get_credential(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')
        c1 = Credential('x.com', 'hdang', 'pswd')

        pm.add_user(u1)
        self.assertEqual(pm.get_credential('hbrt', 'x.com'), None)

        pm.sign_in('hbrt', 'key')
        pm.add_credential('hbrt', c1)
        pm.sign_out('hbrt')
        self.assertEqual(pm.get_credential('hbrt', 'x.com'), None)

        pm.sign_in('hbrt', 'key')
        self.assertEqual(pm.get_credential('hbrt', 'x.com'), c1)

        self.assertEqual(pm.get_credential('dina', 'x.com'), None)

    def test_add_credential(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')
        c1 = Credential('x.com', 'hdang', 'pswd')
        pm.add_user(u1)

        self.assertFalse(pm.add_credential('nonuser', c1))

        self.assertFalse(pm.add_credential('hbrt', c1))

        pm.sign_in('hbrt', 'key')
        self.assertTrue(pm.add_credential('hbrt', c1))

    def test_remove_credential(self):
        pm = PasswordManager()
        u1 = User('hbrt', 'key')
        c1 = Credential('x.com', 'hdang', 'pswd')

        self.assertFalse(pm.remove_credential('hbrt', 'x.com'))

        self.assertTrue(pm.add_user(u1))

        self.assertFalse(pm.remove_credential('nonuser', 'x.com'))

        self.assertFalse(pm.remove_credential('hbrt', 'x.com'))

        pm.sign_in('hbrt', 'key')
        pm.add_credential('hbrt', c1)
        self.assertTrue(pm.remove_credential('hbrt', 'x.com'))

