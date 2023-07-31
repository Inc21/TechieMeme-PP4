# Generated by Django 4.2.3 on 2023-07-30 17:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meme',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='meme',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('comment', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('like', 'Like'), ('unlike', 'Un Like')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('meme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memes.meme')),
            ],
        ),
        migrations.AddField(
            model_name='meme',
            name='tags',
            field=models.ManyToManyField(blank=True, to='memes.tag'),
        ),
    ]