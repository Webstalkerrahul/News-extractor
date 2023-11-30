import pandas as pd
from pathlib import Path
from datetime import date
import xml.etree.ElementTree as ET
import requests



def extraction(company,pathnews):
    Titles=[]
    Links=[]
    
    url = 'https://news.google.com/rss/search?q='+company

    response=requests.get(url)
    root= ET.fromstring(response.content)
    for ele in root.iter():    
        if ele.tag == 'title':
            Titles.append(ele.text)
        if ele.tag == 'link':
            Links.append(ele.text)
        
    df=pd.DataFrame({'Titles':Titles,'Links':Links})
    df.to_excel(f'{pathnews}\\{company}.xlsx', sheet_name='Sheet1', index=False)

    # title
    # link
    # guid
    # pubDate
    # description
    # source
    # item

today = date.today() # capital global variables
date = today.strftime("%B %d, %Y")

company=["ndtv"]
pathnews = 'news\\'+date

#Path lib can be used
Path(pathnews).mkdir(parents=True, exist_ok=True)

for i in range(len(company)):
    extraction(company[i],pathnews)