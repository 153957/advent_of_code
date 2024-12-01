.PHONY: puzzle
puzzle:
	python -m aoc$(year).day$(day)

.PHONY: tests
tests:
	python -m unittest

