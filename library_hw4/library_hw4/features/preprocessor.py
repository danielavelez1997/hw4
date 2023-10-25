#%%

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


class Preprocessor:
    def __init__(self, columns,columns_fill):
        self.columns = columns
        self.columns_fill = columns_fill

    def remove_nan_rows(self, data):
        data_cleaned = data.dropna(subset=self.columns)
        return data_cleaned
    
    def fill_nan_with_mean(self, data):
       
        # Fill NaN values with the mean values
        data_filled = data.copy()
        data_filled[self.columns_fill] = data_filled[self.columns_fill].fillna(data[self.columns_fill].mean())

        return data_filled


