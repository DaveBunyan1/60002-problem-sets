import tempfile
import os
from problem_set_1.ps1a import load_cows


def write_temp_file(contents):
    """Create a temporary file with given contents and return its filename."""
    tmp = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
    tmp.write(contents)
    tmp.close()
    return tmp.name


def test_valid_file():
    filename = write_temp_file("Betsy,34\nMary,42\n")
    assert load_cows(filename) == {"Betsy": 34, "Mary": 42}
    os.remove(filename)


def test_blank_file():
    filename = write_temp_file("")
    assert load_cows(filename) == {}
    os.remove(filename)


def test_malformed_lines():
    contents = (
        "Betsy,34\n"
        "InvalidLine\n"
        "Mary,notanumber\n"
        "NoComma 42\n"
        ",35\n"
        "GoodCow,50\n"
    )
    filename = write_temp_file(contents)
    result = load_cows(filename)
    assert result == {"Betsy": 34, "GoodCow": 50}
    os.remove(filename)


def test_missing_file():
    # create a *name* that doesn't exist
    missing = tempfile.gettempdir() + "/definitely_missing.txt"
    if os.path.exists(missing):
        os.remove(missing)

    assert load_cows(missing) == {}
