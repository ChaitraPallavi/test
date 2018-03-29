from django.conf import settings
from common_utils.error_handler import CondenastException
from constants import FailureMessage, StatusCodes
from common_utils.error_handler import ErrorHandler

db = settings.DB


class AuthenticateUser():

    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_TOKEN')
            if not token:
                raise CondenastException(message=FailureMessage.SESSION_INVALID.value, status_code=StatusCodes.UNAUTHORIZED.value)
            user = db.UserSession.aggregate([{"$match": {"token": token}},
            {
                "$lookup": {
                    "from": "Users",
                    "localField": "userId",
                    "foreignField": "userId",
                    "as": "userData"
                    }
            },
            {"$project": {"user_id": 1, "userData": 1, "_id": 0}}
            ])
            if not user.alive:
                raise CondenastException(message=FailureMessage.SESSION_INVALID.value, status_code=StatusCodes.UNAUTHORIZED.value)

            return user, None
        except Exception as exception:
            return ErrorHandler.handle_exception(exception)


