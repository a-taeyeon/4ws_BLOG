from django import forms
from .models import Blog

# class BlogPost(forms.ModelForm): #모델을 기반으로
#     class Meta:
#         model = Blog    #Blog모델을 기반으로
#         fields = ['title', 'body']  #title과 body를 입력받을 수 있는 공간을 만들겠다

class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])