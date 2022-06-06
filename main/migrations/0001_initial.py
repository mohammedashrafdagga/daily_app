# Generated by Django 4.0.5 on 2022-06-06 08:51

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
            name='DailyNotes',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('descriptions', models.TextField()),
                ('note_image', models.ImageField(blank=True, default='image.png', null=True, upload_to='images')),
                ('bacground_image', models.ImageField(blank=True, default='background.png', null=True, upload_to='background')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('user_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
