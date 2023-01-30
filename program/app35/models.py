from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=20)

class stud_Reg(models.Model):
    name=models.CharField(max_length=100)
    login_id=models.OneToOneField(login,on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    phone_number=models.IntegerField()
    place=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    role=models.CharField(max_length=20)

class Question(models.Model):
    login_id=models.OneToOneField(login,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=20)
    