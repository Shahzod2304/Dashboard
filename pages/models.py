from django.db import models

# Create your models here.


class Excel_file(models.Model):
    Year = models.CharField(max_length=15)
    Industry_aggregation_NZSIOC = models.CharField(max_length=50)
    Industry_code_NZSIOC = models.CharField(max_length=50)
    Industry_name_NZSIOC = models.CharField(max_length=50)
    Units = models.CharField(max_length=50)
    Variable_code = models.CharField(max_length=50)
    Variable_name = models.CharField(max_length=50)
    Variable_category = models.CharField(max_length=50)
    Value = models.FloatField()
    Industry_code_ANZSIC06 = models.CharField(max_length=255)

    def __str__(self):
        return self.Variable_name
    
