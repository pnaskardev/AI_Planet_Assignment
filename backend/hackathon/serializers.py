

from .models import Hackathon, Submission, SubmissionImageFile,SubmissionFile,SubmissionLinkFile
from rest_framework import serializers


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    hackathon = serializers.PrimaryKeyRelatedField(
        queryset=Hackathon.objects.all())

    submission = serializers.JSONField(required=False)

    class Meta:
        model = Submission
        fields = ['submission','name','user', 'hackathon']

    def create(self, validated_data):
        
        hackathon = validated_data.get('hackathon')
        submission = validated_data.pop('submission')


        if not hackathon:
            raise serializers.ValidationError("Hackathon is required")
        
        type = Hackathon.objects.filter(id=hackathon.id).get().submission_type
        print(type)
        submission_instance = Submission.objects.create(
            **validated_data)
        if type == 'image':
            SubmissionImageFile.objects.create(**submission, submission=submission_instance)
        elif type == 'file':
            SubmissionFile.objects.create(**submission, submission=submission_instance)
        else:
            SubmissionLinkFile.objects.create(**submission, submission=submission_instance)

        return submission_instance
    


