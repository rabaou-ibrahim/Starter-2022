#!/bin/bash

if [ "$#" -ne 2 ]; then
echo "Le nombre d'arguments n'est pas bon. Veuillez en mettre 2"
fi
c=($(($1+$2)))
echo "Resultat : $c"
