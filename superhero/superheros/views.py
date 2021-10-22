from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heros = Superhero.objects.all()
    context = {
        'all_heros': all_heros
    }
    return render(request, 'superheros/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    } 
    return render(request, 'superheros/detail.html', context)

def create(request):
    if request.method == "POST":
        # save the form contents
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheros:index'))
    else:
        return render(request, 'superheros/create.html')

def edit(request, hero_id):
    edit_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'edit_hero': edit_hero
    } 
    if request.method == "POST":
        # save the form contents
        # return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        edit_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        edit_hero.save()
        return HttpResponseRedirect(reverse('superheros:index'))
    else:
        return render(request, 'superheros/edit.html', context)
   