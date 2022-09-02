from email import header
from wsgiref import headers
import pandas as pd
import csv
from collections import Counter

#Prepping Data to be Analyzed
view = pd.read_csv('BallPyData.csv', header =None)
view.columns = ['0', 'Gender', 'Maturity','ID']
view.drop('0', inplace=True, axis =1)

#Count Genders
gender = Counter(view['Gender'])
print('Males:', (gender['Male']), 'or', (int(gender['Male']) / len(view)))
print('Females:', (gender['Female']), 'or', (int(gender['Female']) / len(view)))

#Count Maturity
maturity = Counter(view['Maturity'])
print('Baby/Juveniles:', (maturity['Baby/Juvenile']), 'or', (int(maturity['Baby/Juvenile']) / len(view)))
print('Subadults:', (maturity['Subadult']), 'or', (int(maturity['Subadult']) / len(view)))
print('Adults:', (maturity['Adult']), 'or', (int(maturity['Adult']) / len(view)))

#Counting both Gender/Maturity
Gm = view.value_counts(["Gender", 'Maturity'])
print('Table of Counts', Gm)
print('Total Ball Pythons:', len(view))
