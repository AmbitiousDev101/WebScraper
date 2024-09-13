from bs4 import BeautifulSoup
import requests

# the public webpage url 
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"


response = requests.get(url)

if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    
    tables = soup.find_all('table', {'class': 'wikitable'})
    
    # this is for the third table (index 2), you can change the index to display a different table
    
    table = tables[2]

        
    headers = []
    for header in table.find_all('th'):
        header_text = header.get_text(strip=True)
        headers.append(header_text)

        
    rows = []
    for row in table.find_all('tr')[1:]:  #this [1:] is to skip the first row for the header
        cols = row.find_all('td') #<td> is the data cells in the current row in this loop
        
        cleaned_cols = []


        for col in cols:
            cell_text = col.get_text(strip=True)
            cleaned_cols.append(cell_text)
        cols = cleaned_cols
        rows.append(cols)

        
    print("Headers:", headers)
    for i in range(len(rows)):
        print("Row:", rows[i])
else:
    print("Failed to retrieve the webpage. The status code is:",response.status_code)
