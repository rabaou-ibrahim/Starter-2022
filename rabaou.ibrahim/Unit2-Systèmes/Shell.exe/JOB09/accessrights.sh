#!/bin/bash

cut -d, -f2 Shell_Userlist.csv > Prenoms.txt   #Le but ici est de lister les noms des utilisateurs pour ensuite utiliser la fonction sudo adduser pour les ajouter.
tail -n 10 Prenoms.txt > Prenoms_tail.txt      #J'ai fait un tail car la 1ere ligne avait "Prenom" qui ne fait évidemment pas partie de ce que l'on cherche  
      while read line; do
      sudo adduser;
      done < Prenoms.txt
grep 'Admin' 'Shell_Userlist.csv' > Admins.txt #On répertorie les admins dans un nouveau fichier
      cut -d, -f5 Admins.txt
      cat Admins.txt