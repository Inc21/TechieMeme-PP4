# Generated by Django 4.2.3 on 2023-07-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0002_tag_meme_vote_ratio_meme_vote_total_review_meme_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='meme',
            name='meme_img',
            field=models.ImageField(default='static/images/placeholder.png', upload_to='static/images/'),
        ),
    ]
