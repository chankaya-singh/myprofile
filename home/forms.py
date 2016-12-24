'''
Created on 28-Nov-2016

@author: priyansh
'''
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file=forms.FileField()
    
    
    
    

