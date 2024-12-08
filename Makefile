.PHONY: init test format build clean upload_test upload install_test install_local upgrade_test

init:
	sudo apt install -y python3.10-venv
	pip install -r requirements.txt

test:
	python -m unittest test/TestCredential.py
	python -m unittest test/TestUser.py
	python -m unittest test/TestPasswordManager.py

format:
	autopep8 --in-place --recursive .

build: clean
	python -m build

clean:
	rm -rf dist build *.egg-info
	rm -rf one_key/data/*

upload_test:
	twine upload --repository testpypi dist/* --verbose

upload: build
	twice upload dist/*

install_test:
	pip install --index-url https://test.pypi.org/simple/ one_key

install_local: build
	pip install dist/one_key-*.whl --force-reinstall

upgrade_test:
	pip install --index-url https://test.pypi.org/simple/ --upgrade one_key

