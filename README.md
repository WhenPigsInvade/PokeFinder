# PokePoacher
Pokemon finder to be used with conjuction with Poketwo.

## Table of Contents
* [Introduction](#introduction)
* [Installation](#installation)
* [Configurations](#configurations)
* [Change Log](#change-log)

## Introduction
PokePoacher will find Pokemons inside the Poketwo minigame. 

![alt text](https://imgur.com/a/9dDMpdm)

PokePoacher downloads the image and searches for the Pokemon inside the picture. Once it scans through all known Pokemons it will return a list of Pokemons that are possible matches. You can tweek the sensitivity with the threshold variable.

## Installation
Currently does NOT support threading. You will have to host your own bot if you want to use this on your own server.

Requirements:
* Python3
* OpenCV 4.5.5.62
* numpy 1.22.2 (should be automatically installed with OpenCV)
* discordpy 1.6.0

## Configurations

You can set threshold for Pokemon detection inside `find.py`

You can also run find.py directly from the console. Will search for Pokemon inside `pokemon.jpg`

## Change log



