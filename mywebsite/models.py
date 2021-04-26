
from django.db import models

class signupform(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=50)
    community = models.IntegerField()
    
class communities(models.Model):  
    comm_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)

class cquiz(models.Model):
    taker_id = models.AutoField(primary_key=True)
    name_1 = models.CharField(max_length=45)
    location_1 = models.CharField(max_length=45)
    age_1 = models.IntegerField()
    gender_1 = models.CharField(max_length=45)