# Generated by Django 4.1.4 on 2023-01-12 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passnegers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passnegers',
            new_name='Passengers',
        ),
    ]