# Generated by Django 4.2 on 2023-05-08 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artisan', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='artisan',
            new_name='user',
        ),
    ]
