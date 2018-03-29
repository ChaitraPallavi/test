from django.conf.urls import url
from . import api_views

urlpatterns = [
 url(r'^getnearbyplaces', api_views.GetNearByPlaces.as_view(), name='near_by_places'),
 url(r'^getplacedetails', api_views.GetPlaceDetails.as_view()),
 url(r'^getcontributordetails', api_views.GetContributorDetails.as_view())
 ]
