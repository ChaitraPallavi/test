from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from constants import *
from common_utils.error_handler import ErrorHandler
from common_utils.response_handler import SuccessResponse
from common_utils.error_handler import CondenastException
from service import *
from user_authentication import AuthenticateUser
from serializer import UserSerializer

class GetNearByPlaces(APIView):
    authentication_classes = (AuthenticateUser,)
    
    def post(self, request):

        try:
            if not request.data:
                raise CondenastException(message=FailureMessage.EMPTY_REQUEST.value)

            lat = request.data.get(RequestKeys.LATITUDE.value)
            lon = request.data.get(RequestKeys.LONGITUDE.value)
            radius = request.data.get(RequestKeys.RADIUS.value)

            places_in_range = FindPlacesFromLocation.find_near_by_places(lat, lon, radius)
            return SuccessResponse.get_response_obj(data=places_in_range)

        except Exception as exception:
            return ErrorHandler.handle_exception(exception)


class GetPlaceDetails(APIView):
    authentication_classes = (AuthenticateUser,)

    def get(self, request):

        try:

            place_id = request.query_params.get(RequestKeys.PLACE_ID.value)
            limit = request.query_params.get(RequestKeys.LIMIT.value)
            page_num = request.query_params.get(RequestKeys.PAGE_NUM.value)

            if limit is None:
                limit = PaginationConstants.DEFAULT_LIMIT.value

            if page_num is None:
                page_num = PaginationConstants.DEFAULT_PAGE_NUM.value

            if not place_id:
                raise CondenastException(message=FailureMessage.INVALID_REQUEST.value)

            place_details = GetPlaceDetailsFromPlaceId.get_place_details(place_id, int(limit), int(page_num))
            return SuccessResponse.get_response_obj(data=place_details)

        except Exception as exception:
            return ErrorHandler.handle_exception(exception)


class GetContributorDetails(APIView):
    authentication_classes = (AuthenticateUser,)
    
    def get(self, request):

        try:

            contributor_id = request.query_params.get(RequestKeys.CONTRIBUTOR_ID.value)
            limit = request.query_params.get(RequestKeys.LIMIT.value)
            page_num = request.query_params.get(RequestKeys.PAGE_NUM.value)

            if limit is None:
                limit = PaginationConstants.DEFAULT_LIMIT.value

            if page_num is None:
                page_num = PaginationConstants.DEFAULT_PAGE_NUM.value

            if contributor_id is None:
                raise CondenastException(message=FailureMessage.INVALID_REQUEST.value)

            response_data = ContributorDetails.contributor_details(contributor_id, int(limit), int(page_num))
            return SuccessResponse.get_response_obj(data=response_data)

        except Exception as exception:
            return ErrorHandler.handle_exception(exception)

