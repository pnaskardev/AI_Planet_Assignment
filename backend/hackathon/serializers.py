

from .models import Hackathon, Submission, SubmissionImageFile
from rest_framework import serializers


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    hackathon = HackathonSerializer()

    submission = serializers.JSONField()

    class Meta:
        model = Submission
        fields = '__all__'

        def create(self, validated_data):

            hackathon = validated_data.pop('hackathon')
            submission = validated_data.pop('submission')
            print(hackathon)
            print(submission)

            if not hackathon:
                raise serializers.ValidationError("Hackathon is required")
            type = hackathon.get('submission_type')
            submission_instance = Submission.objects.create(
                **validated_data)
            # if type == 'image':
            #     SubmissionImageFile.objects.create()

            return submission_instance
