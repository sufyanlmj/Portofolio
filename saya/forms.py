from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'age', 'alamat', 'email', 'foto']
        
class AbautForm(forms.ModelForm):
    class Meta:
        model = Abaut
        fields = ['judul', 'deskripsi']

        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['judul', 'deskripsi', 'foto']
        
class SertifikatForm(forms.ModelForm):
    class Meta:
        model = Sertifikat
        fields = ['judul_sertifikat', 'deskripsi', 'foto']
        

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ['judul', 'deskripsi', 'foto']
        