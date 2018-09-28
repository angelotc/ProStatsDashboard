import requests
import urllib.parse
import json
import datetime as dt
import pandas as pd
#dt.date.today().ctime()

allProsURL =  'https://www.trackingthepros.com/d/list_players'
response = requests.get(allProsURL)
json_object = response.json()

df = pd.DataFrame(columns=('Pro Name',
                           'Team',
                           'Server',
                           'AccName',
                           'CurRank',
                           'GetTime'))

for data in json_object['data']:
    count=1
    proID = data['DT_RowId']
    ProURL = 'https://www.trackingthepros.com/d/list_accounts?id={}'.format(proID)
    response = requests.get(ProURL)
    json_object2 = response.json()
    ProName = data['name']
    TeamName = data['team']
    print('\nTeam: {}'.format(ProName))
    print('Name: {}'.format(TeamName))
    for item in json_object2['data']:
        df = df.append({'Pro Name' : ProName,
                   'Team' : TeamName,
                   'Server' : item['server'] ,
                   'AccName' : item['name'] ,
                   'CurRank' : item['rankCombined'],
                   'GetTime':dt.date.today().ctime()},
                  ignore_index=True)
        print("   {} Account #{} : {} ".format(item['server'],count,item['name']))
        print("   Rank : {}  \n".format(item['rankCombined']))
        count+=1
        print(df.head())


df.to_csv(r'C:\Users\angeloc\Desktop\trackingthepros.csv')
