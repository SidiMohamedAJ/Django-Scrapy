from django.db import models

class data(models.Model):
    stage_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    url = models.URLField(max_length=5000)

   # class Meta:
       # verbose_name = 'Jobs Data'
       # verbose_name_plural = 'Jobs Data'

    def __str__(self) -> str:
        return self.Name
