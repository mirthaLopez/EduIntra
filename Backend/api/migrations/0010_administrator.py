# Generated by Django 5.1.2 on 2024-11-11 19:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_form'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_first_last_name', models.CharField(max_length=50)),
                ('admin_second_last_name', models.CharField(max_length=50)),
                ('admin_phone_number', models.CharField(max_length=20)),
                ('admin_email', models.EmailField(max_length=254)),
                ('admin_address_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.addresses')),
                ('admin_auth_user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
