from statistics import mode
from django.db import models

# Create your models here.
class Enquiry(models.Model):
    user_name =models.CharField(max_length=50)
    

    phn_num = models.CharField(max_length=15)
    email_id = models.EmailField(max_length=100)