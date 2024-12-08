from one_key.User import User
from one_key.Credential import Credential

import pickle
import os
from importlib.resources import files


class PasswordManager:
    """
    A class to represent a password manager.

    Attributes:
        __users: The dictionary of users.
        __curr_user: The currently signed in user.

    """
    DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
    PM_SAVE_FILE = 'password_manager.pkl'
    PM_SAVE_FILE_PATH = os.path.join(DATA_DIR, PM_SAVE_FILE)

    def __init__(self):
        """
        Initializes a new PasswordManager instance.

        """
        self.__data_file = self.PM_SAVE_FILE_PATH
        self.__users = {}
        self.__curr_user = None
        self.load_data()

    def add_user(self, user: User):
        """
        Adds a user to the password manager.

        Args:
            user: The user to add to the password manager.

        Returns:
           bool: True if the user was successfully added, False otherwise. 

        """
        username = user.get_username()
        if self.__get_user(username) is not None:
            return False
        self.__users[username] = user
        return True

    def remove_user(self, username: str):
        """
        Removes a user from the password manager.

        Args:
            username: The username of the user to remove.

        Returns:
            bool: True if the user was successfully removed, False otherwise. 

        """
        if not self.is_signed_in(username):
            return False
        self.sign_out(username)
        del self.__users[username]
        return True

    def get_num_users(self):
        """
        Gets the password manager's number of users.

        Returns:
            int: The number of users.
        """
        return len(self.__users)

    def user_exists(self, username: str):
        """
        Checks if a username belongs to a valid user.

        Args:
            username: The username of the user to check.

        Returns:
            bool: True if the username belongs to a valid user, False otherwise. 

        """
        if self.__get_user(username) is None:
            return False
        return True

    def __get_user(self, username: str):
        """
        Gets a user from the password manager's users dictionary.

        Args:
            username: The username of the user to get.

        Returns:
            User: The user whose username matches the parameter 'username'. None if the user
            does not exist.

        """
        return self.__users.get(username)

    def __get_curr_user(self):
        """
        Gets the currently signed in user.

        Returns:
            User: The currently signed in user.
        """
        return self.__curr_user

    def __set_curr_user(self, user: User):
        """
        Sets the currently signed in user.

        """
        self.__curr_user = user

    def get_curr_user_username(self):
        """Get the currently signed in user's username.

        Returns:
            str: The currently signed in user's username.
        """
        return self.__get_curr_user().get_username()

    def anyone_signed_in(self):
        """
        Checks if anyone is signed in.

        Returns:
            bool: True if someone is signed in, False otherwise.
        """
        if self.__get_curr_user() is None:
            return False
        return True

    def sign_in(self, username: str, key: str):
        """
        Signs in a user of the password manager.

        Args:
            username: The user's username.
            key: The user's key.

        Returns:
            bool: True if the user was successfully signed in, False otherwise.

        """
        if not self.user_exists(username):
            return False
        if self.anyone_signed_in():
            return False
        user = self.__get_user(username)
        if not user.sign_in(key):
            return False
        self.__set_curr_user(user)
        return True

    def sign_out(self, username: str):
        """
        Signs out a user of the password manager.

        Args:
            username: The user's username.

        Returns:
            bool: True if the user was successfully signed out, False otherwise. 

        """
        if not self.is_signed_in(username):
            return False
        self.__set_curr_user(None)
        return self.__get_user(username).sign_out()

    def is_signed_in(self, username: str):
        """Checks if a user is signed in.

        Args:
            username (str): The user's username.
        """
        if not self.user_exists(username):
            return False
        if self.__get_curr_user() is not self.__get_user(username):
            return False
        return True

    def get_key(self, username: str):
        """
        Gets a user's key.

        Args:
            username: The user's username.

        Returns:
            str: The user's key if they are signed in, None otherwise. 

        """
        if not self.is_signed_in(username):
            return None
        return self.__get_user(username).get_key()

    def set_key(self, username: str, key: str):
        """
        Sets a user's key.

        Args:
            username: The user's username.
            key: The user's new key.

        Returns:
            bool: True if the user's new key was set successfully, False otherwise. 

        """
        if not self.is_signed_in(username):
            return False
        return self.__get_user(username).set_key(key)

    def set_username(self, old_username: str, new_username: str):
        """
        Set's a user's username.

        Args:
            old_username: The user's old username.
            new_username: The user's new username.

        Returns:
            bool: True if the user's new username was successfully set, False otherwise. 

        """
        if not self.is_signed_in(old_username):
            return False
        result = self.__get_user(old_username).set_username(new_username)
        if result:
            # the username-user key-value pair is still using the old username, so update it
            self.__users[new_username] = self.__users.pop(old_username)
        return result

    def get_credential(self, username: str, website: str):
        """
        Get's a user's credential for a website.

        Args:
            username: The user's username.
            website: The website of the credential to get.

        Returns:
            Credential: The user's credential for the given website. None if a credential for the
            given website doesn't exist.
        """
        if not self.is_signed_in(username):
            return False
        return self.__get_user(username).get_credential(website)

    def add_credential(self, username: str, credential: Credential):
        """
        Adds a credential to the user's dictionary of credentials.

        Args:
            username: The user's username.
            credential: The credential to add.

        Returns:
            bool: True if the credential was added successfully, False otherwise.
        """
        if not self.is_signed_in(username):
            return False
        return self.__get_user(username).add_credential(credential)

    def remove_credential(self, username: str, website: str):
        """
        Removes a credential from the user's dictionary of credentials.

        Args:
            username: The user's username.
            website: The website of the credential to remove.

        Returns:
            bool: True if the credential was removed successfully, False otherwise.
        """
        if not self.is_signed_in(username):
            return False
        return self.__get_user(username).remove_credential(website)

    def list_credentials(self, username: str):
        """Lists a user's credentials.

        Args:
            username (str): The user's username.

        Returns:
            str: A list of the user's credentials as a string.
        """
        if not self.is_signed_in(username):
            return False
        return self.__get_user(username).list_credentials()

    def save_data(self):
        """Serializes and saves the password manager state.
        """
        data = {'users': self.__users, 'curr_user': self.__curr_user}
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
        with open(self.__data_file, 'wb+') as f:
            pickle.dump(data, f)

    def load_data(self):
        """Deserializes and loads the password manager state from data/password_manager.pkl
        """
        if not os.path.exists(self.__data_file):
            return
        with open(self.__data_file, 'rb') as f:
            data = pickle.load(f)
            self.__users = data.get('users')
            self.__curr_user = data.get('curr_user')
