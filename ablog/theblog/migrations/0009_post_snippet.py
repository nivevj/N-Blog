# Generated by Django 4.2.2 on 2023-09-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0008_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click link above to view blog', max_length=225),
        ),
    ]
