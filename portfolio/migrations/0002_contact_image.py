# Generated by Django 3.0.8 on 2020-07-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.FileField(default=1, upload_to='comment'),
            preserve_default=False,
        ),
    ]
