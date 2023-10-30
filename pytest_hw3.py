
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

def test_compute_distance():
    geoCoordiSets = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
    exp_out=[31.131865222052042, 157.005827868894]
    out=compute_distance(geoCoordiSets)

    assert out==exp_out    

def test_sum_general_int_list():
    list_1=[[2], 3, [[1,2],5]]
    exp_out=13
    out=sum_general_int_list(list_1)

    assert out==exp_out