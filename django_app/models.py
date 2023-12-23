from django.db import models

class data(models.Model):
    stage_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    url = models.URLField(max_length=5000)

    class Meta:
        db_table="data"

    def __str__(self) -> str:
        return self.Name
