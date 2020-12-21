from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=20, default='')
    price = models.IntegerField(default='0')
    description = models.CharField(max_length=1000,default="")
    image = models.ImageField(upload_to="yogbookingapp/media/images")
    def __str__(self):
        return self.name
class Events(models.Model):
    name = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=1000,default="")
    image = models.ImageField(upload_to="yogbookingapp/media/images")
    def __str__(self):
        return self.name
class Blog(models.Model):
    name = models.CharField(max_length=20, default="")
    img1 = models.ImageField(upload_to="yogbookingapp/media/images")
    img2 = models.ImageField(upload_to="yogbookingapp/media/images")
    text = models.CharField(max_length=2000, default="")
    def __str__(self):
        return self.name
class Instructor(models.Model):
        name = models.CharField(max_length=20, default="")
        fathers_name = models.CharField(max_length=20, default="")
        aadhar = models.IntegerField(default='0')
        address = models.CharField(max_length=20, default="")
        experiance = models.CharField(max_length=20, default="")
        city = models.CharField(max_length=50, default="")
        resume = models.FileField(upload_to='yogbookingapp/media/pdf')
        profile = models.ImageField(upload_to="yogbookingapp/media/images")
        rating = models.IntegerField(default=0)
class Booking(models.Model):
    city = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=20, default="")
    no_of_students = models.IntegerField(default=0)
    date_of_event = models.DateField()
class User(models.Model):
    name = models.CharField(max_length=20, default="")
    fathers_name = models.CharField(max_length=20, default="")
    aadhar = models.IntegerField(default='0')
    address = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=50, default="")
    profile = models.ImageField(upload_to="yogbookingapp/media/images")
    proffession = models.CharField(max_length=20, default="")
    gender = models.CharField(max_length=5, default=0)
