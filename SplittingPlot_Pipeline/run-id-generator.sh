#!/bin/bash

cd ./2024/ToSplit

files=`ls ./*.csv`

for f in $files

do
  echo $f
  python3 ./../../plant-id-generator.py $f -output ./../SplitDone/${f}_SplitDone.csv --digits 3

done

cd ./../SplitDone

newfiles=`ls ./*_SplitDone.csv`

for n in $newfiles

do 
  echo $n
  mv "$n" "${n/2split.csv_/_}"

done
