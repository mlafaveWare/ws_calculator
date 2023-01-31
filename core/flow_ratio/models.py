from django.db import models

# Create your models here.
class Flow_Ratio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.CharField(max_length=5000)

    def _str_(self):
        return self.title