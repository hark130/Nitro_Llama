# Standard Imports
import unittest
# Third Party Imports
# Local Imports
from nitro_llama.nill_passwords import _find_password

class Passwords_Unit_Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.min_num_chars = 5       # Minimum number of chars per position
        self.num_positions = 5       # Number of positions in the password
        self.test_error = 'ERROR: '  # Standardize exceptions of failed tests
        super().__init__(*args, **kwargs)

    def execute_pass_test(self, expected_str: str, test_input: tuple):
        '''
        Purpose: Execute the test, respond to results, provide verbose
            human-readable feedback on failures
        Parameters:
            test_input: Expected return value from the function call
            formatted_input: tuple of formatted user input to use as the
                argument
        Notes:
            This method does not validate its input.
        Returns: None
        '''
        # LOCAL VARIABLES
        ret_val = _find_password(test_input)

        # VALIDATE
        if expected_str != ret_val:
            self.fail(f'Expected "{expected_str}" but received "{ret_val}"')

    def prepare_test_input(self, word_list: list):
        # INPUT VALIDATION
        if not isinstance(word_list, list):
            raise TypeError(f'{self.test_error}"word_list" must be a list '
                            f'instead of a {type(word_list)}')
        elif self.num_positions != len(word_list):
            raise ValueError(f'{self.test_error}"word_list" must have '
                             f'{self.num_positions} entries instead of '
                             f'{len(word_list)}')
        else:
            for word in word_list:
                if not isinstance(word, str):
                    raise TypeError(f'{self.test_error}Found a '
                                    f'{type(word)} in "word_list"')
                elif self.min_num_chars > len(word):
                    raise ValueError(f'{self.test_error}{word} must be '
                                     f'of length {self.min_num_chars}')

        # LOCAL VARIABLES
        pos1 = self.split_string(word_list[0])  # Selections for position 1
        pos2 = self.split_string(word_list[1])  # Selections for position 2
        pos3 = self.split_string(word_list[2])  # Selections for position 3
        pos4 = self.split_string(word_list[3])  # Selections for position 4
        pos5 = self.split_string(word_list[4])  # Selections for position 5

        # DONE
        return tuple((pos1, pos2, pos3, pos4, pos5))

    def split_string(self, word: str):
        # LOCAL VARIABLES
        ret_list = []

        # INPUT VALIDATION
        if not isinstance(word, str):
            raise TypeError(f'"word" must be a str instead of a {type(word)}')
        elif not word:
            raise ValueError('"word" may be blank')

        # SPLIT IT
        for char in word:
            ret_list.append(char)

        # DONE
        return ret_list


class Passwords_Unit_Tests_Normal(Passwords_Unit_Tests):

    def test_normal_01(self):
        '''
        Normal 1 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'prxbie'])
        self.execute_pass_test('other', test_input)

    def test_normal_02(self):
        '''
        Normal 2 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['fazund', 'oairyg', 'hdytav', 'bqiagr', 'dlnqrg'])
        self.execute_pass_test('again', test_input)

    def test_normal_03(self):
        '''
        Normal 3 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['wabosh', 'wirngh', 'courig', 'ywtzfx', 'hpegcu'])
        self.execute_pass_test('write', test_input)

    def test_normal_04(self):
        '''
        Normal 4 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['zdsnqo', 'gyrmtc', 'wohcin', 'xgklmf', 'kzsblj'])
        self.execute_pass_test('still', test_input)

    def test_normal_05(self):
        '''
        Normal 5 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['krsdxf', 'tkcgiy', 'noizbu', 'rdfyxs', 'wufkyx'])
        self.execute_pass_test('study', test_input)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
