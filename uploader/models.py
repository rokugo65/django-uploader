from django.db import models

def file_path(instance, filename):
    path = 'images/'
    return path + filename

class Image(models.Model):
    image = models.FileField(upload_to=file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
