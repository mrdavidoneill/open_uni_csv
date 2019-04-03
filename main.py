########################################################################################################################
#                                              INSTRUCTIONS FOR USE                                                    #
########################################################################################################################
#        Download (due to login complications if online) the html page and place inside "modules" folder               #
#        Change "module name" below to the name of the html file                                                       #
#        Run this file                                                                                                 #
#        A csv file will be created inside "csvs" folder which you can then import into your chosen calendar app       #
#                                                                                                                      #
########################################################################################################################
#                                            FOLDER STRUCTURE NEEDED                                                   #
########################################################################################################################
#                                 modules            csvs           main.py                                            #
#                            (htmls)            (exported csvs)                                                        #
########################################################################################################################
#                                                  USER INPUT                                                          #
########################################################################################################################

# Change this module name to whichever module you are converting to csv #
module_name = "TM111-19D"

# Optional - change start and end times
start_time = "12:00 AM"
end_time = "11:59 PM"

########################################################################################################################

# Uses csv module to output file into csv format that can be imported by calendar apps
import csv

# Uses regex matching for getting dates
import re

# Uses datetime for getting the correct year when the months pass through to another year
from datetime import datetime

# BeautifulSoup parses html data into something manageable for Python
from bs4 import BeautifulSoup

# This creates the module path name
module = "modules/" + module_name + ".html"

# Opens and closes the html file we have downloaded and parses the data we need to "soup" variable
with open(module) as fp:
    soup = BeautifulSoup(fp)

# Finds our chosen div elements from the HTML data
dates = soup.find_all("div", class_="oustudyplan-date")
names = soup.find_all("h3", class_="sectionname")
start_year_div = soup.find("div", class_="block-beforestart-date")

# Finds our start year
start_year = start_year_div.strong.contents[0]  # gets content of the "strong" tag inside "block-beforestart-date" div

# Converts start_year text to number
year_pattern = "20\d\d"
year = re.findall(year_pattern,start_year)[0]   # Findall returns a list. So we target the 1st index only

# Converts dates to "start date" and "end date"
pattern = "[\w]+"   # Search for letters & numbers characters only

# Make two lists to save our start dates & end dates
start_dates = []
end_dates = []

# Make our start & end dates and append them to the two lists above
for date in dates:
    date_string = ''.join(date.contents)  # converts from list to string
    date_stripped = re.findall(pattern,date_string)
    if len(date_stripped) == 3:
        start_date = date_stripped[0] + " " + date_stripped[2]
        end_date = date_stripped[1] + " " + date_stripped[2]
    else:
        start_date = date_stripped[0] + " " + date_stripped[1]
        end_date = date_stripped[2] + " " + date_stripped[3]
    start_dates.append(start_date)
    end_dates.append(end_date)

def convert_to_date_obj(arr):
    """Converts items in a list, to date time objects.
    Input format = '2019 6 April'
    Output format = 06/04/2019 """
    global year
    for index, date in enumerate(arr):
        if type(arr[0]) != unicode and datetime.strptime(year + " " + date, "%Y %d  %B") < arr[0]:
            year = str(int(year) + 1)
        date_obj = datetime.strptime(year + " " + date, "%Y %d  %B")
        arr[index] = date_obj

    # Convert start dates strings into datetime objects
convert_to_date_obj(start_dates)
# Convert end dates strings into datetime objects
convert_to_date_obj(end_dates)

# Removes the initial "Welcome" element on the HTML page
names = names[1:]

# Prepare table to put our elements
table = []
total_rows = len(names) # Number of rows equals the amount of names we have
total_cols = 6  # Columns are:  Subject, Start Date, End Date, Start Time, End Time, All Day Event
for row in range(total_rows): table += [[0]*total_cols]    # Creates our empty table

# Organises the elements into our table
row_num = 0
col_num = 0

for num in range(total_rows):

    table[row_num][col_num] = ''.join(names[num].contents)  # converts from list to string
    col_num += 1
    table[row_num][col_num] = start_dates[num].strftime("%m/%d/%Y")
    col_num += 1
    table[row_num][col_num] = end_dates[num].strftime("%m/%d/%Y")

    table[row_num][3] = start_time
    table[row_num][4] = end_time

    col_num = 0
    row_num += 1

# Create header row
table.insert(0,["Subject","Start Date","End Date","Start Time","End Time","All Day Event"])

# Create and write csv file
with open("csvs/" + module_name + ".csv","w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(table)

