class Credentials:
    """
    A class to represent a set of credentials.

    Attributes:
        website: The website the credentials are used for.
        username: The username of the credentials.
        password: The password of the credentials.

    """

    def __init__(self, username: str, password: str):
        """
        Initializes a new Credentials instance.

        Args:
            website: The website the credentials are used for.
            username: The username of the credentials.
            password: The password of the credentials.

        """
        self._website = website
        self._username = username
        self._password = password

    def get_website(self):
        """
        Gets the website the credentials are used for.

        Returns:
            str: The website the credentials are used for.

        """
        return self._website

    def set_website(self, website: str):
        """
        Sets the website the credentials are used for.

        Args:
            website: The website the credentials are used for.

        """
        self._website = website

    def get_username(self):
        """
        Gets the username of the credentials.

        Returns:
            str: The username of the credentials.

        """
        return self._username

    def set_username(self, username: str):
        """
        Sets the username of the credentials.

        Args:
            username: The username to set the credentials with.

        """
        self._username = username

    def get_password(self):
        """
        Gets the password of the credentials.

        Returns:
            str: The password of the credentials.

        """
        return self._password

    def set_password(self, password: str):
        """
        Sets the password of the credentials.

        Args:
            password: The password to set the credentials with.

        """
        self._password = password

    def __str__(self):
        """
        Returns the string representation of the credentials.

        Returns:
            str: The string representation of the credentials.

        """
        return f"Website: {self._website}; Username: {self._username}; Password: {self._password}"

