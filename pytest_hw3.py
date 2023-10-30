
import pytest
import pandas as pd
from datetime import datetime
from hw3 import *

def test_count_simba():
    word = "Simba"
    sentence= "Simba and Nala are lions.", "I laugh in the face of danger.","Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    exp_out= 3 
    out=count_simba(word,sentence)
    assert out==exp_out


def test_get_day_month_year():
    dates = [datetime(2023, 10, 29)]
    exp_out=pd.DataFrame({'day':[29],'month':[10],'year':[2023]})
    out=get_day_month_year(dates)
    print(exp_out)
    print(out)

    assert out.shape[0]==exp_out.shape[0]
    assert out.shape[1]==exp_out.shape[1]
    assert out.day.values==exp_out.day.values
    assert out.month.values==exp_out.month.values
    assert out.year.values==exp_out.year.values

