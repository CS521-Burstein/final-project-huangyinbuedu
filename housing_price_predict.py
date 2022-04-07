import requests
import csv
import pandas as pd
url = 'https://raw.githubusercontent.com/bursteinalan/Data-Sets/master/Housing/House%20Prediction%20Data.csv'
r = requests.get(url, allow_redirects=True)
open('downloaded.csv', 'wb').write(r.content)
data = pd.read_csv('downloaded.csv')

