# Generated by Django 2.2.5 on 2019-09-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GhostsPosts', '0003_auto_20190916_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boast',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.RemoveField(
            model_name='boast',
            name='boastlikes',
        ),
        migrations.AddField(
            model_name='boast',
            name='boastlikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.RemoveField(
            model_name='post',
            name='postlikes',
        ),
        migrations.AddField(
            model_name='post',
            name='postlikes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
