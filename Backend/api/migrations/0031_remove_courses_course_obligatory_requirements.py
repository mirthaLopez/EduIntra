# Generated by Django 5.1.2 on 2024-12-02 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_student_student_id_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='course_obligatory_requirements',
        ),
    ]