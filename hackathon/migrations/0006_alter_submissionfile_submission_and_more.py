# Generated by Django 4.2.3 on 2023-07-16 16:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0005_rename_image_file_submissionimagefile_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissionfile',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_file', to='hackathon.submission', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])]),
        ),
        migrations.AlterField(
            model_name='submissionimagefile',
            name='file',
            field=models.ImageField(upload_to='submission_images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
    ]
