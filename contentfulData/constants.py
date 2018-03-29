from enum import Enum


class FailureMessages(Enum):
    EMAIL_ALREADY_EXISTS = 'The Email is already registered to an account in Dolby. Please try again'
    PHONE_NUMBER_ALREADY_EXISTS = 'Phone number is already registered to an account in Debx'
    FIELD_MISSING = 'Email, password or name missing'
    INCORRECT_PASSWORD = 'Incorrect password'
    INCOMPLETE_DATA = 'Incomplete data'
    INACTIVE_USER = 'User Inactive'
    EMAIL_OR_PASSWORD_EMPTY = 'Email or password cannot be empty'
    USER_INACTIVE = 'This user is not active'
    USER_DOES_NOT_EXIST_OR_INACTIVE = 'User does not exist or is not active'
    USER_ASSOCIATED_WITH_THIS_EMAIL_DOESNT_EXIST = 'The user with this email does not exist'
    USER_DOES_NOT_EXIST = 'User does not exist'
    INVALID_FACEBOOK_CREDENTIALS = 'Invalid facebook credentials'
    INVALID_INPUT = 'Please enter valid Credentials'
    INVALID_CHANGE_PASSWORD_REQUEST = 'Require both old and new password.'
    USER_NOT_VERIFIED = 'Please verify the user before sign-in'
    INVALID_LOGIN = 'Invalid Login'
    INVALID_SIGNUP_SIGNIN = 'Invalid Sign-up/Sign-in'
    ENTER_PASSWORD_TO_VERIFY = 'Please enter password to be verified.'
    UPDATED_LOGIN_TO_VERIFY = "Your account has been updated. Please verify the email and login again to continue."
    SELECT_MOVIE_TO_ADD = "Please select a movie to add to watchlist"
    SOMETHING_IS_WRONG_TRY_AGAIN = "Sorry!! Something went wrong. Try again!"
    INVALID_LOGIN = 'Invalid Login'
    INVALID_SIGNUP_SIGNIN = 'Invalid Sign-up/Sign-in'
    PAYMENT_NONCE_REQUIRED = "Please provide valid payment nonce"
    INVALID_REQUEST = "Invalid request"
    SES_SANDBOX_FAILURE = "SES Sand-box Failure"
    SELECT_MOVIE_TO_DELETE = "Please select a movie to delete from watchlist"

    # Generic error messages
    SERIALIZER_ERRORS = 'Serializer validation failed'
    INVALID_JSON_REQUEST = 'Invalid JSON request'

    # Views Error messages
    LINK_EXPIRED = 'Link has been expired'
    INVALID_OR_CORRUPT_MAILTOKEN = 'Invalid or corrupt Mailtoken'
    PASSWORDS_DO_NOT_MATCH = 'Passwords do not match'
    INVALID_PASSWORD = 'Password length should be between 8-32 characters and can ' \
                       'only contain alpha-numeric or the following characters: ~`!@#$%^&,.'

    # Errors during creating a profile
    NAME_REGEX_ERROR = "Only letters and spaces are allowed in 'Name' field"
    PASSWORD_REGEX_ERROR = 'Password must contain at-least one alphabet,' \
                           'one number and one special character(and of minimum 8 characters)'
    VALIDATION_ERROR = 'Validation Error'


    # Errors during verifying a profile
    VERIFICATION_ERROR_MESSAGE = 'Oops something went wrong !!!'


class ExceptionHandlerKeys(Enum):
    DATA = 'data'
    MESSAGE = 'message'
    STATUS_CODE = 'status_code'


class SuccesMessages(Enum):
    UPDATE_SUCCESSFUL = 'Update successful'
    PLACE_ADDED_SUCCESSFULLY = 'Place added successfully'
    TIP_ADDED_SUCCESSFULLY = 'Tip added successfully'
    CONTRIBUTOR_ADDED_SUCCESSFULLY = 'Contributor added successfully'
    PLACE_DELETED_SUCCESSFULLY = 'Place deleted successfully'
    FEED_DELETED_SUCCESSFULLY = 'Feed deleted successfully'
    WELCOME_MESSAGE = 'Condenast application is running'
    CONTRIBUTOR_DELETED = 'Contributor deleted successfully'
    DELETED_SUCCESSFULLY = 'Noteworthy data deleted successfully'
