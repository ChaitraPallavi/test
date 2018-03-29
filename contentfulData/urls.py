from django.conf.urls import url
from . import api_views

urlpatterns = [
 url(r'^$', api_views.default_view, name='defaultView'),
 url(r'^publishdata', api_views.UpdateDataToDb.as_view(), name='update_data'),
 url(r'^deletedata$', api_views.DeleteData.as_view()),

 ]