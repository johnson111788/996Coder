# Generated by Django 3.0.8 on 2020-07-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognitions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='name',
        ),
        migrations.RemoveField(
            model_name='preimg',
            name='name',
        ),
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='preimg',
            name='img',
            field=models.FileField(upload_to='media'),
        ),
    ]
