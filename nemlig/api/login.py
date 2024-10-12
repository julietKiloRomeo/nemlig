from nemlig.api import webapi

def login(username: str, password: str) -> dict:
    """
    Logs in a user with the provided username and password.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        dict: A dictionary containing the response from the login API.

    Examples:
        >>> login('john_doe', 'password123')
        {'status': 'success', 'user_id': 12345}
        >>> login('jane_smith', 'pass123')
        {'status': 'success', 'user_id': 67890}
    """
    return webapi.post('/login/login', json={
        'Username': username,
        'Password': password,
        'AppInstalled': False,
        'AutoLogin': False,
        'CheckForExistingProducts': True,
        'DoMerge': True,
    })
