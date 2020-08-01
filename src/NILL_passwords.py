'''
    File: NILL_passwords.py
    Description: Programmatic solutions for the "Keep Talking and Nobody
        Explodes" (KTaNE) "passwords".
    Usage:  Call find_password() (but unit test _find_password())
    Details:
        Site: www.keeptalkinggame.com
        Version: 1
        Verification Code: 241
        Page: 16 of 23
'''

from typing import Tuple

LIST_OF_PWDS = [
        'about', 'after', 'again', 'below', 'could', 'every',
        'first', 'found', 'great', 'house', 'large', 'learn',
        'never', 'other', 'place', 'plant', 'point', 'right',
        'small', 'sound', 'spell', 'still', 'study', 'their',
        'there', 'these', 'thing', 'think', 'three', 'water',
        'where', 'which', 'world', 'would', 'write'
    ]


def find_password():
    # LOCAL VARIABLES
    user_input = _input_pwds()          # Manual user input from KTaNE
    match = _find_password(user_input)  # Matched password based on user input
    # DONE
    print(match)


def _input_pwds():
    '''
    Purpose: Take manual user input on characters for each password position
    Notes:
        Will filter out non-alphabet characters (as typos)
        Will include input that exceeds expected length (git gud at typing)
        Length of each list, contained in the tuple, is not validated
    Returns: A tuple (length 5) of lists.  Each list contains a lower-case
        string of alphabet characters input by the user.
    '''
    pos1 = [char.lower() for char in input('Position 1: ') if char.isalpha()]
    pos2 = [char.lower() for char in input('Position 2: ') if char.isalpha()]
    pos3 = [char.lower() for char in input('Position 3: ') if char.isalpha()]
    pos4 = [char.lower() for char in input('Position 4: ') if char.isalpha()]
    pos5 = [char.lower() for char in input('Position 5: ') if char.isalpha()]
    return tuple((pos1, pos2, pos3, pos4, pos5))


def _validate_user_input(user_input: Tuple):
    # LOCAL VARIABLES
    min_chars = 6  # Minimum characters per password position

    # INPUT VALIDATION
    if not isinstance(user_input, Tuple):
        raise TypeError('The "user_input" argument is of type '
                        f'{type(user_input)} instead of a tuple')
    elif 5 != len(user_input):
        raise ValueError('The "user_input" argument is holds '
                         f'{len(user_input)} positions instead of 5')
    else:
        for entry in user_input:
            if not isinstance(entry, list):
                raise TypeError('The "user_input" argument contains a '
                                f'non-list of type {type(entry)}')
            elif len(entry) < 6:
                raise ValueError('The "user_input" argument contained a '
                                 f'list that contained {len(entry)} '
                                 f'characters instead of {min_chars}')
            else:
                for char in entry:
                    if not char.isalpha():
                        raise ValueError('The "user_input" argument contains '
                                         'an entry with a non-alphabet '
                                         f'character: {entry}')


def _find_password(user_input: Tuple):
    '''
    Purpose: Compare input to the password list to find a single match
    Parameters:
        user_input - A tuple with five string-based entries containing
            per-position input.
    Notes:
        Input validation is handled by _validate_user_input()
    Exceptions:
        RuntimeError if a single match wasn't found
        see: _validate_user_input()
    Returns: A string containing the single password.
    '''
    # LOCAL VARIABLES
    password = ''            # Discrete password from the manual
    currList = LIST_OF_PWDS  # Shortened "starting point" list

    # INPUT VALIDATION
    _validate_user_input(user_input)

    # FIND IT
    currList = [word for word in currList if word[2] in user_input[2]]
    print(currList)  # DEBUGGING
    currList = [word for word in currList if word[4] in user_input[4]]
    print(currList)  # DEBUGGING
    currList = [word for word in currList if word[0] in user_input[0]]
    print(currList)  # DEBUGGING
    currList = [word for word in currList if word[1] in user_input[1]]
    print(currList)  # DEBUGGING
    currList = [word for word in currList if word[3] in user_input[3]]
    print(currList)  # DEBUGGING

    # DONE
    if 1 == len(currList):
        password = currList[0]
    elif len(currList) > 1:
        raise RuntimeError(f'Too many password matches: {currList}')
    else:
        raise RuntimeError('Password not found')

    return password


if __name__ == '__main__':
    try:
        find_password()
    except Exception as err:
        print(f'\nERROR: {err.args[0]}\n')
