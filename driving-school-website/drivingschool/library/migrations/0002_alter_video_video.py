# Generated by Django 4.0.4 on 2022-07-06 09:43

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]