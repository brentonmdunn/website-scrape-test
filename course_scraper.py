from bs4 import BeautifulSoup
import requests
import re
import csv
from csv import writer
import pandas as pd

file = open("coursetester.csv")
url_list = file.readlines()

# Counts the number of lines
csv_file = pd.read_csv("coursetester.csv")
number_of_lines = len(csv_file) + 1     # idk why I add 1 but it undercounts, maybe 0 indexing?


index = 6

if (index < number_of_lines - 1):
    page = requests.get(str(url_list[index])[0:len(str(url_list[index]))-1])
    print("Debug 1")
else:
    page = requests.get(url_list[index])
    print("Debug 2")

print(page)

# if (page)

soup = BeautifulSoup(page.content, "html.parser")

with open('coursedata.csv', 'w', encoding='utf8', newline='') as f:

    thewriter = writer(f)


    dept_code_section = ''
    instructor = ''
    lecture_days = ''
    lecture_time = ''
    lecture_location = ''
    discussion_days = ''
    discussion_time = '' 
    discussion_location = ''
    is_lecture = ''
    is_final = ''
    days = ''
    time = ''
    location = ''
    category = ''
    section_code = ''




    dept_code_section = soup.find('h1').text
    instructor = soup.find('a', id='instructor_HyperLink').text
    category = soup.find('span', id='sections_DataGrid_type_Label_0').text
    section_code = soup.find('span', id='sections_DataGrid_type_Label_0').text
    days = soup.find('span', id='sections_DataGrid_days_Label_0').text
    time = soup.find('span', id='sections_DataGrid_time_Label_0').text
    location = soup.find('span', id='sections_DataGrid_location_Label_0').text


    info = [category, dept_code_section, section_code, instructor, days, time, location]
    thewriter.writerow(info)

    print(dept_code_section)
    print(instructor)
    print(category + " | " + section_code + " | " + days + " | " + time + " | " + location)

#-------------------------------------------------------------------------------
    discussion_list = soup.find_all('tr', class_='discussion')


    discussion_list.append('')      # adds an extra item in list to account for final

    discussion_count = 1

    for discussion in discussion_list:
        
        category_section_num = "sections_DataGrid_type_Label_" + str(discussion_count)
        section_code_section_num = "sections_DataGrid_section_Label_" + str(discussion_count)
        days_section_num = "sections_DataGrid_days_Label_" + str(discussion_count)
        time_section_num = "sections_DataGrid_time_Label_" + str(discussion_count)
        location_section_num = "sections_DataGrid_location_Label_" + str(discussion_count)


        category = soup.find('span', id=category_section_num).text
        section_code = soup.find('span', id=section_code_section_num).text
        days = soup.find('span', id=days_section_num).text
        time = soup.find('span', id=time_section_num).text
        location = soup.find('span', id=location_section_num).text



        print(category + " | " + section_code + " | " + days + " | " + time + " | " + location)

        discussion_count += 1

        info = [category, dept_code_section, section_code, instructor, days, time, location]
        thewriter.writerow(info)

#-------------------------------------------------------------------------------

    # list of 1, have to do this to locate where final is
    # final_list = soup.find_all('tr', class_='final')

    # for final in final_list:





    # for item in soup.find()

    

    

    # is_lecture, is_final, dept_code_section, section_code, instructor, day, time, location
    
