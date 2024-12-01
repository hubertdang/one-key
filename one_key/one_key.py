from one_key.User import User
from one_key.Credential import Credential
from one_key.PasswordManager import PasswordManager

import argparse

MIN_USERS = 0  # min num users required to run commands other than --add-user


def main():
    parser = argparse.ArgumentParser()
    options = parser.add_mutually_exclusive_group()

    options.add_argument('--add-user', action='store_true',
                         help='add a user to the password manager')
    options.add_argument('--sign-in', action='store_true',
                         help='sign yourself in')
    options.add_argument('--delete-acc', action='store_true',
                         help='deletes your account and its credentials')
    options.add_argument('--sign-out', action='store_true',
                         help='sign yourself out')
    options.add_argument('--reset-key', action='store_true',
                         help='reset your key')
    options.add_argument('--reset-username',
                         action='store_true', help='reset your username')

    args = parser.parse_args()

    pm = PasswordManager()


if __name__ == '__main__':
    main()
