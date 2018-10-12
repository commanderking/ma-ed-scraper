from bs4 import BeautifulSoup
import requests
import json 

r  = requests.get("http://profiles.doe.mass.edu/statereport/mcas.aspx")
data = r.text
soup = BeautifulSoup(data)

headers = []
for tableHeader in soup.find_all('th'):
    headers.append(tableHeader.getText())


columnsCount = len(headers)

def createDistrictData(headers, row):
    return dict(zip(headers, row))

outputFilename = "mcas"
for selectedOption in soup.find_all('option', selected=True):
    outputFilename = outputFilename + "_" + selectedOption.getText().replace(" ", "_").lower()
    print(selectedOption)
print(outputFilename)

districtData = []
for rows in soup.find_all('tr'):
    row = []
    for cell in rows.find_all('td'):
        row.append(cell.getText())
    if len(row) == columnsCount:
        districtData.append(createDistrictData(headers, row))

outputPath = './scrapedData/' + outputFilename + '.json'

with open(outputPath, 'w') as fp:
    json.dump(districtData, fp, sort_keys=True, indent=4)