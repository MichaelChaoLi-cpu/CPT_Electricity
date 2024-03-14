# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:06:24 2024

@author: Li Chao
"""

from glob import glob
import pandas as pd

DoneFile = pd.read_csv('Data/DoneFromBQ20240216.csv')
DoneFile = DoneFile['nake_name'].to_list()

file_list = glob('AnnualReport10K/*.pdf')
file_list = [file_name.replace('\\', '/') for file_name in file_list]

file_need_run = [file_name for file_name in file_list if file_name not in DoneFile]



