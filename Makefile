.PHONY: tests
tests:
	python -m unittest discover --start-directory tests --top-level-directory .
