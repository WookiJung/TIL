# Generated by Django 3.1.7 on 2021-03-18 06:43

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_auto_20210318_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='article/'),
        ),
    ]