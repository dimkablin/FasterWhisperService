help:
	clear;
	@echo "================= Usage =================";
	@echo "build 					: Install requirements."
	@echo "clean					: Remove autogenerated folders and artifacts.";
	@echo "clean-pyc           	   	: Remove python artifacts."
	@echo "clean-build            	: Remove build artifacts."


build:
	python3 -m pip install -r requirements.txt


clean: clean-build clean-pyc
	rm -rf .__pycache__
	rm -f .coverage


clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info


clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +