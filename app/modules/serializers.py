from rest_framework import serializers

from .models import Module

from lessons.models import Lesson
from lessons.serializers import LessonSerializer

from taxonomy.models import Standard, StandardsBody, Program, Audience, Tag, Topic, TimeEstimate
from taxonomy.serializers import StandardsSerializer, ProgramSerializer, AudienceSerializer, TagSerializer, TopicSerializer, TimeEstimateSerializer

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        
    standards_alignment = StandardsSerializer(many=True, read_only=True)
    program = ProgramSerializer(many=True, read_only=True)
    time_estimate = TimeEstimateSerializer(many=False, read_only=True)
    audience = AudienceSerializer(many=True, read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    topic = TopicSerializer(many=True, read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)
    # chapter = ChapterSerializer(many=True, read_only=True)
