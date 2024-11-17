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
        self._website = website
        self._username = username
        self._password = password

    def get_website(self):
        """
        Gets the website the credential is used for.

        Returns:
            str: The website the credential is used for.

        """
        return self._website

    def set_website(self, website: str):
        """
        Sets the website the credential is used for.

        Args:
            website: The website the credential is used for.

        """
        self._website = website

    def get_username(self):
        """
        Gets the username of the credential.

        Returns:
            str: The username of the credential.

        """
        return self._username

    def set_username(self, username: str):
        """
        Sets the username of the credential.

        Args:
            username: The username to set the credential with.

        """
        self._username = username

    def get_password(self):
        """
        Gets the password of the credential.

        Returns:
            str: The password of the credential.

        """
        return self._password

    def set_password(self, password: str):
        """
        Sets the password of the credential.

        Args:
            password: The password to set the credential with.

        """
        self._password = password

    def __str__(self):
        """
        Returns the string representation of the credential.

        Returns:
            str: The string representation of the credential.

        """
        return f'Website: {self._website}; Username: {self._username}; Password: {self._password}'

