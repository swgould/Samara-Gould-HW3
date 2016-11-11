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
	comment.replace_with(fixed_text)


for var in soup.find_all(class_='field-items'):
	for link in var.findAll('img'):
		link['src'] = 'https://s-media-cache-ak0.pinimg.com/736x/cd/2d/ab/cd2dab30dc35d59775903d2d54d6fe29.jpg'
html_string = str(soup)

for var2 in soup.find_all(class_='logo'):
	for link in var2.findAll('img'):
		link['src'] = 'logo.png'
html_string = str(soup)

for var3 in soup.find_all(class_='footer-logo'):
	for link in var3.findAll('img'):
		link['src'] = 'logo.png'
html_string = str(soup)


x = soup.find_all('img')
for a in x: 
	href = a["src"]
	if not href.startswith("https:"):
		print ("before changing",a["src"])
		a["src"] = "https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png"
		print (a['src'])

result = str(soup)


f = open("bs3.html", "w") 

f.write(result)
f.close()







