# models.py
from django.db import models

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    correctAnswers = models.IntegerField()
    percentage = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class VideoDB(models.Model):
    u_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videodb')
    videoP1 = models.IntegerField(default=0)
    videoP2 = models.IntegerField(default=0)
    videoP3 = models.IntegerField(default=0)
    videoP4 = models.IntegerField(default=0)
    videoP5 = models.IntegerField(default=0)
    videoP6 = models.IntegerField(default=0)
    videoP7 = models.IntegerField(default=0)
    videoP8 = models.IntegerField(default=0)
    videoP9 = models.IntegerField(default=0)
    videoP10 = models.IntegerField(default=0)
    videoP11 = models.IntegerField(default=0)
    videoP12 = models.IntegerField(default=0)
    videoP13 = models.IntegerField(default=0)
    videoP14 = models.IntegerField(default=0)
    videoP15 = models.IntegerField(default=0)
    videoP16 = models.IntegerField(default=0)
    videoP17 = models.IntegerField(default=0)
    

    def __str__(self):
        return str(self.u_id)