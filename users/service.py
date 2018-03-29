from django.conf import settings
from constants import ResponseKeys,FailureMessage, PaginationConstants
from common_utils.error_handler import CondenastException
from datetime import datetime
import uuid

db = settings.DB


class FindPlacesFromLocation(object):
    @staticmethod
    def find_near_by_places(lat, lon, radius):
        places = db.Places.find(
            {
                "location":
                    {"$near": {"$geometry": {"type": "Point", "coordinates": [lon, lat]}, "$maxDistance": radius}}},
            {"place_id": 1, "_id": 0}
        )
        
        placeIds = []
        for id in places:
            placeIds.append(id.get('place_id'))

        places = db.Places.aggregate([
            {"$match": {"place_id": {"$in": placeIds}}},
            {
            "$lookup": {
                "from": "Contributor",
                "localField": "contributor",
                "foreignField": "contributor_id",
                "as": "contributor_data"
                }
            }, {
            "$lookup": {
                "from": "FeedTips",
                "localField": "place_id",
                "foreignField": "place",
                "as": "FeedTips",
                }
            }
        ])
        if placeIds is not []:
            places_in_range = []

            for place in places:
                place_details = {}
                place_data = {}
                place_data[ResponseKeys.TITLE.value] = place.get('title')
                place_data[ResponseKeys.DESCRIPTION.value] = place.get('description')
                place_data[ResponseKeys.LATITUDE.value] = place.get('location')[1]
                place_data[ResponseKeys.LONGITUDE.value] = place.get('location')[0]
                place_data[ResponseKeys.WORKING.value] = place.get('working_hours')
                place_data[ResponseKeys.CATEGORY.value] = place.get('category')
                place_data[ResponseKeys.PHONE.value] = place.get('phone')
                place_data[ResponseKeys.PLACE_ID.value] = place.get('place_id')
                place_data[ResponseKeys.COST.value] = place.get('cost')
                place_data[ResponseKeys.PLACE_IMAGE.value] = place.get('image')
                place_details[ResponseKeys.PLACE_DETAILS.value] = place_data

                contributor_details = {}
                contributor = place.get('contributor_data')[0]
                contributor_details[ResponseKeys.CONTRIBUTOR_ID.value] = contributor.get('contributor_id')
                contributor_details[ResponseKeys.CONTRIBUTOR_NAME.value] = contributor.get('name')
                contributor_details[ResponseKeys.CONTRIBUTOR_DESCRIPTION.value] = contributor.get('description')
                contributor_details[ResponseKeys.CONTRIBUTOR_IMAGE.value] = contributor.get('profile_image')
                contributor_details[ResponseKeys.CONTRIBUTOR_COMPANY.value] = contributor.get('company')
                contributor_details[ResponseKeys.CONTRIBUTOR_JOB.value] = contributor.get('job_position')
                place_details[ResponseKeys.CONTRIBUTOR.value] = contributor_details

                place_feeds = []
                feeds = place.get('FeedTips')
                for feed in feeds:
                    feed_details = {}
                    feed_details[ResponseKeys.FEED_DESCRIPTION.value] = feed.get('description')
                    feed_details[ResponseKeys.FEED_ID.value] = feed.get('feed_id')
                    feed_details[ResponseKeys.FEED_LIKES.value] = feed.get('number_of_likes')
                    feed_details[ResponseKeys.FEED_IMAGES.value] = feed.get('image')
                    place_feeds.append(feed_details)
                place_details[ResponseKeys.TOTAL_FEEDS.value] = len(feeds)
                place_details[ResponseKeys.PLACE_FEEDS.value] = place_feeds

                places_in_range.append(place_details)
        return places_in_range


class GetPlaceDetailsFromPlaceId(object):

    @staticmethod
    def get_place_details(place_id, limit, page_num):

        place = db.Places.find({'place_id': place_id})
        if not place.count() >0:
            raise CondenastException(message=FailureMessage.INVALID_PLACE.value)
        else:
            place = place[0]
            place_details= {}
            place_data = {}
            place_data[ResponseKeys.TITLE.value] = place.get('title')
            place_data[ResponseKeys.DESCRIPTION.value] = place.get('description')
            place_data[ResponseKeys.LATITUDE.value] = place.get('location')[1]
            place_data[ResponseKeys.LONGITUDE.value] = place.get('location')[0]
            place_data[ResponseKeys.WORKING.value] = place.get('working_hours')
            place_data[ResponseKeys.CATEGORY.value] = place.get('category')
            place_data[ResponseKeys.PHONE.value] = place.get('phone')
            place_data[ResponseKeys.PLACE_ID.value] = place.get('place_id')
            place_data[ResponseKeys.COST.value] = place.get('cost')
            place_data[ResponseKeys.PLACE_IMAGE.value] = place.get('image')
            place_details[ResponseKeys.PLACE_DETAILS.value] = place_data

            feeds = db.FeedTips.find({'place': place_id}).skip(limit*page_num).limit(limit)
            place_feeds = []
            if feeds.count() > 0:
                for feed in feeds:
                    feed_details = {}
                    feed_details[ResponseKeys.FEED_DESCRIPTION.value] = feed.get('description')
                    feed_details[ResponseKeys.FEED_ID.value] = feed.get('feed_id')
                    feed_details[ResponseKeys.FEED_LIKES.value] = feed.get('number_of_likes')
                    feed_details[ResponseKeys.FEED_IMAGES.value] = feed.get('image')
                    place_feeds.append(feed_details)
                place_details[ResponseKeys.TOTAL_FEEDS.value] = feeds.count()
            place_details[ResponseKeys.PLACE_FEEDS.value] = place_feeds

            contributor = db.Contributor.find({'contributor_id': place.get('contributor')})
            contributor_details = {}
            if contributor.count() > 0:
                contributor = contributor[0]
                contributor_details[ResponseKeys.CONTRIBUTOR_ID.value] = contributor.get('contributor_id')
                contributor_details[ResponseKeys.CONTRIBUTOR_NAME.value] = contributor.get('name')
                contributor_details[ResponseKeys.CONTRIBUTOR_DESCRIPTION.value] = contributor.get('description')
                contributor_details[ResponseKeys.CONTRIBUTOR_IMAGE.value] = contributor.get('profile_image')

            place_details[ResponseKeys.CONTRIBUTOR.value] = contributor_details
            return place_details


class ContributorDetails(object):
    @staticmethod
    def contributor_details(contributor_id, limit, page_num):
        response_data = {}
        contributor = db.Contributor.find_one({"contributor_id": contributor_id})
        if contributor is not None:
            response_data[ResponseKeys.CONTRIBUTOR_ID.value] =  contributor.get('contributor_id')

            places = db.Places.aggregate([{"$match": {"contributor": contributor_id}},
                                          {"$project": {"place_id": 1, "location": 1, "_id": 0}},{"$skip": page_num*limit},{"$limit": limit}
            ])
            total_places = db.Places.find({"contributor": contributor_id}).count()
            place_details = []
            for place in places:
                place_data = {
                    ResponseKeys.PLACE_ID.value: place.get('place_id'),
                    ResponseKeys.LATITUDE.value : place.get('location')[1],
                    ResponseKeys.LONGITUDE.value : place.get('location')[0]
                }
                place_details.append(place_data)
            response_data[ResponseKeys.TOTAL_PLACES.value]= total_places
            response_data[ResponseKeys.PLACE_DETAILS.value] = place_details
        return response_data


