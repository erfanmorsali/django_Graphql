# Generated by Django 3.2.3 on 2021-05-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_category'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ManyToManyField(blank=True, related_name='comments', to='post.Post'),
        ),
    ]
