#!/bin/sh

cd crafted_payloads
target_files="`find . -name *.py`"

for file in $target_files; do
	ofile="${file}z"
	echo "Obfuscating $file to $ofile..."
	pyminifier  --obfuscate --gzip --pyz=$ofile $file
done

