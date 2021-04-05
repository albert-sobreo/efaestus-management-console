# Generated by Django 3.1.7 on 2021-03-19 10:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210317_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(default='Unresolved', max_length=10),
        ),
        migrations.AlterField(
            model_name='work',
            name='assignees',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
