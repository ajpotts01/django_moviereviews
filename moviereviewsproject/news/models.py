from django.db import models

class News(models.Model):
    class Meta:
            verbose_name_plural = "news posts"
            
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()