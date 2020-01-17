# Generated by Django 3.0.2 on 2020-01-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0003_auto_20200116_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='knn',
            field=models.BooleanField(default=False, verbose_name='KNN:'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='svm',
            field=models.BooleanField(default=False, verbose_name='Linear SVM:'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='tree',
            field=models.BooleanField(default=False, verbose_name='Decision Tree:'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='data_file',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='Upload csv:'),
        ),
    ]
