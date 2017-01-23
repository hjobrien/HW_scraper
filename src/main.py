import requests
from bs4 import BeautifulSoup
import sqlite3
import random



def date_to_num(due_date):
    #17191: Jan 25 2017

    due_date = due_date[:due_date.index(',')]
    due_string = due_date.split(' ')

    month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9,
                 'Oct': 10, 'Nov': 11, 'Dec': 12}

    due_string[0] = month_map[due_string[0]]

    date_list = [int(num) for num in due_string]

    days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    days_since = date_list[1] #get days
    for i in range(date_list[0] - 1): #loop through past months
        days_since += days_in_month[i]

    days_since -= 25 # get difference to january 25th (so 25 days since the start of the year)
    return 17191 + days_since+8 #add the delta of the days to the known day number (17191) which corresponds to jan 25th





# params = (30111307098, 0, 0, 0, None, None, 0, None, 17191, 0, None, 0, None,
#           'notification ID', 1, None, 43200.0, 30110954415, 1, None, 'Test', None)

def add_to_assignments(params):
    conn = sqlite3.connect('/Users/Hank/Library/Group Containers/YJW8D95H2C.com.istudiezteam/Library/Application Support/main.db')
    # conn = sqlite3.connect('main copy.db') #temp for testing
    c = conn.cursor()
    notes = (params[7],)
    if(len([1 for row in c.execute('SELECT * FROM assignments where notes = ? and DEL = 0' , notes)]) == 0):
        c.execute("INSERT INTO assignments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  params)

    conn.commit()

    for row in c.execute('SELECT * FROM assignments'):
        print(row)

    conn.close()



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
    reading = col[1].next.strip()
    # and append it to last_name variable
    readings.append(reading)

    # Create a variable of the string inside 3rd <td> tag pair,
    prob_set = col[2].next.strip()
    # and append it to age variable
    problems.append(prob_set)
#
# print(due_dates)
# print(readings)
# print(problems)
for problem_set, due_string, reading in zip(problems, due_dates, readings):
    if(problem_set != ''):  #some assignments are posted but without question numbers
        uid = int(random.random() * 1000000)
        is_new = 0
        is_local = 0
        del_val = 0
        server_uid = None
        old_server_uid = None
        notification_day = 0
        notes = problem_set
        due_date = date_to_num(due_string)
        completion_date = 0
        weight_uid = None
        complete = 0
        partners = None
        notification_uid = 'notification ID'
        priority = 1
        earned_points = None
        notification_time = 43200.0
        course_uid = 30110954415 #course ID for math 53
        notify = 1
        total_points = None
        name = reading + 'Test'
        completion_time_offset = None

        params = (uid, is_new, is_local, del_val, server_uid, old_server_uid, notification_day, notes, due_date,
                  completion_date, weight_uid, complete, partners, notification_uid, priority, earned_points,
                  notification_time, course_uid, notify, total_points, name, completion_time_offset)

        add_to_assignments(params)





