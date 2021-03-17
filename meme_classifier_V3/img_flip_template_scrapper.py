###########################################
###########################################
###########################################
# DO NOT RUN THIS FILE IF MEMES.CSV EXISTS
# NO NEED TO UNNECESSARILY ADD WEB TRAFFIC TO 
# IMGFLIP
###########################################
###########################################
###########################################
# Jeffrey Worley 
# 2021
# jeff@theworleys.com

from bs4 import BeautifulSoup
import subprocess
import json

IMG_FLIP_URL = "https://imgflip.com/"
NUM_TEMPLATE_PAGES = 14
TEMPLATE_SUFFIX = "memetemplates?page="

templateNames = []

for i in range(1, NUM_TEMPLATE_PAGES):
	print("starting " + str(i))
	curr_url = IMG_FLIP_URL + TEMPLATE_SUFFIX + str(i)
	html = subprocess.run(["curl", curr_url], capture_output=True, text=True).stdout
	soup = BeautifulSoup(html, "html.parser")
	templates = soup.find_all("div", class_="mt-box")

	for template in templates:
		try:
			divWithLink = template.find("div", class_="mt-img-wrap")
			link = divWithLink.a["href"]
			link = link[1:]
			templateNames.append(link)
		except:
			print("an error occured")

# check for and remove duplicates
noDupesNames = []
[noDupesNames.append(x) for x in templateNames if x not in noDupesNames]

print(str(len(noDupesNames)) + " meme templates found")
with open("memeLabels.json", "w") as f:
	json.dump(noDupesNames, f)


