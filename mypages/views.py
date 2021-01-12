from django.shortcuts import render, redirect, get_object_or_404, Http404
from django import forms
from django.http import HttpResponse
from .models import Vocab, VocabularySets
from .forms import VocabForm, TitleForm, EditForm
from googletrans import Translator
import pinyin_jyutping_sentence
from django.contrib.auth.models import User
from django.contrib import messages
from vocabularytool.utils import render_to_pdf
from django.template.loader import get_template


def home(request):
    all_item = VocabularySets.objects.all
    details = Vocab.objects.all
    if request.method == 'POST':
        form = TitleForm(request.POST or None)
        if form.is_valid():
            title = form.save(commit=False)
            title.username = request.user
            title.save()
            context = {'title': title, 'form': form, 'all_item': all_item}
            return render(request, 'home.html', context)
        else:
            messages.error(request, 'Input not valid.')
            return redirect(home)
    else: 
        if request.user.is_authenticated:
            count = VocabularySets.objects.filter(username=request.user).count()
        else:
            count = 0
        return render(request, 'home.html', {'all_item': all_item, 'details': details, 'count': count})


def about(request):
    return render(request, 'about.html', {})


def create(request, slug):
    table = VocabularySets.objects.get(slug=slug)   #get the slug object from VocabularySets model
    all_item = Vocab.objects.all
    
    if request.method == 'POST':
        form = VocabForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            w = request.POST.get('word')
            f.p = pinyin_jyutping_sentence.pinyin(w)
            trans = Translator()
            e = trans.translate(w)
            f.eng = e.text
            f.title = table
            form.save()
            context = {'all_item': all_item, 'table': table}
            return render(request, 'create.html', context)
        else:
            messages.error(request, 'Input not valid (e.g. can only accept chinese and up to 20 characters).')
            return redirect(create, slug)
    else:
        return render(request, 'create.html', {'table': table, 'all_item': all_item})


def vocab_delete_view(request, slug, id):
    obj = Vocab.objects.get(pk=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    messages.success(request, ('Vocabulary has been deleted.'))
    return render(request, 'vocab_delete.html', {'object': obj})


def vocab_edit_view(request, slug, id):
    if request.method == 'POST':
        obj = Vocab.objects.get(pk=id)
        form = EditForm(request.POST or None, instance=obj)
        if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.eng = obj.eng
            new_obj.save()
            return redirect('../../')
        else:
            messages.error(request, 'Input not valid (e.g. only allow up to 50 characters).')
            return redirect(vocab_edit_view, slug, id)
    else:
        obj = Vocab.objects.get(pk=id)
        return render(request, 'vocab_edit.html', {'obj': obj})


def set_delete_view(request, slug):
    obj = VocabularySets.objects.get(slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
        messages.success(request, ('The whole vocabulary set has been deleted.'))
    return render(request, 'set_delete.html', {'object': obj})


def generate_PDF(request, slug):
    title = VocabularySets.objects.get(slug=slug)
    username = request.user
    all_item = Vocab.objects.all
    template = get_template('invoice.html')
    context = {
        'title': title,
        'username': username,
        'all_item': all_item
    }

    html = template.render(context)
    pdf = render_to_pdf('invoice.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "%s.pdf" %(title)
        content = "inline; filename=%s" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("PDF not found.")
