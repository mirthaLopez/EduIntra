# Generated by Django 5.1.2 on 2024-12-03 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_remove_courses_course_obligatory_requirements'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_Modality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_modality_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]