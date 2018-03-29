from django.http import JsonResponse
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from common_utils.custom_exception import ErrorCodeException, SoapClientException
from common_utils.error_codes import error_codes_to_messages, ErrorCodes
from rest_framework.response import Response
from rest_framework import status
def handle_failure_response(exception):

    return handle_rest_soap_failure_response(exception=exception, is_rest_api=True)


def handle_soap_failure_response(exception):
    return handle_rest_soap_failure_response(exception=exception, is_rest_api=False)


def handle_rest_soap_failure_response(exception, is_rest_api):
    message = exception.message
    if isinstance(exception, ErrorCodeException):
        return failure_response_with_code(error_code=message, is_rest_api=is_rest_api)

    if isinstance(exception, ParseError):
        message = "Error while parsing JSON"

    return failure_response_with_message(error_message=message, is_rest_api=is_rest_api)


def failure_response(error_code, error_message, is_rest_api):
    response_data = {'error_message': error_message, 'error_code': error_code}
    return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST) if is_rest_api else response_data


def failure_response_with_code(error_code, is_rest_api):
    error_message = error_codes_to_messages[error_code]
    return failure_response(error_code=error_code, error_message=error_message, is_rest_api=is_rest_api)


def failure_response_with_message(error_message, is_rest_api):
    return failure_response(error_code=ErrorCodes.ERROR_IN_REQUEST_DATA, error_message=error_message,
                            is_rest_api=is_rest_api)


def get_serializer_error_message(errors):
    error_message = ''
    print (errors)
    for error_key in errors:
        error_message = errors[error_key][0]
        if 'required' in error_message:
            error_message = format_error_key(error_key) + ' is required'
        elif 'blank' in error_message:
            error_message = format_error_key(error_key) + ' cannot be blank'
        elif 'may not be null' in error_message:
            error_message = format_error_key(error_key) + ' cannot be null'
        elif 'wrong format' in error_message:
            error_message = format_error_key(error_key) + ' format is wrong'
        elif 'object does not exist' in error_message:
            error_message = format_error_key(error_key) + ' does not exists'
        break

    return error_message


def format_error_key(key):
    return key.replace('_', ' ').title()


def json_response(data, http_status):
    return JsonResponse(data=data, status=http_status, safe=False)


def success_ok_data(data):
    return json_response(data, status.HTTP_200_OK)


def success_created_data(data):
    return json_response(data, status.HTTP_201_CREATED)


def success_response(response_serializer, http_status):
    data = get_data_from_response_serializer(response_serializer=response_serializer)
    return JsonResponse(data=data, status=http_status, safe=False)


def get_data_from_response_serializer(response_serializer):
    data = {}
    if response_serializer:
        if not response_serializer.is_valid():
            raise Exception(get_serializer_error_message(response_serializer.errors))

        data = response_serializer.validated_data

    return data


def success_ok(response_serializer):
    return success_response(response_serializer, status.HTTP_200_OK)


def success_created(response_serializer):
    return success_response(response_serializer, status.HTTP_201_CREATED)


def success_no_content():
    return success_response({}, status.HTTP_204_NO_CONTENT)


def success_response_message(success_message):
    response_data = {'message': success_message}
    return JsonResponse(response_data, status=status.HTTP_200_OK)


class SuccessResponse(object):

    @staticmethod
    def get_response_obj(data=None, message=None,):
        if data is not None:
            return Response({
                'data': data,
                },
                status=status.HTTP_200_OK)
        else:
            return Response({
                'message': message
            },
                status=status.HTTP_200_OK)

