from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Predator
from .forms import SightingForm


class FinchCreate(CreateView):
    model = Finch
    fields = ['commonName', 'species', 'description', 'iocSequence']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['species','description', 'iocSequence']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    id_list = finch.predators.all().values_list('id')
    predators_finch_doesnt_have = Predator.objects.exclude(id__in=id_list)
    sighting_form = SightingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'sighting_form': sighting_form,
         'predators': predators_finch_doesnt_have
    })

def add_sighting(request, finch_id):
    form = SightingForm(request.POST)
    #validate the form
    if form.is_valid():
        # dont save the form to database until
        # has finch_id assigned
        new_sighting = form.save(commit=False)
        new_sighting.finch_id = finch_id
        new_sighting.save()
    return redirect('detail', finch_id=finch_id)

class PredatorList(ListView):
  model = Predator

class PredatorDetail(DetailView):
  model = Predator

class PredatorCreate(CreateView):
  model = Predator
  fields = '__all__'

class PredatorUpdate(UpdateView):
  model = Predator
  fields = ['commonName', 'description']

class PredatorDelete(DeleteView):
  model = Predator
  success_url = '/predators/'

def assoc_predator(request, finch_id, predator_id):
    Finch.objects.get(id=finch_id).predators.add(predator_id)
    return redirect('detail', finch_id=finch_id)