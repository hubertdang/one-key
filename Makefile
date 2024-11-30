.PHONY: test

test:
	python -m unittest test/TestCredential.py
	python -m unittest test/TestUser.py
	python -m unittest test/TestPasswordManager.py

