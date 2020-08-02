from . nill_passwords import find_password

if __name__ == '__main__':
    try:
        find_password()
    except Exception as err:
        print(f'\nERROR: {err.args[0]}\n')
