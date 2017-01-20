import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create a variable with the URL to this tutorial
url = 'https://math.berkeley.edu/~frenkel/math53/hw.html'
# Scrape the HTML at the url
r = requests.get(url)

# Turn the HTML into a Beautiful Soup object
soup = BeautifulSoup(r.text, 'lxml')

due_dates = []
readings = []
problems = []
last_date = None

for row in soup.find_all('tr')[1:]:
    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')

    # Create a variable of the string inside 1st <td> tag pair,

    date = col[0].next.strip()
    # and append it to first_name variable
    if(date != ''):
        due_dates.append(date)
        last_date = date
    else:
        due_dates.append(last_date)

    # Create a variable of the string inside 2nd <td> tag pair,
    reading = col[1].next
    # and append it to last_name variable
    readings.append(reading)

    # Create a variable of the string inside 3rd <td> tag pair,
    prob_set = col[2].next
    # and append it to age variable
    problems.append(prob_set)


print(due_dates)
print(readings)
print(problems)