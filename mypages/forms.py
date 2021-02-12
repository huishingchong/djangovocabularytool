from django import forms
from django.forms import ModelForm
from .models import Vocab, VocabularySets

def isAllChinese(s):
    for c in s:
        if not('\u4e00' <= c <= '\u9fa5'):
            return False
    return True

class TitleForm(forms.ModelForm):
    class Meta:
        model = VocabularySets
        fields = ['title']
        unique_together = ('title', 'slug')


class VocabForm(forms.ModelForm):
    class Meta:
        model = Vocab
        fields = ['word', 'star']

    def clean_word(self, *args, **kwargs):
        word = self.cleaned_data.get("word")
        condition = isAllChinese(word)
        if condition == True:
            return word

class EditForm(forms.ModelForm):
    class Meta:
        model = Vocab
        fields = ['word', 'eng']
