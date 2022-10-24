#!/bin/bash

if [ $1 == "Hello" ]; then
echo "Bonjour, je suis un script"
fi
if [ $1 == "Bye" ]; then
echo "Au revoir et bonne journée"
fi
if [ "$#" -ne 1 ]; then
echo "
(Vous n'avez droit qu'à 2 arguments !)"
fi