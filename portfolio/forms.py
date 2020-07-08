from django import forms

LANGUAGE=[
    ('Subject :I will Love This Subject','Subject :I will Love This Subject'),
    ('ENGLISH','ENGLISH'),
    ('BANGLA','BANGLA'),
    ('MATH','MATH'),
    ('SCIENCE','SCIENCE'),
]
class ContactFroms(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name:','class':'wow fadeInRight','data-wow-duration':'1.7s','data-wow-delay':'.3s'}),label=False,max_length=100,required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email:','class':'wow fadeInRight','data-wow-duration':'2s','data-wow-delay':'.4s'}),label=False,required=False)
    selectOption=forms.ChoiceField(widget=forms.Select(attrs={'placeholder': 'Subject :I will Love This Subject','class':'wow zoomIn','data-wow-duration':'5s'}),label=False,choices=LANGUAGE,required=False)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message:','class':'wow fadeInRight','data-wow-duration':'2.3s','data-wow-delay':'.5s'}),label=False,required=False)


# from django import forms

# from .models import MyModel

# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Name'}),
#             'description': forms.Textarea(
#                 attrs={'placeholder': 'Enter description here'}),
#         }