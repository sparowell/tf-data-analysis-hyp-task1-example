import pandas as pd
import numpy as np
from scipy import stats as st

chat_id = 654929803 # Ваш chat ID, не меняйте название переменной

def solution(m1: int, 
             n1: int, 
             m2: int, 
             n2: int) -> bool:
    p1 = m1/n1
    p2 = m2/n2
    df = n1 + n2 - 2

    var1 = p1*(1-p1)
    var2 = p2*(1-p2)
    sme = var1/n1 + var2/n2

    t = (p1-p2)/np.sqrt(sme)
    p = st.t.cdf(t,df)
    return p<0.05
