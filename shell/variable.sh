#!/bin/bash

VAR1='var1'
VAR2='var2'

echo $VAR1
echo $VAR1 $VAR2

array=("a1" "a2" "a3")

echo ${array[0]}
echo ${array[*]}
echo ${array[@]}
echo ${#array[@]}

filelist=($(ls))
echo ${filelist[*]}
