# Generated by Django 4.2.3 on 2023-08-15 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_img',
            field=models.ImageField(default='users/default_user.webp', upload_to='users/'),
        ),
    ]
