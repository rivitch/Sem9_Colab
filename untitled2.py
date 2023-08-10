# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lJGT6z1TnMUetqyYBeyy1eDp7ufUVS_c
"""



"""Задача 40:  Работать с файлом california_housing_train.csv, который находится в папке
sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""

import pandas as pd

df = pd.read_csv("sample_data/california_housing_train.csv")

df[df['population'] <= 500]['median_house_value'].mean()

"""1 вариант"""

df[pd.read_csv("sample_data/california_housing_train.csv")['population'] <= 500]['median_house_value'].mean()

"""2 вариант"""