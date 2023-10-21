class BaseAPIError:
    """Base class for custom API Exceptions."""

    status_code: int
    message: str

    def to_dict(self):
        return {"status_code": self.status_code, "message": self.message}


class UserNotFoundError(BaseAPIError):
    """User Not Found Error Class."""

    status_code = 400
    message = "Username field is required"


class EmailNotFoundError(BaseAPIError):
    """Email Not Found Error Class."""

    status_code = 400
    message = "Email field is required"


class PictureNotFoundError(BaseAPIError):
    """Picture Not Found Error Class."""

    status_code = 400
    message = "Picture field is required"


class SaveUserSuccessfull(BaseAPIError):
    """User saved successfully"""

    status_code = 201
    message = "User saved successfully"


class APIError(BaseAPIError):
    """User saved successfully"""

    status_code = 500
    message = "An error occured while processing your request, please try again later"
