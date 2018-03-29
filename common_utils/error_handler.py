from rest_framework.exceptions import (
    APIException,
    ParseError
)
from contentfulData.constants import FailureMessages, ExceptionHandlerKeys
import sys
import traceback


class CondenastException(Exception):

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        Exception.__init__(self, args, kwargs)


class ErrorHandler:

    def __init__(self):
        pass

    @staticmethod
    def handle_exception(exception):
        # For tracking exception in console -- Replace with loggers
        traceback.print_exc(file=sys.stdout)

        with open('error_log.txt', 'a') as file:
            file.write('\n-----\n\n')
            file.write(str(exception)+'\n\n')
            file.write(traceback.format_exc())
            file.write('\n-----')

        if isinstance(exception, CondenastException):
            status_code = exception.kwargs.get(ExceptionHandlerKeys.STATUS_CODE.value)
            raise HttpCustomError(
                ErrorResponse.get_response_obj(
                    ErrorResponse.VALIDATION_ERROR,
                    message=exception.kwargs.get(ExceptionHandlerKeys.MESSAGE.value),
                    data=exception.kwargs.get(ExceptionHandlerKeys.DATA.value)
                ),
                status_code
            )
        elif isinstance(exception, ValueError):
            raise HttpCustomError(
                ErrorResponse.get_response_obj(
                    ErrorResponse.VALIDATION_ERROR,
                    FailureMessages.VALIDATION_ERROR.value),

            )
        elif isinstance(exception, ParseError):
            raise HttpCustomError(
                ErrorResponse.get_response_obj(
                    ErrorResponse.PARSE_ERROR,
                    FailureMessages.INVALID_JSON_REQUEST.value),

            )
        else:
            print(exception)
            raise HttpCustomError(
            )


class ErrorResponse(object):
    API_ERROR = 'api_error'
    AUTHENTICATION_ERROR = 'authentication_error'
    INVALID_REQUEST_ERROR = 'invalid_request_error'
    RATE_LIMIT_ERROR = 'rate_limit_error'
    VALIDATION_ERROR = 'validation_error'
    SERIALIZER_ERRORS = 'serializer_error'
    PARSE_ERROR = 'parse_error'

    @staticmethod
    def get_response_obj(error_type=None, message=None, data=None, param=None):
        if param:
            return {
                'type': error_type,
                'errorMessage': message,
                'param': param
            }
        elif data:
            return {
                'type': error_type,
                'errorMessage': message,
                'errors': data
            }
        else:
            return {
                'type': error_type,
                'errorMessage': message
            }


class HttpCustomError(APIException):
    API_ERROR = 'api_error'
    AUTHENTICATION_ERROR = 'authentication_error'
    INVALID_REQUEST_ERROR = 'invalid_request_error'
    RATE_LIMIT_ERROR = 'rate_limit_error'
    VALIDATION_ERROR = 'validation_error'

    default_detail = {
        'type': API_ERROR,
        'message': 'Oops! Something went wrong!',
        'param': None}
    default_code = 'bu_uahaha'

    def __init__(self, detail=None, status_code=None, code=None):
        if status_code:
            self.status_code = status_code
        else:
            self.status_code = 400
        if detail:
            self.default_detail = detail
        if code:
            self.default_code = code
        super(HttpCustomError, self).__init__()
