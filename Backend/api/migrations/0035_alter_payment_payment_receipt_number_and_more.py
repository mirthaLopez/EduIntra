# Generated by Django 5.1.2 on 2024-12-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_courses_obligatory_requirements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_receipt_number',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_receipt_url',
            field=models.URLField(null=True),
        ),
    ]
