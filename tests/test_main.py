import pytest
from main import country_sort
import os
import csv

# Фікстура для тимчасового вхідного файлу
@pytest.fixture
def input_file(tmpdir):
    data = [["Country", "Area", "Population"],
            ["Ukraine", "603628", "44134645"],
            ["Japan", "377973", "126919566"],
            ["USA", "9629091", "331443284"]]
    input_file = tmpdir.join("input.txt")
    with open(input_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    return str(input_file)

# фікстура для тимчасового файлу результату
@pytest.fixture
def output_file(tmpdir):
    return str(tmpdir.join("output.txt"))

def test_country_sort(input_file, output_file):
    country_sort(input_file, output_file)
    with open(output_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    assert data[6][0] == "USA"  # перевіряємо по рядках (але оскільки це індекси, то номер рядка мінус 1)
    assert data[20][0] == "Ukraine"  # так саме, у файлі має бути на 21 рядку
