import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Time, Pokemon
from .forms import TimeForm, PokemonForm

def home(request):
    return render(request, 'team_builder/home.html')

def lista_times(request):
    times = Time.objects.all()
    if not times:
        return render(request, 'team_builder/sem_time.html')
    return render(request, 'team_builder/lista_times.html', {'times': times})

def criar_time(request):
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TimeForm()
    return render(request, 'team_builder/criar_time.html', {'form': form})

def detalhe_time(request, time_id):
    time = get_object_or_404(Time, id=time_id)
    pokemons = time.pokemons.all()
    return render(request, 'team_builder/detalhe_time.html', {'time': time, 'pokemons': pokemons})

def editar_time(request, time_id):
    time = get_object_or_404(Time, id=time_id)
    if request.method == 'POST':
        form = TimeForm(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return redirect('detalhe_time', time_id=time.id)
    else:
        form = TimeForm(instance=time)
    return render(request, 'team_builder/editar_time.html', {'form': form, 'time': time})

def excluir_time(request, time_id):
    time = get_object_or_404(Time, id=time_id)
    time.delete()
    return redirect('lista_times')

def adicionar_pokemon(request, time_id):
    time = get_object_or_404(Time, id=time_id)
    if time.pokemons.count() >= 6:
        return redirect('detalhe_time', time_id=time.id)

    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.time = time
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon.nome.lower()}')
            if response.status_code == 200:
                data = response.json()
                tipos = [t['type']['name'] for t in data['types']]
                pokemon.tipo = '/'.join(tipos)
                pokemon.imagem = data['sprites']['front_default']
            else:
                pokemon.tipo = "Desconhecido"
                pokemon.imagem = ""
            pokemon.save()
            return redirect('detalhe_time', time_id=time.id)
    else:
        form = PokemonForm()
    return render(request, 'team_builder/adicionar_pokemon.html', {'form': form, 'time': time})

def detalhe_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    return render(request, 'team_builder/detalhe_pokemon.html', {'pokemon': pokemon})

def excluir_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    time_id = pokemon.time.id
    pokemon.delete()
    return redirect('detalhe_time', time_id=time_id)