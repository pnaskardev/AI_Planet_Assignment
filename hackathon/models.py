from django.db import models


class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(
        upload_to='hackathon_images/background_images')
    hackathon_image = models.ImageField(
        upload_to='hackathon_images/hackathon_images')
    TYPE_CHOICES = (
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    )
    submission_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.title


class SubmissionImageFile(models.Model):
    image_file = models.ImageField(
        upload_to='hackathon_images/submission_images')
    submission = models.ForeignKey('hackathon.Submission',
                                   on_delete=models.CASCADE)

class SubmissionLinkFile(models.Model):
    link_file = models.URLField(max_length=200)
    submission = models.ForeignKey('hackathon.Submission',
                                   on_delete=models.CASCADE)
    
class SubmissionFile(models.Model):
    file=models.FileField(upload_to='hackathon_submissions/submission_files')
    submission=models.ForeignKey('hackathon.Submission',on_delete=models.CASCADE)

class Submission(models.Model):
    name=models.CharField(max_length=255)
    user=models.ForeignKey('user.User',on_delete=models.CASCADE)
    hackathon=models.ForeignKey('hackathon.Hackathon',on_delete=models.CASCADE)
