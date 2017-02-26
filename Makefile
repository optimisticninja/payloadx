all: craft-payloads

craft-payloads:
	./payloads/rshellgenerator.py
	./scripts/obfuscate_python.sh
