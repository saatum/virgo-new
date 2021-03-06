# Generated by Django 3.2 on 2021-12-10 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vergo', '0002_alter_post_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vergo.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_category',
            field=models.IntegerField(choices=[(1, 'Trending'), (2, 'Latest'), (3, 'Education'), (4, 'Tech'), (5, 'Sports'), (6, 'news')], default=1),
        ),
    ]
