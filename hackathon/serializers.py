from .models import Hackathon, Submission, SubmissionImageFile, SubmissionFile, SubmissionLinkFile
from rest_framework import serializers


class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    hackathon = serializers.PrimaryKeyRelatedField(
        queryset=Hackathon.objects.all())

    submission_type = serializers.CharField(write_only=True)

    hackathon_body = HackathonSerializer(source='hackathon', read_only=True)

    file = serializers.FileField(write_only=True, required=False)

    url = serializers.URLField(write_only=True, required=False)

    class Meta:
        model = Submission
        # depth = 1
        fields = ['file', 'url', 'name', 'user',
                  'hackathon', 'hackathon_body', 'submission_type']

    def validate(self, attrs):
        print(attrs)
        hackathon = attrs.get('hackathon')
        user = self.context['request'].user
        print(hackathon)
        submission_type = hackathon.submission_type
        input_submission_type = attrs.get('submission_type')
        print(submission_type)
        print(input_submission_type)
        if submission_type != input_submission_type:
            raise serializers.ValidationError(
                "Submission type is not valid")

        if not user.hackathons.filter(id=hackathon.id).exists():
            raise serializers.ValidationError(
                "User is not registered for this hackathon")

        if submission_type=='link' and attrs.get('url'):
            pass
        elif submission_type != 'link' and attrs.get('file'):
            file_type = attrs.get('file').content_type
            if submission_type == 'image' and file_type not in ['image/png', 'image/jpeg', 'image/jpg']:
                raise serializers.ValidationError(
                    'Invalid file type for image submission')

            if submission_type == 'file' and file_type in ['image/png', 'image/jpeg', 'image/jpg', 'text/plain']:
                raise serializers.ValidationError(
                    'Invalid file type for file submission')
        else:
            raise serializers.ValidationError(
                f'{submission_type} is required for submission')

        if Submission.objects.filter(hackathon=hackathon, user=user).exists():
            raise serializers.ValidationError(
                "User has already submitted for this hackathon")

        return attrs

    def create(self, validated_data):
        validated_data.pop('submission_type')
        print(validated_data)

        hackathon = validated_data.get('hackathon')

        if not hackathon:
            raise serializers.ValidationError("Hackathon is required")

        type = Hackathon.objects.filter(id=hackathon.id).get().submission_type

        if type == 'image':
            file = validated_data.pop('file')
            submission_instance = Submission.objects.create(
                **validated_data)
            SubmissionImageFile.objects.create(
                file=file, submission=submission_instance)
        elif type == 'file':
            file = validated_data.pop('file')
            submission_instance = Submission.objects.create(
                **validated_data)
            SubmissionFile.objects.create(
                file=file, submission=submission_instance)
        else:
            url = validated_data.pop('url')
            submission_instance = Submission.objects.create(
                **validated_data)
            SubmissionLinkFile.objects.create(
                file=url, submission=submission_instance)

        return submission_instance
