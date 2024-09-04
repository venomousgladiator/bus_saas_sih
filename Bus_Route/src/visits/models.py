from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> Table 
    # id -> primary key 
    path = models.TextField(blank=True,null=True)
    timestamp =  models.DateTimeField(auto_now_add= True) #col
    