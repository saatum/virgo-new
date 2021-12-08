# Generated by Django 3.2 on 2021-11-05 14:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default=None, upload_to='static/images')),
                ('description', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(unique=True)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('post_category', models.IntegerField(choices=[(1, 'Trending'), (2, 'Latest'), (3, 'Education'), (4, 'Tech'), (5, 'Sports'), (6, 'Politics'), (7, 'History')], default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
