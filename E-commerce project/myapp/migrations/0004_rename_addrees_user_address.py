# Generated by Django 5.0.6 on 2024-05-29 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_password_alter_user_addrees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='addrees',
            new_name='address',
        ),
    ]
