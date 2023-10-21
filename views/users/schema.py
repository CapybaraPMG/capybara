class APIError(Exception):
    """All custom API Exceptions"""

    pass


class UserNotFoundError(APIError):
    """User Not Found Error Class."""

    status_code: str = str(403)
    message: str = "Username field is required"


class EmailNotFoundError(APIError):
    """Email Not Found Error Class."""

    status_code: str = str(403)
    message: str = "Email field is required"


class PictureNotFoundError(APIError):
    """Picture Not Found Error Class."""

    status_code: str = str(403)
    message: str = "Picture field is required"
