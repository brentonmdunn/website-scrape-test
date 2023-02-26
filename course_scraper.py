from bs4 import BeautifulSoup
import requests
import re
import csv
from csv import writer
import pandas as pd

file = open("coursetester.csv")

url_list = file.readlines()


csv_file = pd.read_csv("coursetester.csv")

number_of_lines = len(csv_file)

print("LINESSSS ____ " + str(number_of_lines))

# print("-----------")
# print(url_list)


index = 1

# if contains \n
# if str(url_list[index])[len(str(url_list[index]))-1:len(str(url_list[index]))]:

# TODO: last page doesn't have \n
# page = requests.get(str(url_list[index])[0:len(str(url_list[index]))-1])
# else:
#     
page = requests.get(url_list[index])

print(page)

# if (page)

soup = BeautifulSoup(page.content, "html.parser")

with open('coursedata.csv', 'w', encoding='utf8', newline='') as f:

    thewriter = writer(f)


    print("This works")
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

    print("Works")

    # for header in soup.find_all('h1'):

    print("[----------------------------------------]")

    dept_code_section = soup.find('h1').text
    print('dept_code_section: ' + str(dept_code_section))

    instructor = soup.find('a', id='instructor_HyperLink').text
    print('instructor: ' + str(instructor))

    # lecture_days = soup.find('span', id='sections_DataGrid_days_Label_0').text
    # print('lecture days: ' + str(lecture_days))

    # lecture_time = soup.find('span', id='sections_DataGrid_time_Label_0').text
    # print('lecture time: ' + str(lecture_time))

    # lecture_location = soup.find('span', id='sections_DataGrid_location_Label_0').text
    # print('lecture location: ' + str(lecture_location))


    # info = [dept_code_section, 
    #         instructor, 
    #         lecture_days, 
    #         lecture_time, 
    #         lecture_location, 
    #         discussion_days,
    #         discussion_time,
    #         discussion_location]

    category = soup.find('span', id='sections_DataGrid_type_Label_0').text
    print('category: ' + str(category))

    section_code = soup.find('span', id='sections_DataGrid_type_Label_0').text
    print('category: ' + str(section_code))

    days = soup.find('span', id='sections_DataGrid_days_Label_0').text
    print('days: ' + str(days))

    time = soup.find('span', id='sections_DataGrid_time_Label_0').text
    print('time: ' + str(time))

    location = soup.find('span', id='sections_DataGrid_location_Label_0').text
    print('location: ' + str(location))


    print("[----------------------------------------]")

    info = [category, dept_code_section, section_code, instructor, days, time, location]
    thewriter.writerow(info)

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
    
