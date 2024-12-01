from .context import one_key
from one_key.PasswordManager import PasswordManager
from one_key.User import User
from one_key.Credential import Credential

import unittest


class TestPasswordManager(unittest.TestCase):
    def setUp(self):
        self.pm = PasswordManager()

    def test_add_user(self):
        """Requirements:

        => can add multiple users.
        => cannot add a user if another user under the same username already exists.
        """
        u1 = User('hbrt', 'key')
        u2 = User('hbrt', 'diff_key')
        u3 = User('saal', 'orange')

        self.assertTrue(self.pm.add_user(u1))
        self.assertFalse(self.pm.add_user(u2))
        self.assertFalse(self.pm.add_user(u1))
        self.assertTrue(self.pm.add_user(u3))

    def test_remove_user(self):
        """Requirements:

        => should only remove a user that exists.
        => to remove a user, the user to remove must be signed in.
        => after removing a user, no one should be signed in.
        """
        u1 = User('hbrt', 'key')

        # try removing a non-existant user
        self.assertFalse(self.pm.remove_user('some guy'))
        self.assertFalse(self.pm.remove_user('hbrt'))

        # try removing an existing user that is not signed in
        self.pm.add_user(u1)
        self.assertFalse(self.pm.remove_user('hbrt'))

        # try removing an existing user that is signed in
        self.pm.add_user(u1)
        self.pm.sign_in('hbrt', 'key')
        self.assertTrue(self.pm.remove_user('hbrt'))
        self.assertFalse(self.pm.anyone_signed_in())

    def test_get_num_users(self):
        """Requirements:

        => should return number of existing users, signed in, or not.
        => should update when users are added/removed.
        => can only return a positive number or 0.
        """
        u1 = User('hbrt', 'key')
        u2 = User('saal', 'orange')
        u3 = User('matt', 'key3')

        self.assertEqual(self.pm.get_num_users(), 0)

        # try to return a negative number
        self.pm.sign_in('nobody', 'nobody_key')
        self.pm.remove_user('nobody')
        self.assertEqual(self.pm.get_num_users(), 0)

        self.pm.add_user(u1)
        self.assertEqual(self.pm.get_num_users(), 1)

        self.pm.add_user(u2)
        self.assertEqual(self.pm.get_num_users(), 2)

        self.pm.sign_in('saal', 'orange')
        self.pm.remove_user('saal')
        self.assertEqual(self.pm.get_num_users(), 1)

        self.pm.add_user(u2)
        self.pm.add_user(u3)
        self.assertEqual(self.pm.get_num_users(), 3)

    def test_user_exists(self):
        """Requirements:

        => if the user has been added and not removed, they exist.
        => if a user is removed, they are no longer an existing user.
        => sign in/out status of user does not affect this.
        => multiple users can be considered "existing users".
        => existence of a user is not impacted by other users.
        """
        u1 = User('hbrt', 'key')
        u2 = User('saal', 'orange')

        # try checking a user that hasn't been added
        self.assertFalse(self.pm.user_exists('hbrt'))

        # try checking a user that's been added, but isn't signed in
        self.pm.add_user(u1)
        self.assertTrue(self.pm.user_exists('hbrt'))

        # try when that user has been signed in
        self.pm.sign_in('hbrt', 'key')
        self.assertTrue(self.pm.user_exists('hbrt'))

        # make sure multiple users can be valid users
        self.pm.add_user(u2)
        self.assertTrue(self.pm.user_exists('saal'))
        self.assertTrue(self.pm.user_exists('hbrt'))

        # users that get removed are no longer valid
        self.pm.remove_user('hbrt')
        self.assertFalse(self.pm.user_exists('hbrt'))

        # remaining user that was not removed should still be valid
        self.assertTrue(self.pm.user_exists('saal'))

    def test_sign_in(self):
        """Requirements:

        => can only sign in users that exist.
        => a user will not be signed in if their key is incorrect.
        => a user cannot sign in more than once, unless they have signed out first.
        => only one user can be signed in at a time.
        """
        u1 = User('hbrt', 'key')
        u2 = User('saal', 'orange')

        # signing in a user that doesn't exist
        self.assertFalse(self.pm.sign_in('hbrt', 'key'))

        # signing in a user that exists but with the wrong key
        self.pm.add_user(u1)
        self.assertFalse(self.pm.sign_in('hbrt', 'wrongkey'))

        # signing in a user that exists with the correct key
        self.assertTrue(self.pm.sign_in('hbrt', 'key'))

        # sign in again
        self.assertFalse(self.pm.sign_in('hbrt', 'key'))

        # sign in another user while u1 is still signed in
        self.pm.add_user(u2)
        self.assertFalse(self.pm.sign_in('saal', 'orange'))

        # sign out u1 and then try again with u2
        self.pm.sign_out('hbrt')
        self.assertTrue(self.pm.sign_in('saal', 'orange'))

    def test_sign_out(self):
        """Requirements:

        => can only sign out a user that is signed in.
        """
        u1 = User('hbrt', 'key')

        # sign out a non-existent user
        self.assertFalse(self.pm.sign_out('hbrt'))

        # sign out an existing user that isn't signed in
        self.pm.add_user(u1)
        self.assertFalse(self.pm.sign_out('hbrt'))

        # sign out an existing user that is signed in
        self.pm.sign_in('hbrt', 'key')
        self.assertTrue(self.pm.sign_out('hbrt'))

        # sign them out again before signing them back in
        self.assertFalse(self.pm.sign_out('hbrt'))

    def test_get_key(self):
        """Requirements:

        => only gets the key if user is signed in (meaning they must also exist).
        """
        u1 = User('hbrt', 'key')

        # get key for a non-existent user
        self.assertEqual(self.pm.get_key('hbrt'), None)

        # get key for existing user that is not signed in
        self.pm.add_user(u1)
        self.assertEqual(self.pm.get_key('hbrt'), None)

        # get key for existing user that is signed in
        self.pm.sign_in('hbrt', 'key')
        self.assertEqual(self.pm.get_key('hbrt'), 'key')

    def test_set_key(self):
        """Requirements:

        => user must be signed in (and therefore exist) to set their key.
        """
        u1 = User('hbrt', 'key')

        # set key for a non-existent user
        self.assertFalse(self.pm.set_key('hbrt', 'new key'))

        # set key for an existing user that is not signed in
        self.pm.add_user(u1)
        self.assertFalse(self.pm.set_key('hbrt', 'new key'))

        # set key for an existing user that is signed in
        self.pm.sign_in('hbrt', 'key')
        self.assertTrue(self.pm.set_key('hbrt', 'new key'))

    def test_set_username(self):
        """Requirements:

        => user must be signed in (and therefore exist) to set their username.
        """
        u1 = User('hbrt', 'key')

        # set username for a non-existent user
        self.assertFalse(self.pm.set_username('hbrt', 'new username'))

        # set username for an existing user that is not signed in
        self.pm.add_user(u1)
        self.assertFalse(self.pm.set_username('hbrt', 'new username'))

        # set username for an existing user that is signed in
        self.pm.sign_in('hbrt', 'key')
        self.assertTrue(self.pm.set_username('hbrt', 'new username'))

    # def test_get_credential(self):
    #     u1 = User('hbrt', 'key')
    #     c1 = Credential('x.com', 'hdang', 'pswd')

    #     self.pm.add_user(u1)
    #     self.assertEqual(self.pm.get_credential('hbrt', 'x.com'), None)

    #     self.pm.sign_in('hbrt', 'key')
    #     self.pm.add_credential('hbrt', c1)
    #     self.pm.sign_out('hbrt')
    #     self.assertEqual(self.pm.get_credential('hbrt', 'x.com'), None)

    #     self.pm.sign_in('hbrt', 'key')
    #     self.assertEqual(self.pm.get_credential('hbrt', 'x.com'), c1)

    #     self.assertEqual(self.pm.get_credential('dina', 'x.com'), None)

    # def test_add_credential(self):
    #     u1 = User('hbrt', 'key')
    #     c1 = Credential('x.com', 'hdang', 'pswd')
    #     self.pm.add_user(u1)

    #     self.assertFalse(self.pm.add_credential('nonuser', c1))

    #     self.assertFalse(self.pm.add_credential('hbrt', c1))

    #     self.pm.sign_in('hbrt', 'key')
    #     self.assertTrue(self.pm.add_credential('hbrt', c1))

    # def test_remove_credential(self):
    #     u1 = User('hbrt', 'key')
    #     c1 = Credential('x.com', 'hdang', 'pswd')

    #     self.assertFalse(self.pm.remove_credential('hbrt', 'x.com'))

    #     self.assertTrue(self.pm.add_user(u1))

    #     self.assertFalse(self.pm.remove_credential('nonuser', 'x.com'))

    #     self.assertFalse(self.pm.remove_credential('hbrt', 'x.com'))

    #     self.pm.sign_in('hbrt', 'key')
    #     self.pm.add_credential('hbrt', c1)
    #     self.assertTrue(self.pm.remove_credential('hbrt', 'x.com'))
