# Generated by Django 3.2 on 2021-12-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vergo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.IntegerField(choices=[(1, 'Trending'), (2, 'Latest'), (3, 'Education'), (4, 'Tech'), (5, 'Sports')], default=1),
        ),
    ]
