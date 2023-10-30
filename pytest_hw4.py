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



