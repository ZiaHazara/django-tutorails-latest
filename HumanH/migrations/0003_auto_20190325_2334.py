# Generated by Django 2.1.5 on 2019-03-25 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HumanH', '0002_experiencesby'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanstory',
            name='story_teller',
            field=models.ManyToManyField(to='HumanH.ExperiencesBy', verbose_name='Experience By'),
        ),
        migrations.AlterField(
            model_name='experiencesby',
            name='story',
            field=models.ManyToManyField(to='HumanH.HumanStory', verbose_name='Experience Story'),
        ),
    ]
