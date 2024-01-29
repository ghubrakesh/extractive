from django.db import models

class ExtractedText(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/')
