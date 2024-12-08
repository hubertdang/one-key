from one_key.User import User
from one_key.Credential import Credential
from one_key.PasswordManager import PasswordManager

import os
import argparse
import getpass
from colorama import Fore, Style

MIN_USERS = 0  # min num users required to run commands other than --add-user
USER = os.environ.get('USER')


def bad_str(in_str: str):
    """Checks if a string (for a website, username, or password) is an unacceptable string.
    An unacceptable string is empty or contains spaces.

    Args:
        in_str (str): The string to check.

    Returns:
        bool: True if the string is unacceptable, False otherwise.
    """
    if not in_str or in_str == '':
        return True
    return False


def prompt_y_n(msg: str):
    """Prompts a yes or no message.

    Args:
        msg (str): The prompt message.

    Returns:
        bool: True if the user replied yes, False otherwise.
    """
    while True:
        response = input(f'{msg} (y/n): ').strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print('Please enter \'y\' or \'n\'.')


def prompt_password(msg: str):
    """Prompts the user for a password. The password must not be blank and cannot contain spaces.

    Args:
        msg (str): The prompt message.

    Returns:
        str: The password entered by the user
    """
    while True:
        password = getpass.getpass(f'{msg}')
        if bad_str(password):
            print('Your password must not be blank and cannot contain spaces.')
            continue
        break
    return password


def prompt_str(msg: str):
    """Prompts the user for a string that doesn't need to be hidden.

    Args:
        msg (str): The prompt message.

    Returns:
        str: The user's response.
    """
    while True:
        resp = input(msg)
        if bad_str(resp):
            print('Blank strings and spaces are not permitted.')
            continue
        break
    return resp


def print_success(msg: str):
    """Prints a success message.

    Args:
        msg (str): The success message.
    """
    print('[' + Fore.GREEN + 'SUCCESS' + Style.RESET_ALL + '] ' + msg)


def print_failure(msg: str):
    """Prints a failure message.

    Args:
        msg (str): The failure message.
    """
    print('[' + Fore.RED + 'FAILURE' + Style.RESET_ALL + '] ' + msg)


def print_warning(msg: str):
    """Prints a warning message

    Args:
        msg (str): The warning message.
    """
    print('[' + Fore.YELLOW + 'WARNING' + Style.RESET_ALL + '] ' + msg)


def main():
    """Main entry point of the one_key application.
    """
    parser = argparse.ArgumentParser()
    options = parser.add_mutually_exclusive_group()

    options.add_argument('-acc', '--add-acc', action='store_true',
                         help='add an account for yourself')
    options.add_argument('-si', '--sign-in', action='store_true',
                         help='sign yourself in')
    options.add_argument('-d', '--del-acc', action='store_true',
                         help='delete your user account and your credentials')
    options.add_argument('-so', '--sign-out', action='store_true',
                         help='sign yourself out')
    options.add_argument('-k', '--reset-key', action='store_true',
                         help='reset your key')
    options.add_argument('-g', '--get-cred', action='store_true',
                         help='get a credential')
    options.add_argument('-a', '--add-cred', action='store_true',
                         help='add a credential')
    options.add_argument('-rm', '--rm-cred', action='store_true',
                         help='remove a credential')
    options.add_argument('-l', '--list', action='store_true',
                         help='list the current user\'s credentials')

    pm = PasswordManager()

    if not pm.user_exists(USER):
        print_warning(
            'You do not have an account yet. Create one with the -acc option')
    else:
        if not pm.anyone_signed_in():
            print_warning(
                'No one currently signed in. Sign in with the -si option')
        else:
            curr_user = pm.get_curr_user_username()
            print('Currently signed in: ' + Style.BRIGHT +
                  curr_user + Style.RESET_ALL)

    # work for the argument/option provided starts here:
    args = parser.parse_args()
    if not any(vars(args).values()):
        print_warning('No options passed, nothing to do!')
        print()
        parser.print_help()

    if args.add_acc:
        if pm.user_exists(USER):
            print_failure(
                f'An account with username \"{USER}\" already exists.')
        else:
            while True:
                u_key = prompt_password(
                    'Please enter a key to use to access your account: ')
                u_key_confirm = prompt_password(
                    'Please re-enter the key to confirm: ')
                if u_key_confirm == u_key:
                    break
                print_failure('The keys you entered do not match.')

            u = User(USER, u_key)
            success = pm.add_user(u)
            if not success:
                print_failure(f'Could not add user \"{USER}\".')
            else:
                print_success(f'Added account with username \"{USER}\".')

    if args.sign_in:
        input_key = prompt_password('Please enter your key: ')
        success = pm.sign_in(USER, input_key)
        if not success:
            print_failure(
                'Could not sign in. Make sure your key is correct and no one else is signed in.')
        else:
            print_success('Signed in.')

    if args.del_acc:
        if not pm.is_signed_in(USER):
            print_failure('You must sign in to delete your account.')
        else:
            confirmed = prompt_y_n(
                'Are you sure you want to delete your account?')
            if confirmed:
                success = pm.remove_user(USER)
                if not success:
                    print_failure(f'Could not delete your account.')
                else:
                    print_success(f'Deleted your account.')

    if args.sign_out:
        if not pm.is_signed_in(USER):
            print_failure('You are not signed in.')
        else:
            success = pm.sign_out(USER)
            if not success:
                print_failure('Could not sign out.')
            else:
                print_success(f'Signed out.')

    if args.reset_key:
        if not pm.is_signed_in(USER):
            print_failure('You must sign in to reset your key.')
        else:
            new_key = prompt_password('Please enter your new key: ')
            success = pm.set_key(USER, new_key)
            if not success:
                print_failure('Could not set a new key.')
            else:
                print_success('Reset key.')

    if args.get_cred:
        if not pm.is_signed_in(USER):
            print_failure('You must sign in to get a credential.')
        else:
            ws = prompt_str('Please enter the website of the credential: ')
            cred = pm.get_credential(USER, ws)
            if cred is None:
                print_failure(
                    f'A credential for {ws} does not exist for {USER}.')
            else:
                print_success(
                    f'Successfully got the {ws} credential for {USER}.')
                print(str(cred))

    if args.add_cred:
        if not pm.is_signed_in(USER):
            print_failure('You must sign in to add a credential.')
        else:
            ws = prompt_str('Please enter the website: ')
            uname = prompt_str('Please enter the username/email: ')
            pswd = prompt_password('Please enter the password: ')
            success = pm.add_credential(USER, Credential(ws, uname, pswd))
            if not success:
                print_failure(
                    f'Could not add the credential for {ws} for {USER}.')
            else:
                print_success(f'Added the credential for {ws} for {USER}.')

    if args.rm_cred:
        if not pm.is_signed_in(USER):
            print_failure('You must sign in to remove a credential.')
        else:
            ws = prompt_str(
                'Please enter the website of the credential to remove: ')
            success = pm.remove_credential(USER, ws)
            if not success:
                print_failure(
                    f'A credential for {ws} does not exist for {USER}.')
            else:
                print_success(f'Removed the credential for {ws} for {USER}.')

    if args.list:
        if not pm.is_signed_in(USER):
            print_failure('You must sign in to list credentials.')
        else:
            print()
            print(pm.list_credentials(USER))

    pm.save_data()


if __name__ == '__main__':
    main()
