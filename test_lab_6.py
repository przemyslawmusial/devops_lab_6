import pytest
import requests


def test_czyEleganckiResponseCodePoleciPrzyOdejmowaniu():
    data = {"a": 2.5, "b": 3.5}
    response = requests.post("http://127.0.0.1:8000/odejmowanie", json=data)

    assert response.status_code == 200


def test_czyEleganckiResponseCodePoleciPrzyMnożeniu():
    data = {"a": 2.5, "b": 3.5}
    response = requests.post("http://127.0.0.1:8000/mnozenie", json=data)

    assert response.status_code == 200


def test_czyEleganckiResponseCodePoleciPrzyDzieleniu():
    data = {"a": 2.5, "b": 3.5}
    response = requests.post("http://127.0.0.1:8000/dzielenie", json=data)

    assert response.status_code == 200

def test_czyEleganckiResponseCodePoleciPrzyDzieleniuPrzezZero():
    data = {"a": 2.5, "b": 0}
    response = requests.post("http://127.0.0.1:8000/dzielenie", json=data)

    assert response.status_code == 400
