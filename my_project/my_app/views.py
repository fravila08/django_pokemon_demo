from django.shortcuts import render
import requests
import pprint
import math
import random

# Create your views here.
def home(request):
    #this will hold an array of 5 pokemon
    allPokemon=[]
    #creates a random number
    random_num= random.randint(1,152)
    #lines 14-15 makes an API call and turns the reponse to json readable.
    my_pokemon= requests.get(f"https://pokeapi.co/api/v2/pokemon/{random_num}")
    pokemon=my_pokemon.json()
    #This function will search by type and return a pokemons name and img in a dictionary.
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
    #we will call the function get by type 5 times and append the result to the allPokemon list
    for i in range(5):
        new_poke=get_by_type(pokemon["types"][0]["type"]["name"])
        allPokemon.append(new_poke)
    
    data={
        # lines 35-37 will hold the original pokemons picture, name, and type
        "img":pokemon["sprites"]["front_default"],
        "name":pokemon["name"],
        "type":pokemon["types"][0]["type"]["name"],
        #holds a list of dictionaries holding name and imgurl
        "rest":allPokemon
    }
    response= render(request, "pages/home.html", data)
    return response