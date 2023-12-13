from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Wine, Country

from .forms import DrinkingForm

# CBV Wine Views
class WineCreate(CreateView):
    model = Wine
    fields = ['name', 'color', 'description', 'age']

class WineUpdate(UpdateView):
    model = Wine
    fields = ['name', 'description', 'age']

class WineDelete(DeleteView):
    model = Wine
    success_url = '/wines'

#country views
class CountryList(ListView):
    model = Country

class CountryDetail(DetailView):
    model = Country

class CountryCreate(CreateView):
    model = Country
    fields = '__all__'

class CountryUpdate(UpdateView):
    model = Country
    fields = ['name', 'region']

class CountryDelete(DeleteView):
    model = Country
    success_url = '/countries/'

# regular views
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wines_index(request):
    wines = Wine.objects.all()
    return render(request, 'wines/index.html', {'wines': wines})

def wines_detail(request, wine_id):
    wine = Wine.objects.get(id=wine_id)
    id_list = wine.toys.all().values_list('id')
    countries_doesnt_have_wine = Country.objects.exclude(id__in=id_list)
    drinking_form = DrinkingForm()
    return render(request, 'wines/detail.html', {'wine':wine, 'drinking_form': drinking_form, 'countries': countries_doesnt_have_wine})

def assoc_country(request, wine_id, country_id):
    wine = Wine.objects.get(id=wine_id)
    wine.countries.add(country_id)
    return redirect('detail', wine_id=wine_id)

def add_drinking(request, wine_id):
    form = DrinkingForm(request.POST)
    if form.is_valid():
        new_drinking = form.save(commit=False)
        new_drinking.wine_id = wine_id
        new_drinking.save()
    return redirect('detail', wine_id=wine_id)
