from django.shortcuts import (get_object_or_404, render, redirect)
from django.contrib import messages
from .forms import NoteForm
from django.http import HttpResponse
from .models import Note


def index_view(request):
    context = {}
    return HttpResponse("The index View")

def detail_view(request, nid):
    note = Note.objects.get(pk=id)
    context = {"note": note}
    return HttpResponse("The detail view for " + note.title)

def create_view(request):
    context = {}
    return HttpResponse("The create view")

def update_view(request, nid):
    note = Note.objects.get(pk=id)
    context = {"note": note}
    return HttpResponse("The update view for " + note.title)

def delete_view(request, nid):
    note = Note.objects.get(pk=id)
    context = {"note": note}
    return HttpResponse("Delete view for " + note.title)

def create_view(request):
    context ={}
    form = NoteForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Note Created')
            return redirect('notes_index')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Note not created')
    context['form']= form
    return render(request, "notesapp/create_view.html", context)

def index_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    context["note_list"] = Note.objects.all()
    return render(request, "notesapp/index.html", context)    

# pass id attribute from urls
def detail_view(request, nid):
    context ={}
    # add the dictionary during initialization
    context["note"] = get_object_or_404(Note, pk=nid)
    return render(request, "notesapp/detail_view.html",context)


def update_view(request, nid):
    context ={}
    # fetch the object related to passed id
    obj = get_object_or_404(Note, id = nid)
    # pass the object as instance in form
    form = NoteForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Note Updated')
        return redirect('notes_detail', nid=nid)
    # add form dictionary to context
    context["form"] = form
    
    return render(request, "notesapp/update_view.html", context)

def delete_view(request, nid):
    # fetch the object related to passed id
    obj = get_object_or_404(Note, id = nid)
    # delete object
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Note Deleted')
    # after deleting redirect to index view
    return redirect('notes_index')    