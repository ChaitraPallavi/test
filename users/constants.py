from enum import Enum

class RequestKeys(Enum):
   LATITUDE = 'latitude'
   LONGITUDE = 'longitude'
   RADIUS = 'radius' #range of radius to be covered.
   PLACE_ID = 'placeId'
   LIMIT = 'limit'
   PAGE_NUM = 'pageNo'
   CONTRIBUTOR_ID = 'contributorId'

class ResponseKeys(Enum):
    TITLE = 'title'
    DESCRIPTION = 'description'
    WORKING = 'workingHours'
    PHONE = 'phone'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    CATEGORY = 'category'
    PLACE_ID = 'placeId'
    COST = 'cost'
    PLACE_IMAGE = 'placeImageUrl'
    PLACE_FEEDS = 'placeFeeds'
    TOTAL_FEEDS = 'totalFeeds'
    FEED_DESCRIPTION = 'feedDescription'
    FEED_IMAGES = 'feedImages'
    FEED_LIKES = 'feedLikes'
    CONTRIBUTOR_ID = 'contributorId'
    CONTRIBUTOR_NAME = 'contributorName'
    CONTRIBUTOR_IMAGE = 'contributorImageUrl'
    CONTRIBUTOR_DESCRIPTION = 'contributorDescription'
    CONTRIBUTOR_JOB = 'contributorJobDescription'
    CONTRIBUTOR_COMPANY = 'contributorCompany'
    FEED_ID = 'feedId'
    CONTRIBUTOR = 'contributor'
    PLACE_DETAILS = 'placeDetails'
    TOTAL_LIKES = 'totalLikes'
    TOTAL_PLACES = 'totalPlaces'

class PaginationConstants(Enum):

    DEFAULT_LIMIT = 5;
    DEFAULT_PAGE_NUM = 0


class FailureMessage(Enum):
    EMPTY_REQUEST = 'Request cannot be empty'
    INVALID_PLACE = 'Place is invalid. Please select a valid place'
    INVALID_REQUEST = 'Invalid request'
    SESSION_INVALID = 'Session invalid'
    SERIALIZER_ERRORS = 'Serializer validation failed'


class SuccesMessages(Enum):
    LOGOUT_SUCCESS = 'logged out successfully'

class StatusCodes(Enum):
    UNAUTHORIZED = 401
