# Generated by Django 2.1.2 on 2018-10-18 12:40

from django.db import migrations, models
import photo_blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to=photo_blog.models.get_image_path),
        ),
    ]
