#%%
import pytest
import pandas as pd
from datetime import datetime

from hw4 import *


def test_patient_initialization():
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms)
    print(patient.name)
    assert patient.name == name
    assert patient.symptoms == symptoms

def test_add_test():
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms)    
    patient.add_test("covid", True)
    assert hasattr(patient, "test_data")
    assert patient.test_data["covid"] == True

def test_has_covid_with_covid_test():
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms) 
    patient.add_test("covid", True)
    probability = patient.has_covid()
    assert probability == 0.99

def test_has_covid_with_false_covid_test():
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms) 
    patient.add_test("covid", False)
    probability = patient.has_covid()
    assert probability == 0.01

def test_has_covid_without_covid_test():
    name = "Daniela Velez"
    symptoms = ["Fever", "Cough"]
    patient = Patient(name, symptoms) 
    probability = patient.has_covid()
    assert probability == 0.25  


def test_card_attributes():
    card = Card("Hearts", "A")
    assert card.suit == "Hearts"
    assert card.value == "A"

def test_card_string_representation():
    card = Card("Diamonds", "K")
    assert str(card) == "K of Diamonds"


def test_deck_creation():
    deck = Deck()
    assert len(deck.cards) == 52 

def test_shuffle_deck():
    deck = Deck()
    original_order = deck.cards.copy()
    deck.shuffle()
    assert deck.cards != original_order  

def test_draw_from_deck():
    deck = Deck()
    drawn_card = deck.draw()
    assert drawn_card is not None


def test_triangle_init():
    triangle= Triangle(3.0, 4.0, 5.0, 4.0)
    print(triangle.c1)
    assert triangle.base==3.0
    assert triangle.c1==4.0
    assert triangle.c2==5.0
    assert triangle.h==4.0


def test_triangle_perimeter():
    triangle = Triangle(3.0, 4.0, 5.0, 4.0)
    assert triangle.compute_perimeter()==12

def test_triangle_surface():
    triangle = Triangle(3.0, 4.0, 5.0, 4.0)
    assert triangle.compute_surface()==6
def test_rectangle_init():
    rectangle=Rectangle(2.0,3.0)
    assert rectangle.a==2
    assert rectangle.b==3

def test_rectangle_perimeter():
    rectangle = Rectangle(2.0, 3.0)
    assert rectangle.compute_perimeter()==10

def test_rectangle_surface():
    rectangle = Rectangle(2.0, 3.0)
    assert rectangle.compute_surface()==6

def test_circle_init():
    circle=Circle(4)
    assert circle.radius==4    

def test_circle_perimeter():
    circle = Circle(4.0)
    assert circle.compute_perimeter()==25.132741228718345

def test_circle_surface():
    circle = Circle(4.0)
    assert circle.compute_surface()==50.26548245743669

# def test_compute_perimeter_abstract_method():
#     with pytest.raises(NotImplementedError):
#         figure = PlaneFigure()
#         #figure.compute_perimeter()

# def test_compute_surface_abstract_method():
#     with pytest.raises(NotImplementedError):
#         figure = PlaneFigure()
#         #figure.compute_surface()
