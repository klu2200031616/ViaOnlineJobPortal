from datetime import date

from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class ViaUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to="media/",null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15,null=True)
    def __str__(self):
        return self.user.username



class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.ImageField(upload_to="media/",null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=100)
    type = models.CharField(max_length=15, null=True)
    # status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username

class Job(models.Model):
    recruiter = models.ForeignKey(Employer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.FloatField()
    image = models.ImageField(upload_to="media/")# Change upload_to parameter
    description = models.CharField(max_length=300)
    experience = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    company = models.CharField(max_length=100)  # Add company_name field
    creationdate = models.DateField(auto_now_add=True)  # Add creation date field

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth import get_user_model

class AppliedJobs(models.Model):
    resume = models.FileField(upload_to="media/")
    name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    qualification = models.CharField(max_length=100)
    cgpa = models.FloatField()
    marksheet = models.FileField(upload_to="media/")
    github = models.URLField()
    date_applied = models.DateTimeField(auto_now_add=True)
    candidate = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    email=models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    employer = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)  # Relate to the company
    STATUS_CHOICES = [
        ('selected', 'Selected'),
        ('unselected', 'Unselected'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.name







# class CustomUser(AbstractUser):
#     company_name = models.CharField(max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.username

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name