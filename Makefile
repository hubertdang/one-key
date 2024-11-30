.PHONY: init test format

init:
	pip install -r requirements.txt

test:
	python -m unittest test/TestCredential.py
	python -m unittest test/TestUser.py
	python -m unittest test/TestPasswordManager.py

format:
	autopep8 --in-place --recursive .

