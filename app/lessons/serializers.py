from rest_framework import serializers

from .models import Lesson

from taxonomy.models import Standard, StandardsBody, Program, Audience, Tag, Topic, TimeEstimate
from taxonomy.serializers import StandardsSerializer, ProgramSerializer, AudienceSerializer, TagSerializer, TopicSerializer, TimeEstimateSerializer




class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

    # standards_alignment = StandardsSerializer(many=True, read_only=True)
    # program = ProgramSerializer(many=True, read_only=True)
    # time_estimate = TimeEstimateSerializer(many=False, read_only=True)
    # audience = AudienceSerializer(many=True, read_only=True)
    # tag = TagSerializer(many=True, read_only=True)
    # topic = TopicSerializer(many=True, read_only=True)
    # chapter = ChapterSerializer(many=True, read_only=True)
