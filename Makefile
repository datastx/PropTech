WORKDIR = $(shell pwd)
VENV_DIR = $(WORKDIR)/.venv
VENV_BIN = $(VENV_DIR)/bin


setup-local: clean-venv venv
	cp -R -p -n credentials_sample.json credentials.json || echo "credentials.json already exists"
	echo "fill out credentials.json with relevant credentials"
	echo "https://bridgedataoutput.com/myApplication/overview"

run:
	scripts/run.sh 

get-models:
	scripts/download_models.sh

	
include Makefile.venv