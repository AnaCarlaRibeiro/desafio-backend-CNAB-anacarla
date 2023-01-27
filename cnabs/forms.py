from django import forms
from .models import ArquivoModel
from  django.db import models



class FileForm(models.Model):
    file = models.FileField()

class UploadFileForm(forms.ModelForm):
    class Meta:
        model= FileForm
        fields= "__all__"
    
    
    




