from rest_framework import serializers

from .models import Standard, StandardsBody, Program, Audience, Tag, Topic, AssetType, ActivityType, TimeEstimate, LearningSpace

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class StandardsBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardsBody
        fields = '__all__'

class StandardsSerializer(serializers.ModelSerializer):
    standard_group = StandardsBodySerializer(many=False, read_only=True)

    class Meta:
        model = Standard
        fields = '__all__'

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audience
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'

class TimeEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEstimate
        fields = '__all__'

class LearningSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningSpace
        fields = '__all__'
