from .context import one_key
from one_key.Credential import Credential

import unittest

class TestCredential(unittest.TestCase):
    def test_str(self):
        c = Credential('x.com', 'hbrt', 'pswd')
        self.assertEqual(c.__str__(), 'Website: x.com; Username: hbrt; Password: pswd')

