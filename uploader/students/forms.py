from django import forms
from .models import Detail

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

Job_Choices=[
    ('Data Analyst','Data Analyst'),
    ('Software Engg','Sofware Engg'),
    ('Marketing','Marketing'),
    ('Core','Core')
]

class DetailForm(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 job_type = forms.MultipleChoiceField(label='Preferred Job Type', choices=Job_Choices, widget=forms.CheckboxSelectMultiple)
 class Meta:
  model = Detail
  fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'phone', 'email', 'job_type', 'Profile_picture', 'my_file']
  labels = {'name':'Full Name', 'dob': 'Date of Birth', 'pin':'Pin Code', 'phone':'Mobile No.', 'email':'Email ID', 
  'Profile_picture':'Profile Image', 'my_file':'Document'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'locality':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'phone':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }