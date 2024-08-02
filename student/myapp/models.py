from django.db import models

# Create your models here.

class Faculty(models.Model):
    fac_name = models.CharField(max_length=50) 
    femail = models.EmailField(unique=True)  
    fpassword = models.CharField(max_length=128)

    def __str__(self):
        return self.fac_name +" "+self.femail

class Student(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50) 
    lname = models.CharField(max_length=50) 
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=128)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other')
    qualification = models.CharField(max_length=100, choices=[
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('graduate', 'Graduate'),
        ('postgraduate', 'Postgraduate'),
    ])

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.qualification})"
