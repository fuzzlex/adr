# Generated by Django 4.0 on 2023-03-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_question_plananswer_question_uncurrectanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='currect',
            field=models.CharField(default='evet', max_length=500),
            preserve_default=False,
        ),
    ]
