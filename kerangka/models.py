from django.db import models

# Create your models here.



class EmpInsert(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    typeuser=models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    class Meta:
        db_table='users'
# class User(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     class Meta:
#         db_table='users'
    # def __str__(self):
    #     return self.username

    


    

    
    


