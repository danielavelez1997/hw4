#%%

import pandas as pd
from sklearn.model_selection import train_test_split
class split_data:

    def __init__(self,file_path,test_size,random_state):
        self.file_path=file_path
        self.test_size=test_size
        self.random_state=random_state
        self.train_data=None
        self.test_data=None

    def load_data(self):
        data = pd.read_csv(self.file_path)
        train_data, test_data = train_test_split(data, test_size=self.test_size, random_state=self.random_state)
        self.train_data=train_data
        self.test_data=test_data

    def get_train_data(self):
        if self.train_data is None:
            raise ValueError("Train data not loaded.")
        return self.train_data

    def get_test_data(self):
        if self.test_data is None:
            raise ValueError("Test data not loaded")
        return self.test_data
        


#%%

class RemoveNaN:
    def __init__(self, columns):
        self.columns = columns

    def remove_nan_rows(self, data):
        data_cleaned = data.dropna(subset=self.columns)
        return data_cleaned



# %%

import pandas as pd

class fill_Nan:
    def __init__(self, columns_fill):
        self.columns_fill = columns_fill
       
    def fill_nan_with_mean(self, data):
       
        # Fill NaN values with the mean values
        data_filled = data.copy()
        data_filled[self.columns_fill] = data_filled[self.columns_fill].fillna(data[self.columns_fill].mean())

        return data_filled


# %%
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


