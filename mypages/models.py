from django.db import models
from django.contrib.auth.models import User
from vocabularytool.utils import unique_slug_generator
from django.db.models.signals import pre_save


class VocabularySets(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, default="")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.slug

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=VocabularySets)

class Vocab(models.Model):
    title = models.ForeignKey(VocabularySets, on_delete=models.CASCADE, null=True)
    word = models.CharField(max_length=20)
    eng = models.CharField(max_length=50)
    p = models.CharField(max_length=30)
    star = models.BooleanField(default=False)

    def __str__(self):
        return self.word
