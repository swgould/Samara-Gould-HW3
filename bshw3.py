# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup
import re

baseurl = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "html.parser")

findstudent = soup.find_all(text = re.compile('student'))
for comment in findstudent: 
	fixed_text = str(comment).replace('student', 'AMAZING student')
	comment.replaceWith(fixed_text)


for img in soup.findAll('img'):
	if img['src'] == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		img['src'] = 'https://s-media-cache-ak0.pinimg.com/736x/cd/2d/ab/cd2dab30dc35d59775903d2d54d6fe29.jpg'
	else: 
		img['src'] = 'media\logo.png'


result = str(soup)


f = open("bs3.html", "w") 

f.write(result)
f.close()







