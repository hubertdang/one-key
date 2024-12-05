from one_key.Credential import Credential


class User:
    """
    A class to represent a user of the password manager.

    Attributes:
        __username: The username of the user.
        __key: The key to the user's credentials.
        __signed_in: True if the user is signed in, false otherwise.
        __credentials: Collection of the user's credentials.

    """

    def __init__(self, username: str, key: str):
        """
        Initializes a new User instance.

        Args:
            username: The username of the user.
            key: The key to the user's credentials.

        Raises:
            ValueError: If the username or key is invalid.

        """
        if username is None or username.strip() == '':
            raise ValueError('Invalid username.')
        if key is None or key.strip() == '':
            raise ValueError('Invalid key.')
        self.__username = username
        self.__key = key
        self.__signed_in = False
        self.__credentials = {}

    def __eq__(self, other):
        """
        Checks if two User objects are equal.

        Args:
            other: The other User object.

        Returns:
            bool: True if they are equal, False otherwise.

        """
        if not isinstance(other, User):
            return False
        # directly reference fields because of sign-in mechanism
        if other._User__username != self.__username:
            return False
        if other._User__key != self.__key:
            return False
        if other._User__signed_in != self.__signed_in:
            return False
        if other._User__credentials != self.__credentials:
            return False
        return True

    def sign_in(self, key: str):
        """
        Signs the user in. 

        Args:
            key: The key to the user's credentials.

        Returns:
            bool: True if the user successfully signed in, False otherwise.

        """
        if key != self.__key:
            return False
        self.__signed_in = True
        return True

    def sign_out(self):
        """
        Signs the user out.

        Returns:
            bool: True if the user successfully signed out, False otherwise. 

        """
        if not self.is_signed_in():
            return False
        self.__signed_in = False
        return True

    def is_signed_in(self):
        """
        Checks if the user is signed in.

        Returns:
            bool: True if the user is signed in, False otherwise.

        """
        return self.__signed_in

    def get_key(self):
        """
        Gets the user's key if they are signed in.

        Returns:
            str: The user's key if they are signed in, None otherwise.

        """
        if not self.is_signed_in():
            return None
        return self.__key

    def set_key(self, key: str):
        """
        Sets the user's key if they are signed in.

        Args:
            key: The user's new key.

        Returns:
            bool: True if the new key was set successfully, False otherwise.

        """
        if not self.is_signed_in():
            return False
        if key is None or key.strip() == '':
            return False
        self.__key = key
        return True

    def get_username(self):
        """
        Gets the user's username.

        Returns:
            str: The user's username.

        """
        return self.__username

    def set_username(self, username: str):
        """
        Sets the user's username.

        Args:
            username: The user's new username.

        Returns:
            bool: True if the new username was set succesfully, False otherwise.

        """
        if not self.is_signed_in():
            return False
        if username is None or username.strip() == '':
            return False
        self.__username = username
        return True

    def get_credential(self, website: str):
        """
        Get a credential for a website from the user's collection of credentials.

        Args:
            website: The website to get the credential for.

        Returns:
            Credential: the credential if it exists and the user is signed in, None otherwise. 

        """
        if not self.is_signed_in():
            return None
        if website not in self.__credentials:
            return None
        return self.__credentials[website]

    def add_credential(self, credential: Credential):
        """
        Add a credential to the user's collection of credentials.

        Args:
            credential: The user's new credential to be added.

        Returns:
            bool: True if the credential was added successfully, False otherwise.

        """
        website = credential.get_website()

        if not self.is_signed_in():
            return False
        if website in self.__credentials:
            return False
        self.__credentials[website] = credential
        return True

    def remove_credential(self, website: str):
        """
        Remove a credential from the user's collection of credentials.

        Args:
            website: The website of the credential to be removed.

        Returns:
            bool: True if the credential was removed successfully, False otherwise.

        """
        if not self.is_signed_in():
            return False
        if website not in self.__credentials:
            return False
        del self.__credentials[website]
        return True

    def list_credentials(self):
        """List the user's credentials.

        Returns:
            str: The list of the user's credentials as a string.
        """
        if not self.is_signed_in():
            return False
        headers = ["Website", "Username", "Password"]
        rows = [headers] + [[cred.get_website(), cred.get_username(), cred.get_password()]
                            for cred in self.__credentials.values()]
        column_widths = [max(len(str(item)) for item in col)
                         for col in zip(*rows)]
        total_width = sum(column_widths) + (len(column_widths) - 1) * 2
        border_line = '=' * total_width + '\n'

        cred_list = ''
        cred_list += "  ".join(f"{header.ljust(width)}" for header,
                               width in zip(headers, column_widths)) + '\n'
        cred_list += border_line
        for row in rows[1:]:
            cred_list += "  ".join(f"{str(item).ljust(width)}" for item,
                                   width in zip(row, column_widths)) + '\n'

        return cred_list
