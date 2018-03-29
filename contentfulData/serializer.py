from rest_framework import serializers


class PlaceSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=55, required=True, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=40, required=True, allow_null=False, allow_blank=False)
    location = serializers.ListField()
    phone = serializers.CharField(max_length=50, required=True, allow_null=False, allow_blank=False)
    category = serializers.CharField(max_length=50, required=True, allow_null=False, allow_blank=False)
    image = serializers.CharField(max_length=500, required=False, allow_null=False, allow_blank=False)
    cost = serializers.CharField(max_length=50, required=True, allow_null=False, allow_blank=False)
    working_hours = serializers.JSONField()
    contributor = serializers.CharField(max_length=50, required=True, allow_null=False, allow_blank=False)
    # feeds = serializers.ListField()

class FeedSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=500, required=True, allow_null=False, allow_blank=False)
    image = serializers.ListField(required=False)
    place = serializers.CharField(max_length=100, required=True, allow_null=False, allow_blank=False)


class ContributorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, required=True, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=50, required=False, allow_null=False, allow_blank=False)
    password = serializers.CharField(max_length=50, required=False, allow_null=False, allow_blank=False)
    company = serializers.CharField(max_length=200, required=True, allow_null=False, allow_blank=False)
    job_position = serializers.CharField(max_length=200, required=True, allow_null=False, allow_blank=False)
    description = serializers.CharField(max_length=500, required=True, allow_null=False, allow_blank=False)
    profile_image = serializers.CharField(max_length=500, required=True, allow_null=False, allow_blank=False)