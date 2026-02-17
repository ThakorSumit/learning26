from django.db import models

# Create your models here.
class serivce(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    rating = models.FloatField()
    review = models.TextField()

    class Meta:
        db_table = 'services'
        verbose_name = 'Services'
        verbose_name_plural = 'Services'
    def __str__(self):
        return self.name    

    

    