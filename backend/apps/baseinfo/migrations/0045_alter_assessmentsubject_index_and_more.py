# Generated by Django 4.1.5 on 2023-02-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0044_alter_questionnaire_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentsubject',
            name='index',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='assessmentsubject',
            unique_together={('index', 'assessment_profile'), ('title', 'assessment_profile')},
        ),
    ]