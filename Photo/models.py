from django.db import models


class Album(models.Model):
    # album title
    title = models.CharField(max_length=200)
    # album decsription
    desc = models.TextField(max_length=1000)
    # relative path
    path = models.FilePathField()
    # create date
    create_date = models.DateTimeField()
    # upload date
    upload_date = models.DateTimeField()
    # photo count
    photo_count = models.BigIntegerField()
    # parent id
    parent_id = models.ForeignKey('Album', on_delete=models.CASCADE)

