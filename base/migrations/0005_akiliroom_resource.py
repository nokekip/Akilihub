# Generated by Django 5.0.2 on 2024-02-09 11:47

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkiliRoom',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.field')),
                ('members', models.ManyToManyField(blank=True, related_name='members', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('link', models.TextField(null=True)),
                ('related_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.field')),
            ],
        ),
    ]