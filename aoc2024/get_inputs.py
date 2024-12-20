from pathlib import Path


def get_inputs(filename):
    input_path = Path(__file__).parent.parent / 'inputs' / '2024' / filename
    return input_path.read_text().splitlines()
