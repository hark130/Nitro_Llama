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

    def run_test_pass(self, expected_str: str, test_input: tuple):
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

    def run_test_fail(self, test_input, exception_type,
                      exception_msg: str):
        '''
        Purpose: Execute the test, respond to results, provide verbose
            human-readable feedback on failures
        Parameters:
            formatted_input: input, valid or otherwise, to pass to the
                function call
            exception_type: The type of exception to expect
            exception_msg: The exception message, as a string, to expect
        Notes:
            This method checks exception_msg against the Exception's args[0]
        Returns: None
        '''
        try:
            _find_password(test_input)
        except exception_type as err:
            if err.args[0] != exception_msg:
                self.fail(f'Expected "{exception_msg}" but received '
                          f'"{err.args[0]}"')
        except Exception as err:
            self.fail(f'Expected {exception_type}({exception_msg}) but '
                      f'received {repr(err)}')
        else:
            self.fail(f'Expected {exception_type}({exception_msg}) but '
                      'no Exception was raised')

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
        self.run_test_pass('other', test_input)

    def test_normal_02(self):
        '''
        Normal 2 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['fazund', 'oairyg', 'hdytav', 'bqiagr', 'dlnqrg'])
        self.run_test_pass('again', test_input)

    def test_normal_03(self):
        '''
        Normal 3 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['wabosh', 'wirngh', 'courig', 'ywtzfx', 'hpegcu'])
        self.run_test_pass('write', test_input)

    def test_normal_04(self):
        '''
        Normal 4 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['zdsnqo', 'gyrmtc', 'wohcin', 'xgklmf', 'kzsblj'])
        self.run_test_pass('still', test_input)

    def test_normal_05(self):
        '''
        Normal 5 - Standard, valid, normalized input from actual gameplay
        '''
        test_input = self.prepare_test_input(
            ['krsdxf', 'tkcgiy', 'noizbu', 'rdfyxs', 'wufkyx'])
        self.run_test_pass('study', test_input)


class Passwords_Unit_Tests_Error(Passwords_Unit_Tests):

    def test_error_01(self):
        '''
        Error 1 - Parameter is the wrong type (not a tuple)
        '''
        test_input = ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'prxbie']
        exp_err_msg = 'The "user_input" argument is of type ' + \
                      f'{type(test_input)} instead of a tuple'
        self.run_test_fail(test_input, TypeError, exp_err_msg)

    def test_error_02(self):
        '''
        Error 2 - Parameter doesn't have enough elements (4)
        '''
        test_input = self.prepare_test_input(
            ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'prxbie'])[:4]
        exp_err_msg = 'The "user_input" argument holds ' + \
                      f'{len(test_input)} positions instead of 5'
        self.run_test_fail(test_input, ValueError, exp_err_msg)

    def test_error_03(self):
        '''
        Error 3 - Parameter has too many elements (6)
        '''
        test_input = self.prepare_test_input(
            ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'prxbie'])
        test_input = test_input + tuple((test_input[0]))
        exp_err_msg = 'The "user_input" argument holds ' + \
                      f'{len(test_input)} positions instead of 5'
        self.run_test_fail(test_input, ValueError, exp_err_msg)

    def test_error_04(self):
        '''
        Error 4 - Parameter contains a non-list element
        '''
        test_input = self.prepare_test_input(
            ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'prxbie'])[:4] + \
            tuple(('X'))
        exp_err_msg = 'The "user_input" argument contains a ' + \
                      f'non-list of type {type(test_input[4])}'
        self.run_test_fail(test_input, TypeError, exp_err_msg)

    def test_error_05(self):
        '''
        Error 5 - Parameter contains an empty list element
        '''
        test_input = tuple((['p', 'c', 'n', 'r', 'o', 'x'],
                            ['i', 'f', 'j', 't', 'u', 'p'],
                            ['p', 'w', 'k', 'h', 'q', 'r'],
                            ['i', 'w', 'e', 'h', 'm', 'o'],
                            []))
        exp_err_msg = 'The "user_input" argument contained a ' + \
                      f'list that contained {len(test_input[4])} ' + \
                      'characters instead of 6'
        self.run_test_fail(test_input, ValueError, exp_err_msg)

    def test_error_06(self):
        '''
        Error 6 - Parameter contains a list element with a non-string
        '''
        test_input = tuple((['p', 'c', 'n', 'r', 'o', 'x'],
                            ['i', 'f', 'j', 't', 'u', 'p'],
                            ['p', 'w', 'k', 'h', 'q', 'r'],
                            ['i', 'w',  3,  'h', 'm', 'o'],
                            ['p', 'r', 'x', 'b', 'i', 'e']))
        exp_err_msg = 'The "user_input" argument contains ' + \
                      f'an entry with a non-string of type {type(3)}'
        self.run_test_fail(test_input, TypeError, exp_err_msg)

    def test_error_07(self):
        '''
        Error 7 - Parameter contains a list with non enough input
        '''
        test_input = tuple((['p', 'c', 'n', 'r', 'o', 'x'],
                            ['i', 'f', 'j', 't', 'u', 'p'],
                            ['p', 'w', 'k', 'h', 'r'],
                            ['i', 'w', 'e', 'h', 'm', 'o'],
                            ['p', 'r', 'x', 'b', 'i', 'e']))
        exp_err_msg = 'The "user_input" argument contained a ' + \
                      'list that contained 5 characters instead of 6'
        self.run_test_fail(test_input, ValueError, exp_err_msg)

    def test_error_08(self):
        '''
        Error 8 - Parameter contains input that has no match
        '''
        test_input = self.prepare_test_input(
            ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'jqxazo'])
        exp_err_msg = 'Password not found'
        self.run_test_fail(test_input, RuntimeError, exp_err_msg)

    def test_error_09(self):
        '''
        Error 9 - Parameter is the wrong type (not a tuple)
        '''
        test_input = self.prepare_test_input(
            ['awsjqx', 'bhmjqx', 'oeajqx', 'urljqx', 'teljqx'])
        exp_err_msg = "Too many password matches: ['about', 'small', 'where']"
        self.run_test_fail(test_input, RuntimeError, exp_err_msg)


class Passwords_Unit_Tests_Boundary(Passwords_Unit_Tests):

    def test_boundary_01(self):
        '''
        Boundary 1 - Standard, valid, normalized input from actual gameplay
        Notes:
            This test may mirror input from a Normal unit test but here it
                represents the minimum valid input
        '''
        test_input = self.prepare_test_input(
            ['pcnrox', 'ifjtup', 'pwkhqr', 'iwehmo', 'prxbie'])
        self.run_test_pass('other', test_input)

    def test_boundary_02(self):
        '''
        Boundary 2 - Valid input from actual gameplay with "typos" thrown in
        Notes:
            In the heat of the moment mistakes are made: spoken language
                is misunderstood, "state" is forgotten, etc.
        '''
        test_input = self.prepare_test_input(
            ['pcnroxpcnroxp', 'ifjtupjqx', 'pwkhqriwe', 'iwehmo', 'prxbie'])
        self.run_test_pass('other', test_input)

    def test_boundary_03(self):
        '''
        Boundary 7 - Invalid input based on input from actual gameplay
        Notes:
            This test may mirror input from an Error unit test but it has
                been subtly changed.  The thought here is the user hits
                the final return prematurely.
        '''
        test_input = tuple((['p', 'c', 'n', 'r', 'o', 'x'],
                            ['i', 'f', 'j', 't', 'u', 'p'],
                            ['p', 'w', 'k', 'h', 'q', 'r'],
                            ['i', 'w', 'e', 'h', 'm', 'o'],
                            ['p', 'r', 'x', 'b', 'i']))
        exp_err_msg = 'The "user_input" argument contained a ' + \
                      'list that contained 5 characters instead of 6'
        self.run_test_fail(test_input, ValueError, exp_err_msg)


class Passwords_Unit_Tests_Special(Passwords_Unit_Tests):

    def test_special_01(self):
        '''
        Special 1 - Parameter contains non-alphabet input from user (number)
        '''
        test_input = tuple((['p', 'c', 'n', 'r', 'o', 'x'],
                            ['i', 'f', 'j', 't', 'u', 'p'],
                            ['p', 'w', 'k', 'h', 'q', 'r'],
                            ['i', 'w', '3', 'h', 'm', 'o'],
                            ['p', 'r', 'x', 'b', 'i', 'e']))
        exp_err_msg = 'The "user_input" argument contains ' + \
                      'an entry with a non-alphabet character: ' + \
                      "['i', 'w', '3', 'h', 'm', 'o']"
        self.run_test_fail(test_input, ValueError, exp_err_msg)

    def test_special_02(self):
        '''
        Special 2 - Parameter contains non-alphabet input from user
            (symbol)
        '''
        test_input = tuple((['p', 'c', 'n', 'r', 'o', 'x'],
                            ['i', 'f', 'j', 't', 'u', 'p'],
                            ['p', 'w', 'k', 'h', 'q', 'r'],
                            ['i', 'w', '#', 'h', 'm', 'o'],
                            ['p', 'r', 'x', 'b', 'i', 'e']))
        exp_err_msg = 'The "user_input" argument contains ' + \
                      'an entry with a non-alphabet character: ' + \
                      "['i', 'w', '#', 'h', 'm', 'o']"
        self.run_test_fail(test_input, ValueError, exp_err_msg)

    def test_special_03(self):
        '''
        Special 1 - Standard, valid, normalized input from actual gameplay...
            but the CAPS LOCK IS ON
        Note:
            CaSe ShOuLdN't MaTtEr WhEn DiFfUsInG a BoMb!
            The user input function from nill_passwords.py should be
                handling this already but (SPOILER ALERT), input could be
                coming from somewhere else.
        '''
        test_input = self.prepare_test_input(
            ['PCNROX', 'IFJTUP', 'PWKHQR', 'IWEHMO', 'PRXBIE'])
        self.run_test_pass('other', test_input)

    def test_special_04(self):
        '''
        Special 4 - Standard, valid, normalized input from actual gameplay
            that also includes unused characters: j, q, x.
        '''
        test_input = self.prepare_test_input(
            ['jqxpcnro', 'jqxiftup', 'jqxpwkhr', 'jqxiwehmo', 'jqxprbie'])
        self.run_test_pass('other', test_input)


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
