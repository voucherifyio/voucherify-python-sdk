configure:
	pyenv install 2.7.10
	pyenv install 3.6.3
	pyenv global 2.7.10 3.6.3

make test:
	pipenv run tox
