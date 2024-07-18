from .models import Articles
from django.forms import ModelForm, TextInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title']

        widgets = {
            'title': Textarea(attrs={
                'class': 'autoresize',
                'oninput': 'autoResize(this)',
                'rows': '1',
                'maxlength': '1000',
                'placeholder': 'Начни писать...'
            })
        }