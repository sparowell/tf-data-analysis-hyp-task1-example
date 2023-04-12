import pandas as pd
import numpy as np
from scipy import stats as st

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    _, p = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
    return p<0.05
