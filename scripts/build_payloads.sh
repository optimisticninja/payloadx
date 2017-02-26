#!/bin/sh

cd crafted_payloads

for payload in `find . -name *.py`; do
	../scripts/obfuscate_python.sh $payload > "$payload.minified"
done

