from bs4 import BeautifulSoup
import requests
import json 

url = input("profiles.doe.mass.edu/statereport/mcas.aspx")

r  = requests.get("http://profiles.doe.mass.edu/statereport/mcas.aspx")

data = r.text

soup = BeautifulSoup(data)

# Get Headers
headers = []
for tableHeader in soup.find_all('th'):
    headers.append(tableHeader.getText())

districtData = []

columnsCount = len(headers)

def createDistrictData(headers, row):
    return dict(zip(headers, row))
    

for rows in soup.find_all('tr'):
    row = []
    for cell in rows.find_all('td'):
        print(cell.getText())
        row.append(cell.getText())
    if len(row) == columnsCount:
        districtData.append(createDistrictData(headers, row))

with open('./scrapedData/data.json', 'w') as fp:
    json.dump(districtData, fp)
