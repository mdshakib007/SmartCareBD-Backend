# Generated by Django 5.1 on 2025-01-10 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]