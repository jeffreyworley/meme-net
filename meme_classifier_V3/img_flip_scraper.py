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
import json
import subprocess

MEME_LABELS = []
with open("memeLabels.json") as f:
	MEME_LABELS = json.load(f)
print(len(MEME_LABELS))

IMG_FLIP_URL = "https://imgflip.com/"
NUM_PAGES_PER_LABEL = 25
IMG_PRE = "http://i.imgflip.com/"

BAD_LINKS = ["4urdei.jpg", "4sntwv.jpg", "4cosd1.jpg", "3xecn2.jpg", "4js4bo.jpg", "40vhlw.jpg"]
for i in range(0, len(BAD_LINKS)):
	BAD_LINKS[i] = IMG_PRE + BAD_LINKS[i]

# setup csv
f = open("memes.csv", "w")
f.write("label,pageLink,imageLink\n")

# start scraping
for memeLabel in MEME_LABELS:
	print("starting " + memeLabel)
	for i in range(1, NUM_PAGES_PER_LABEL): # retrieves ~300 memes per label
		# setup current page number
		currUrl = IMG_FLIP_URL + memeLabel + "?page=" + str(i)
		# curl the html file
		print(currUrl)
		html = subprocess.run(["curl", currUrl], capture_output=True, text=True).stdout
		# soupify for dom manipulation
		soup = BeautifulSoup(html, "html.parser")

		memes = soup.find_all("div", class_="base-unit clearfix")

		for meme in memes:
			try:
				pageLink = IMG_FLIP_URL + meme.a["href"][1:]
				imgLink = meme.img["src"][2:]
				if not imgLink in BAD_LINKS:
					f.write(memeLabel + "," + pageLink + "," + imgLink + "\n")
			except:
				# some of their memes have a weird format. just move on
				print("an error occured")
	print("finished " + memeLabel)
