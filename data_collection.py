from requests import get
import pandas as pd

def getData(keyword):
    baseUrl = 'https://justjoin.it/api/offers/search?'
    
    url = f'{baseUrl}keywords[]={keyword}'
    resInBytes = get(url)
    resInJson = resInBytes.json()
    
    return pd.DataFrame.from_dict(resInJson)

df = getData('frontend')
df.to_csv('frontend_raw_data.csv')
