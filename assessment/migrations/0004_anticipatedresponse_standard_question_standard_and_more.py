# Generated by Django 4.2.6 on 2023-11-06 19:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_alter_question_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='anticipatedresponse',
            name='standard',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Standard must be in the format of 'x.xx.x' or 'x.xxx.x' where x is a number", regex='^\\d+(\\.\\w+){2}$')]),
        ),
        migrations.AddField(
            model_name='question',
            name='standard',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Standard must be in the format of 'x.xx.x' or 'x.xxx.x' where x is a number", regex='^\\d+(\\.\\w+){2}$')]),
        ),
        migrations.AddField(
            model_name='userresponse',
            name='standard',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="Standard must be in the format of 'x.xx.x' or 'x.xxx.x' where x is a number", regex='^\\d+(\\.\\w+){2}$')]),
        ),
    ]
