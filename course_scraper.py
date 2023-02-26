from bs4 import BeautifulSoup
import requests
import re
import csv
from csv import writer
import pandas as pd
import constant


file = open(constant.COURSES_CSV)
url_list = file.readlines()

# Counts the number of lines
csv_file = pd.read_csv(constant.COURSES_CSV)
number_of_lines = len(csv_file) + 1     # idk why I add 1 but it undercounts, maybe 0 indexing?

for index in range(number_of_lines):

    print("{---------------------------}")

    if (index < number_of_lines - 1):
        page = requests.get(str(url_list[index])[0:len(str(url_list[index]))-1])
        print("Debug 1")
    else:
        page = requests.get(url_list[index])
        print("Debug 2")

    print(page)

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
        days = ''
        time = ''
        location = ''
        category = ''
        section_code = ''

        print("Debug code 3")

        
        dept_code_section = soup.find('h1').text
        instructor = soup.find('a', id='instructor_HyperLink').text

        try:
            category = soup.find('span', id='sections_DataGrid_type_Label_0').text
            section_code = soup.find('span', id='sections_DataGrid_type_Label_0').text
            days = soup.find('span', id='sections_DataGrid_days_Label_0').text
            time = soup.find('span', id='sections_DataGrid_time_Label_0').text
            location = soup.find('span', id='sections_DataGrid_location_Label_0').text

            print("Debg code 4")

            info = [category, dept_code_section, section_code, instructor, days, time, location]
            thewriter.writerow(info)
        except:
            pass
        print("Debug code 5")

        # cuts off graduate courses
        try:
            if int(dept_code_section[4:7]) > 199:

                break
        except:
            pass
            

        print(dept_code_section)
        print(instructor)
        print("Debug code 6")
        print(category + " | " + section_code + " | " + days + " | " + time + " | " + location)
        

    #-------------------------------------------------------------------------------
        
        

        # seminars this doesn't happen
        # bad coding but idk what else to do
        try:
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
        except:
            continue
            

    #-------------------------------------------------------------------------------
    
