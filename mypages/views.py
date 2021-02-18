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
    all_item = VocabularySets.objects.all #Queryset all VocabularySet objects to be passed into home template
    details = Vocab.objects.all #Queryset all Vocab objects to be passed into home template
    if request.method == 'POST':
        form = TitleForm(request.POST or None) #TitleForm to be populated upon POST request
        if form.is_valid(): #method that validates form
            title = form.save(commit=False)
            title.username = request.user #Username field for the title object is the current user in request
            title.save()
            return redirect(home)
        else:
            messages.error(request, 'Input not valid.') #Error message displayed in html
            return redirect(home)
    else: 
        if request.user.is_authenticated: #Django's built-in method that checks whether user is logged in (authorisation protocol)
            count = VocabularySets.objects.filter(username=request.user).count() 
            #Counts the amount of sets in VocabularySets model that matches the given user parameter
        else:
            count = 0 #count is 0 if user is not authenticated (just in case)
        return render(request, 'home.html', {'all_item': all_item, 'details': details, 'count': count}) 
        #Variables passed into home template through a dictionary to be displayed.


def about(request):
    return render(request, 'about.html', {})


def create(request, slug):
    table = VocabularySets.objects.get(slug=slug)   #Queryset the slug object from VocabularySets model
    all_item = Vocab.objects.all
    
    if 'word' in request.POST: #Checks for POST method when button is pressed submitting 'word' value (see create template)
        form = VocabForm(request.POST or None)
        if form.is_valid():
            f = form.save(commit=False)
            w = request.POST.get('word')
            f.p = pinyin_jyutping_sentence.pinyin(w) #p field of the word is assigned to the pinyin generated
            trans = Translator()
            e = trans.translate(w) #Google translate method
            f.eng = e.text #eng field is assigned to Google translated text
            f.title = table #title field is assigned to table variable defined earlier (slug object)
            form.save()
            context = {'all_item': all_item, 'table': table}
            return render(request, 'create.html', context)
        else:
            messages.error(request, 'Input not valid (e.g. can only accept chinese and up to 20 characters).') #error handling message
            return redirect(create, slug)
    return render(request, 'create.html', {'table': table, 'all_item': all_item})   

def star(request, slug, id):
    obj = Vocab.objects.get(pk=id)
    obj.star = True #change star field of Vocab to True
    obj.save()
    return redirect(create, slug)

def unstar(request, slug, id):
    obj = Vocab.objects.get(pk=id)
    obj.star = False #change star field of Vocab to False
    obj.save()
    return redirect(create, slug)


def vocab_delete_view(request, slug, id):
    obj = Vocab.objects.get(pk=id) #get Vocab object currently deleting by primary key passed in function during request
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    messages.success(request, ('Vocabulary has been deleted.')) #success message displayed in create template
    return render(request, 'vocab_delete.html', {'object': obj})


def vocab_edit_view(request, slug, id):
    if request.method == 'POST':
        obj = Vocab.objects.get(pk=id) #get vocab object by primary key passed in the function during request
        form = EditForm(request.POST or None, instance=obj) #object to be edited in EditForm
        if form.is_valid():
            new_obj = form.save(commit=False)
            new_obj.eng = obj.eng #replace with new edited object
            new_obj.save()
            return redirect('../../')
        else:
            messages.error(request, 'Input not valid (e.g. only allow up to 50 characters).') #error message handling
            return redirect(vocab_edit_view, slug, id)
    else:
        obj = Vocab.objects.get(pk=id)
        return render(request, 'vocab_edit.html', {'obj': obj})


def set_delete_view(request, slug):
    obj = VocabularySets.objects.get(slug=slug) #get object by slug parameter from VocabularySets model
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
        messages.success(request, ('The whole vocabulary set has been deleted.')) #success message
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
