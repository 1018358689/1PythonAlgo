# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 16:33:57 2019

@author: 111
"""
import pandas as pd
import numpy as np
np.random.seed(1975)
l1=pd.DataFrame({'A':np.random.randn(200),'B':np.random.randn(200)})  #正态随机分布
l2=l1.cumsum()                                                 #累积和
l2.plot() 
