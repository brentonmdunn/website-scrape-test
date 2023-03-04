from bs4 import BeautifulSoup
import requests
import re
from csv import writer
import constant

url = "http://courses.ucsd.edu/courseList.aspx?name=BILD"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

file_name = "courses" + "BILD" + ".csv"

with open(file_name, 'w', encoding='utf8', newline='') as f:

    thewriter = writer(f)
    # header = ['Course']
    # thewriter.writerow(header)

    for link in soup.find_all('a', attrs={'href': re.compile("^coursemain.aspx")}):

        fullURL = "http://courses.ucsd.edu/" + str(link.get('href'))

        info = [fullURL]

        thewriter.writerow(info)