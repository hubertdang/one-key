class Credential:
    """
    A class to represent a login credential.

    Attributes:
        website: The website the credential is used for.
        username: The username of the credential.
        password: The password of the credential.

    """

    def __init__(self, website: str, username: str, password: str):
        """
        Initializes a new Credential instance.

        Args:
            website: The website the credential is used for.
            username: The username of the credential.
            password: The password of the credential.

        """
        self.__website = website
        self.__username = username
        self.__password = password

    def get_website(self):
        """
        Gets the website the credential is used for.

        Returns:
            str: The website the credential is used for.

        """
        return self.__website

    def set_website(self, website: str):
        """
        Sets the website the credential is used for.

        Args:
            website: The website the credential is used for.

        """
        self.__website = website

    def get_username(self):
        """
        Gets the username of the credential.

        Returns:
            str: The username of the credential.

        """
        return self.__username

    def set_username(self, username: str):
        """
        Sets the username of the credential.

        Args:
            username: The username to set the credential with.

        """
        self.__username = username

    def get_password(self):
        """
        Gets the password of the credential.

        Returns:
            str: The password of the credential.

        """
        return self.__password

    def set_password(self, password: str):
        """
        Sets the password of the credential.

        Args:
            password: The password to set the credential with.

        """
        self.__password = password

    def __str__(self):
        """
        Returns the string representation of the credential.

        Returns:
            str: The string representation of the credential.

        """
        return f'Website: {self.__website}; Username: {self.__username}; Password: {self.__password}'

