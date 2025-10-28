from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    alamat = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField(upload_to='profile/', blank=True , null=True)

    def __str__(self):
        return self.name

class Abaut(models.Model):
    judul = models.CharField(max_length=100)
    tanggal = models.DateField(auto_now_add=True)
    deskripsi = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.judul
    
class Project(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='project/')

    def __str__(self):
        return self.judul

class Sertifikat(models.Model):
    judul_sertifikat = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='sertifikat/')
    tanggal = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.judul_sertifikat
    
class Design(models.Model):
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='design/')
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.judul



















