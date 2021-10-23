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
    if request.method == "POST":
        edit_hero = Superhero.objects.get(pk=hero_id)
        edit_hero.name = request.POST.get('name')
        edit_hero.alter_ego = request.POST.get('alter_ego')
        edit_hero.primary_ability = request.POST.get('primary')
        edit_hero.secondary_ability = request.POST.get('secondary')
        edit_hero.catch_phrase = request.POST.get('catchphrase')
        edit_hero.save()
        return HttpResponseRedirect(reverse('superheros:detail', kwargs={'hero_id':edit_hero.id}))
    else:
        edit_hero = Superhero.objects.get(pk=hero_id)
        context = {
            'edit_hero': edit_hero
        }
        return render(request, 'superheros/edit.html', context)
   
def delete(request, hero_id):
    if request.method == "POST":
        delete_hero = Superhero.objects.get(pk=hero_id)
        delete_hero.delete()
        return HttpResponseRedirect(reverse('superheros:index'))
    else:
        delete_hero = Superhero.objects.get(pk=hero_id)
        context = {
        'delete_hero': delete_hero
        } 
        return render(request, 'superheros/delete.html', context)
   