from django.db import models

# Create your models here.
class Bills(models.Model):
    pro_img = models.CharField(max_length=500)
    pro_name=models.CharField(max_length=255)
    pro_quantity=models.IntegerField()
    pro_rate=models.IntegerField()

    def __str__(self) -> str:
        return self.pro_name