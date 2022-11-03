from django.shortcuts import render
import requests
import pprint
import math
import random

# Create your views here.
def home(request):
    allPokemon=[]
    random_num= random.randint(1,152)
    my_pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_num}")
    pokemon=my_pokemon.json()
    def get_by_type(type):
        answer={}
        random2=random.randint(1,20)
        other_poke=requests.get(f"https://pokeapi.co/api/v2/type/{type}/")
        other_poke=other_poke.json()
        answer['name']=other_poke["pokemon"][random2]["pokemon"]["name"]
        newImg=requests.get(other_poke["pokemon"][random2]["pokemon"]["url"])
        newImg=newImg.json()
        newImg=newImg["sprites"]["front_default"]
        answer["img"]=newImg
        return answer
    for i in range(5):
        new_poke=get_by_type(pokemon["types"][0]["type"]["name"])
        allPokemon.append(new_poke)
    
    data={
        "img":pokemon["sprites"]["front_default"],
        "name":pokemon["name"],
        "type":pokemon["types"][0]["type"]["name"],
        "rest":allPokemon
    }
    response= render(request, "pages/home.html", data)
    return response