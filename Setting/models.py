from django.db import models

class PhotoRoot(models.Model):
    # photo albums root path
    path = models.FilePathField()
