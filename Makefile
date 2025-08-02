#===================== Notes ============================
## To source venv:
## >> source ./.venv/bin/activate


#===================== Categories =======================
.phony: all install venv_create


#===================== Variables ========================


#===================== Recipes ==========================
all:

install:
	pip install -e .

venv_create:
	pyenv local 3.10
	python -m venv .venv

