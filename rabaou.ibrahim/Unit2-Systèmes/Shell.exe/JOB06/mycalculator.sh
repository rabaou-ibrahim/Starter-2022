#!/bin/bash

a=$1
b=$3
if [ $2 == + ]; then
c=$(($1+$3))
echo "$c"
fi
if [ $2 == - ]; then
c=$(($1-$3))
echo "$c"
fi
if [ $2 == * ]; then
c=$(($1*$3))
echo "$c"
fi
if [ $2 == / ]; then
c=$expr$(($1/$3))
echo "$c"
fi