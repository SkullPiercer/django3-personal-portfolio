from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(auto_now=True)
    url = models.URLField(blank=False)

    def __str__(self):
        return self.title
