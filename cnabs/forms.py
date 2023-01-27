from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
    
    





# from .models import UploadFileForm
# from django.forms import forms





# class ClienteForm(forms.ModalForm):
#     name = forms.Charfield(label='Names')
#     file = forms.FileField()
    
    
# class Cliente(forms.Form):
#     class Meta:
#         model:UploadFileForm
#         fields= "__all__"