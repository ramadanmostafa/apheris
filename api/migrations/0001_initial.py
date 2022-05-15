# Generated by Django 4.0.4 on 2022-05-15 05:33

import api.mixins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('data', models.JSONField(default=dict)),
            ],
            options={
                'abstract': False,
            },
            bases=(api.mixins.EventDispatcherMixin, models.Model),
        ),
    ]
