# Generated by Django 4.0.6 on 2022-07-07 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(blank=True, max_length=255, null=True)),
                ('short_url', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
