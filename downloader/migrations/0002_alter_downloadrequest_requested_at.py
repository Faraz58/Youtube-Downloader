# Generated by Django 4.0.5 on 2022-06-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='downloadrequest',
            name='requested_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]