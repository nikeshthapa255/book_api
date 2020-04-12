# Generated by Django 3.0.5 on 2020-04-11 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('amazon_url', models.URLField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateTimeField(auto_now=True)),
                ('favourite', models.ManyToManyField(related_name='favourite', to='account.Book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-join_date'],
            },
        ),
    ]
