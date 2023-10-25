#%%

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

from abc import ABC, abstractmethod

class FeatureTransformer(ABC):
    @abstractmethod
    def transform(self, data):
        pass

class GenderTransformer(FeatureTransformer):
    def __init__(self, gender):
        self.gender = gender

    def transform(self, data):
        data['gender'] = data['gender'].map(self.gender)
        return data

class EthnicityTransformer(FeatureTransformer):
    def __init__(self, ethnicity):
        self.ethnicity = ethnicity

    def transform(self, data):
        data['ethnicity'] = data['ethnicity'].map(self.ethnicity)
        return data
