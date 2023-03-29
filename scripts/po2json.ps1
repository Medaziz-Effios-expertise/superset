#!/bin/sh

for file in $(dir /s superset\translations\*.*);
do
  extension=${file##*.}
  filename="${file%.*}"
  if "%extension%" == "po"
  then
    .\superset-frontend\node_modules\.bin\po2json --domain superset --format jed1.x $file $filename.json
    .\superset-frontend\node_modules\.bin\prettier --write $filename.json
  fi
done
