# Generated by Django 3.0.2 on 2020-01-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_auto_20200116_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='data_bin',
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data_file',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='heloo'),
        ),
    ]
