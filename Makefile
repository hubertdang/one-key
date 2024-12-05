.PHONY: init test format build upload_test upload install_test install_local clean

init:
	sudo apt install -y python3.10-venv
	pip install -r requirements.txt

test:
	python -m unittest test/TestCredential.py
	python -m unittest test/TestUser.py
	python -m unittest test/TestPasswordManager.py

format:
	autopep8 --in-place --recursive .

build:
	python -m build

upload_test: build
	twine upload --repository testpypi dist/*

upload: build
	twice upload dist/*

install_test:
	pip install --index-url https://test.pypi.org/simple/ one_key

install_local: build
	pip install dist/one_key-x.y.z-py3-none-any.whl

clean:
	rm -rf dist build *.egg-info
	rm data/*

