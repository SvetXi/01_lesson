import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# Тесты для trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("     hello", "hello"),
    (" space ", "space "),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "skypro"),
    ("", ""),
    ("no_spaces", "no_spaces"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# Тесты для contains

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"),
    ("hello world", " "),
    ("python", "t"),
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "U"),
    ("hello world", "z"),
    ("python", "3"),
])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False

# Тесты для delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", "l", "heo word"),
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "z", "SkyPro"),
    ("", "a", ""),
    ("python", "", "python"),
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
