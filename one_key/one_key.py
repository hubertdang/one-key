from one_key.User import User
from one_key.Credential import Credential
from one_key.PasswordManager import PasswordManager

import os
import argparse
import getpass

MIN_USERS = 0  # min num users required to run commands other than --add-user
USER = os.environ.get('USER')


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
            print("Please enter 'y' or 'n'.")


def prompt_password(msg: str):
    """Prompts the user for a password.

    Args:
        msg (str): The prompt message.

    Returns:
        str: The password entered by the user
    """
    return getpass.getpass(f'{msg}')


def main():
    """Main entry point of the one_key application.
    """
    parser = argparse.ArgumentParser()
    options = parser.add_mutually_exclusive_group()

    options.add_argument('--sign-in', action='store_true',
                         help='sign yourself in')
    options.add_argument('--delete-acc', action='store_true',
                         help='delete your user account and your credentials')
    options.add_argument('--sign-out', action='store_true',
                         help='sign yourself out')
    options.add_argument('--reset-key', action='store_true',
                         help='reset your key')
    options.add_argument('--reset-username',
                         action='store_true', help='reset your username')
    # TODO: add options for credential management

    pm = PasswordManager()

    if not pm.is_valid_user(USER):
        print()
        create_acc = prompt_y_n(
            'You do not have an account yet, would you like to create one?')
        print()
        if not create_acc:
            return # ok to do because nothing to save yet
        print(f'Creating an account under username: {USER}')
        print()
        while True:
            u_key = prompt_password(
                'Please enter a key to use to access your account: ')
            u_key_confirm = prompt_password(
                'Please re-enter the key to confirm: ')
            if u_key_confirm == u_key:
                break
            print()
            print('Sorry, the keys you entered do not match.')
            print()
        u = User(USER, u_key)
        if not pm.add_user(u):
            return # ok to do because nothing to save yet
        print()
        print(f'Successfully added {USER} as a user!')
        print()
        parser.print_help()

    # work for the argument/option provided starts here:
    args = parser.parse_args()
    if not any(vars(args).values()):
        print()
        print("No options passed, nothing to do!")
        print()
        parser.print_help()

    if args.sign_in:
        print()
        input_key = prompt_password('Please enter your key: ')
        success = pm.sign_in(USER, input_key)
        if not success:
            print('Failed to sign in.')
        else:
            print('Successfully signed in.')

    if args.delete_acc:
        print()
        success = pm.remove_user(USER)
        if not success:
            print('Failed to delete your acount.')
        else:
            print('Successfully deleted your account.')

    pm.save_data()


if __name__ == '__main__':
    main()
