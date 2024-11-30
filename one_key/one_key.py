from one_key.User import User
from one_key.Credential import Credential
from one_key.PasswordManager import PasswordManager

import argparse

MIN_USERS = 0  # min num users required to run commands other than --add-user


def add_options(parser, pm: PasswordManager):
    """Dynamically add options to the program based on certain conditions.

    Args:
        parser (ArgumentParser): The argument parser used for this program.
        pm (PasswordManager): The password manager.
    """
    options = parser.add_mutually_exclusive_group()

    # options that are always provided start here
    options.add_argument('--add-user', action='store_true',
                         help='add a user to the password manager')

    # options that are conditional start here
    if pm.get_num_users() > MIN_USERS:
        if pm.anyone_signed_in():
            options.add_argument('--delete-acc', action='store_true',
                                 help='deletes your account and its credentials')
            options.add_argument('--sign-out', action='store_true',
                                 help='sign yourself out')
            options.add_argument('--reset-key', action='store_true',
                                 help='reset your key')
            options.add_argument('--reset-username',
                                 action='store_true', help='reset your username')
        else:
            options.add_argument(
                '--sign-in', action='store_true', help='sign yourself in')


def main():
    pm = PasswordManager()

    parser = argparse.ArgumentParser()
    add_options(parser, pm)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
