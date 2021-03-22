from django import forms
from .models import Article

# forms.form은 특정 모델과 연동 X/ 단순히 데이터 검증 및 HTML생성용
class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=15)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=3, max_value=100)
    content = forms.CharField(widget=forms.Textarea)  # widget은 html생성시 주는 옵션이다.


class AriticleForm(forms.ModelForm):  # 모델과 연동 가능
    class Meta:
        model = Article
        fields = '__all__'