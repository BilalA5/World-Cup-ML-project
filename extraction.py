#Extraction Process
import numpy as np
import pandas as pd

data = pd.read_csv('Fifa_world_cup_matches.csv')
#print(data.head()) # 5 x 88

#Clean Data for model

#Posession Data : 42% -> 42

data['possession team1'] = data ['possession team1'].str.replace('%', '').astype(float)

#Date to UTC
data['date'] = pd.to_datetime(data['date'])

#Fix hour data colon and spaces
data['hour'] = data['hour'].str.replace(':', '').astype(int)

#Rename columns : completed, line, breakstream1, 

data = data.rename(columns={
    'completed line breaksteam1': 'completed line breaks team1',
    'completed line breaksteam2': 'completed line breaks team2',
    'attempted defensive line breaks team1': 'attempted defensive line breaks team1',
    'attempted defensive line breaks team2': 'attempted defensive line breaks team2',
    'completed defensive line breaksteam1': 'completed defensive line breaks team1',
    'completed defensive line breaksteam2': 'completed defensive line breaks team2',
})




