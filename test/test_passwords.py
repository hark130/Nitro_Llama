# Standard Imports
import unittest
# Third Party Imports
# Local Imports
from nitro_llama.nill_passwords import _find_password

class Passwords_Unit_Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Passwords_Unit_Tests_Normal(Passwords_Unit_Tests):

    def test_Normal_01(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
