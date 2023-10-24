#%%

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score


class Model():
    def __init__(self, feature_columns, target_column, params=None):
        print('initializing class')
        self.__feature_columns = feature_columns
        self.__target_column = target_column
        self.__params = params
        if self.__params != None:
            self.model = RandomForestClassifier(n_estimators=self.__params['n_estimators'], random_state=42)
        else:
            self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    def train(self, train_data):
        self.model.fit(train_data[self.__feature_columns], train_data[self.__target_column])        

    def predict(self, df):
        return self.model.predict_proba(df[self.__feature_columns])[:,1]

    def get_accuracy(self, y_test, y_pred):
        return roc_auc_score(y_test, y_pred)



