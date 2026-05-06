"""Tests for the sample application."""
import pytest
from src.app import greet, add


def test_greet_returns_message():
    result = greet("Nexon")
    assert "Nexon" in result
    assert "Welcome" in result


def test_greet_raises_on_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_negative_numbers():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 5) == 5
