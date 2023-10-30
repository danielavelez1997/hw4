#%%
import pytest
import pandas as pd
from datetime import datetime
from hw4 import *


def test_patient_initialization(self):
name = "Daniela Velez"
symptoms = ["Fever", "Cough"]
patient = Patient(name, symptoms)
assert patient.name == name
assert patient.symptoms == symptoms

def test_add_test():
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms)    
    patient.add_test("covid", True)
    assert hasattr(patient, "test_data")
    assert patient.test_data["covid"] == True

def test_has_covid_with_covid_test(self):
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms) 
    patient.add_test("covid", True)
    probability = patient.has_covid()
    assert probability == 0.99

def test_has_covid_with_false_covid_test(self):
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms) 
    patient.add_test("covid", False)
    probability = patient.has_covid()
    assert probability == 0.01

def test_has_covid_without_covid_test(self):
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms) 
    probability = patient.has_covid()
    assert probability == 0.15  


def test_card_attributes(self):
    card = Card("Hearts", "A")
    assert card.suit == "Hearts"
    assert card.value == "A"

def test_card_string_representation(self):
    card = Card("Diamonds", "K")
    assert str(card) == "K of Diamonds"


def test_deck_creation(self):
    deck = Deck()
    assert len(deck.cards) == 52 

def test_shuffle_deck(self):
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle()
    assert deck.cards != original_order  

def test_draw_from_deck(self):
    deck = Deck()
    drawn_card = deck.draw()
    assert drawn_card is not None

def test_draw_from_empty_deck(self):
    deck = Deck()
    while deck.cards:
        deck.draw()
    drawn_card = deck.draw()
    assert drawn_card is None
    assert "Deck is empty!" in capsys.readouterr().out  

def test_compute_perimeter_abstract_method(self):
    with pytest.raises(NotImplementedError):
        figure = PlaneFigure()
        figure.compute_perimeter()

def test_compute_surface_abstract_method(self):
    with pytest.raises(NotImplementedError):
        figure = PlaneFigure()
        figure.compute_surface()

def test_triangle_perimeter(self):
    triangle = Triangle(3.0, 4.0, 5.0, 4.0)
    assert math.isclose(triangle.compute_perimeter(), 12.0, rel_tol=1e-9)

def test_triangle_surface(self):
    triangle = Triangle(3.0, 4.0, 5.0, 4.0)
    assert math.isclose(triangle.compute_surface(), 6.0, rel_tol=1e-9)


def test_rectangle_perimeter(self):
    rectangle = Rectangle(2.0, 3.0)
    assert math.isclose(rectangle.compute_perimeter(), 10.0, rel_tol=1e-9)

def test_rectangle_surface(self):
     rectangle = Rectangle(2.0, 3.0)
    assert math.isclose(rectangle.compute_surface(), 6.0, rel_tol=1e-9)

def test_circle_perimeter(self):
    circle = Circle(4.0)
    assert math.isclose(circle.compute_perimeter(), 2 * math.pi * 4.0, rel_tol=1e-9)

def test_circle_surface(self):
    circle = Circle(4.0)
    assert math.isclose(circle.compute_surface(), math.pi * 4.0 ** 2, rel_tol=1e-9)


