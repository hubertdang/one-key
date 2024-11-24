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
        self.assertEqual(pm.get_user(u1.get_username()), None)
        self.assertFalse(pm.remove_user(u1.get_username()))

        pm.add_user(u1)
        pm.add_user(u2)

        self.assertTrue(pm.remove_user(u1.get_username()))
        self.assertEqual(pm.get_user(u1.get_username()), None)
        self.assertTrue(pm.remove_user(u2.get_username()))
        self.assertEqual(pm.get_user(u2.get_username()), None)

    def test_sign_in(self):
        pm = PasswordManager()

    def test_set_username(self):
        pm = PasswordManager()


