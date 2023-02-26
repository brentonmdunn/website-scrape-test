from bs4 import BeautifulSoup
import requests
import re
from csv import writer

url = "http://courses.ucsd.edu/courseList.aspx?name=CSE%20&dept=true"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

with open('courses.csv', 'w', encoding='utf8', newline='') as f:

    thewriter = writer(f)
    # header = ['Course']
    # thewriter.writerow(header)

    for link in soup.find_all('a', attrs={'href': re.compile("^coursemain.aspx")}):

        fullURL = "http://courses.ucsd.edu/" + str(link.get('href'))

        info = [fullURL]

        thewriter.writerow(info)