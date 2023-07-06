from django.contrib import admin
from . models import Hackathon, Submission, SubmissionFile, SubmissionImageFile, SubmissionLinkFile

admin.site.register(Hackathon)
admin.site.register(Submission)
admin.site.register(SubmissionFile)
admin.site.register(SubmissionImageFile)
admin.site.register(SubmissionLinkFile)
