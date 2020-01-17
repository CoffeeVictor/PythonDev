from django.db import models

class Dataset(models.Model):
    data_file = models.FileField('Upload csv:', upload_to='', blank=True)
