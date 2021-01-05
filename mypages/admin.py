from django.contrib import admin
from .models import Vocab, VocabularySets

# Register your models here.
admin.site.register(VocabularySets)
admin.site.register(Vocab)