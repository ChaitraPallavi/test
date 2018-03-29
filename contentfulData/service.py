from constants import *
import contentful
from datetime import datetime
from common_utils.error_handler import CondenastException
from serializer import PlaceSerializer, FeedSerializer, ContributorSerializer
from django.conf import settings

# setting contentful client
client = contentful.Client(settings.SPACE_ID,  settings.ACCESS_KEY)
# getting database object
db = settings.DB
# Method takes input and update or edit a place based on placeId


class AddOrEditPlace(object):
    place_serializer = PlaceSerializer

    @classmethod
    def add_edit_place(cls, input_request, place_id):

        # check if object exist, if yes update
        place = db.Places.find({'place_id': place_id})
        if place.count() > 0:
            place = place[0]
            for key, value in input_request.iteritems():
                if key == 'location':
                    location = value.get('en-US')
                    place_location = []
                    place_location.insert(0, location.get('lon'))
                    place_location.insert(1, location.get('lat'))
                    place['location'] = place_location

                elif key == 'contributor':
                    place['contributor'] = value.get('en-US').get('sys').get('id')

                elif key == 'feeds':
                    feeds = value.get('en-US')
                    feeds_tips = []
                    for feed in feeds:
                        feed_id = feed.get('sys').get('id')
                        feeds_tips.append(feed_id)
                        place['feeds'] = feeds_tips

                elif key == 'image':
                    image_id = value.get('en-US').get('sys').get('id')
                    url = client.asset(image_id).url()
                    url = "https:" + url
                    place['image'] = url

                else:
                    place[key] = value.get('en-US')

            place['place_id'] = place.get('place_id')
            place['created_time'] = place.get('created_time')
            place['last_updated_time'] = datetime.now()
            db.Places.update({"place_id": place_id}, place)
            return SuccesMessages.UPDATE_SUCCESSFUL.value

        # If object does not exist create
        else:
            request_dictionary = {}
            for key, value in input_request.iteritems():
                if key == 'location':
                    location = value.get('en-US')
                    place_location = []
                    place_location.insert(0, location.get('lon'))
                    place_location.insert(1, location.get('lat'))
                    request_dictionary['location'] = place_location

                elif key == 'contributor':
                    request_dictionary['contributor'] = value.get('en-US').get('sys').get('id')

                elif key == 'feeds':
                    feeds = value.get('en-US')
                    feeds_tips = []
                    for feed in feeds:
                        feed_id = feed.get('sys').get('id')
                        feeds_tips.append(feed_id)
                        request_dictionary['feeds'] = feeds_tips

                elif key == 'image':
                    image_id = value.get('en-US').get('sys').get('id')
                    url = client.asset(image_id).url()
                    url = "https:" + url
                    request_dictionary['image'] = url

                else:
                    request_dictionary[key] = value.get('en-US')

            serializer_data = cls.place_serializer(data=request_dictionary)
            if serializer_data.is_valid():
                place = serializer_data.data
                place['place_id'] = place_id
                place['created_time'] = datetime.now()
                place['last_updated_time'] = datetime.now()
                db.Places.insert_one(place)
                return SuccesMessages.PLACE_ADDED_SUCCESSFULLY.value
            else:
                raise CondenastException(message=FailureMessages.SERIALIZER_ERRORS.value, data=serializer_data.errors)


class AddEditTips(object):
    tip_serializer = FeedSerializer

    @classmethod
    def add_edit_tips(cls, input_request, document_id):

        feed_tip = db.FeedTips.find({'feed_id': document_id})
        if feed_tip.count() > 0:
            feed_tip = feed_tip[0]
            for key, value in input_request.iteritems():

                if key == 'place':
                    place_id = value.get('en-US').get('sys').get('id')
                    feed_tip['place'] = place_id
                elif key == 'image':
                    image_urls = []
                    url = "https:" + (client.asset(value.get('en-US').get('sys').get('id')).url())
                    image_urls.append(url)
                    feed_tip['image'] = image_urls

                else:
                    feed_tip[key] = value.get('en-US')
            feed_tip['number_of_likes'] = feed_tip.get('number_of_likes')
            feed_tip['feed_id'] = feed_tip.get('feed_id')
            feed_tip['created_time'] = feed_tip.get('created_time')
            feed_tip['last_updated_time'] = datetime.now()
            db.FeedTips.update({"feed_id": document_id}, feed_tip)
            return SuccesMessages.UPDATE_SUCCESSFUL.value

        else:

            request_dictionary = {}
            for key, value in input_request.iteritems():
                if key == 'place':
                    place_id = value.get('en-US').get('sys').get('id')
                    request_dictionary['place'] = place_id

                elif key == 'image':
                    image_urls = []
                    url = "https:" + (client.asset(value.get('en-US').get('sys').get('id')).url())
                    image_urls.append(url)
                    request_dictionary['image'] = image_urls
                else:
                    request_dictionary[key] = value.get('en-US')

            serializer = cls.tip_serializer(data=request_dictionary)
            if serializer.is_valid():
                tips = serializer.data
                tips['feed_id'] = document_id
                tips['number_of_likes'] = 0
                tips['created_time'] = datetime.now()
                tips['last_updated_time'] = datetime.now()
                db.FeedTips.insert_one(tips)

                return SuccesMessages.TIP_ADDED_SUCCESSFULLY.value
            else:
                raise CondenastException(message=FailureMessages.SERIALIZER_ERRORS.value, data=serializer.errors)


class Contributor(object):
    contributor_serializer = ContributorSerializer

    @classmethod
    def add_edit_contributor(cls, input_request, document_id):

        contributor = db.Contributor.find({'contributor_id': document_id})
        if contributor.count() > 0:
            contributor = contributor[0]

            for key, value in input_request.iteritems():
                if key == 'profile_image':
                    image_id = value.get('en-US').get('sys').get('id')
                    url = client.asset(image_id).url()
                    contributor['profile_image'] = "https:" + url
                else:
                    contributor[key] = value.get('en-US')
            contributor['contributor_id'] = contributor.get('contributor_id')
            contributor['created_time'] = contributor.get('created_time')
            contributor['last_updated_time'] = datetime.now()
            db.Contributor.update({"contributor_id": document_id}, contributor)

            return SuccesMessages.UPDATE_SUCCESSFUL.value

        else:

            request_dictionary = {}
            for key, value in input_request.iteritems():

                if key == 'profile_image':
                    image_id = value.get('en-US').get('sys').get('id')
                    url = client.asset(image_id).url()
                    request_dictionary['profile_image'] = "https:" + url
                else:
                    request_dictionary[key] = value.get('en-US')

            serializer = cls.contributor_serializer(data=request_dictionary)
            if serializer.is_valid():
                contributor = serializer.data
                contributor['contributor_id'] = document_id
                contributor['created_time'] = datetime.now()
                contributor['last_updated_time'] = datetime.now()
                db.Contributor.insert_one(contributor)
                return SuccesMessages.CONTRIBUTOR_ADDED_SUCCESSFULLY.value
            raise CondenastException(message=FailureMessages.SERIALIZER_ERRORS.value, data=serializer.errors)

class Noteworthy(object):
    @classmethod
    def add_edit_noteworthy(cls, input_request, document_id):
        
        noteworthy = db.Noteworthy.find_one({"noteworthy_id" : document_id})
        if noteworthy is not None:
            for key, value in input_request.iteritems():
                noteworthy['about'] = value.get('en-US')
                noteworthy['last_updated_time'] = datetime.now()
            db.Noteworthy.update({"noteworthy_id": document_id}, noteworthy)
            return SuccesMessages.UPDATE_SUCCESSFUL.value
        else:
            noteworthy = {}
            for key, value in input_request.iteritems():
                noteworthy['about'] = value.get('en-US')
                noteworthy['noteworthy_id'] = document_id
                noteworthy['created_time'] = datetime.now()
                noteworthy['last_updated_time'] = datetime.now()
            db.Noteworthy.insert_one(noteworthy)
            return SuccesMessages.UPDATE_SUCCESSFUL.value

class DeletePlace(object):
    @classmethod
    def delete_place(cls, place_id):

        # remove related feeds before deleting place
        db.FeedTips.remove({'place': place_id})

        db.Places.remove({'place_id': place_id})
        return SuccesMessages.PLACE_DELETED_SUCCESSFULLY.value


class DeleteTips(object):
    @classmethod
    def delete_tips(cls, feed_id):

            db.FeedTips.remove({'feed_id': feed_id})
            return SuccesMessages.FEED_DELETED_SUCCESSFULLY.value


class DeleteContributor(object):
    @classmethod
    def delete_contributor(cls, contributor_id):

            # get all places added by the contributor
            places = db.Places.find({'contributor': contributor_id})
            if places.count() > 0:
                place_ids = []
                for place in places:
                    place_ids.append(place.get('place_id'))
                # remove all feeds related to each place.
                db.FeedTips.remove({'place': {"$in": place_ids}})
                # remove all places added by contributor
                db.Places.remove({'contributor': contributor_id})

            # delete contributor
            db.Contributor.remove({'contributor_id': contributor_id})
            return SuccesMessages.CONTRIBUTOR_DELETED.value


class DeleteNoteworthy(object):
    @classmethod
    def delete_noteworthy_about(cls, noteworthy_id):
        db.Noteworthy.remove({'noteworthy_id': noteworthy_id})
        return SuccesMessages.FEED_DELETED_SUCCESSFULLY.value