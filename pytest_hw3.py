#%%
# from pathlab import Path 
# import sys
# parh_root=Path(__file__).parents[2]
# sys.path.append(str(path_root))


import pytest
import pandas as pd
from datetime import datetime
from hw3 import *

def test_count_simba():
    word = "Simba"
    sentence= "Simba and Nala are lions.", "I laugh in the face of danger.","Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    exp_out= 3 
    out=test_count_simba(word,sentence)
    assert out==exp_out


def test_get_day_month_year():
    dates = [datetime(2023, 10, 29)]
    exp_out=pd.DataFrame({'year':[2023],'month':[10],'day':[29]})
    out=test_get_day_month_year(dates)

    assert out==exp_out

def test_compute_distance():
    geoCoordiSets = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
    exp_out=[31.131865222052042, 157.005827868894]
    out=test_compute_distance(geoCoordiSets)

    assert out==exp_out    


def test_sum_general_int_list():
    list_1=[[2], 3, [[1,2],5]]
    exp_out=13
    out=test_sum_general_int_list(list_1)

    assert out==exp_out    
