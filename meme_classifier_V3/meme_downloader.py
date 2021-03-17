# Jeffrey Worley 
# 2021
# jeff@theworleys.com

import csv
import os
import subprocess
import random
import json

IMAGES_FOLDER = "meme_img_set/"
TEST_FOLDER = "test/"
TRAIN_FOLDER = "train/"
CSV_FILE_NAME = "memes.csv"

# setup folders for test set and validation set
if not os.path.exists(IMAGES_FOLDER):
	os.mkdir(IMAGES_FOLDER)
os.chdir(IMAGES_FOLDER)
if not os.path.exists(TEST_FOLDER):
	os.mkdir(TEST_FOLDER)
if not os.path.exists(TRAIN_FOLDER):
	os.mkdir(TRAIN_FOLDER)
os.chdir("../")

# load csv file with scraped links
curlLinks = {}
with open(CSV_FILE_NAME) as csvFile:
	scrapedMemes = csv.reader(csvFile)
	next(scrapedMemes)
	if not scrapedMemes is None:
		for line in scrapedMemes:
			tmp = line[0].split("/")
			lineLabel = tmp[len(tmp) - 1]
			if not lineLabel in curlLinks:
				curlLinks[lineLabel] = []
			curlLinks[lineLabel].append(line[2])
	else:
		print("Error: " + CSV_FILE_NAME + " file not found")

with open("fetchedMemes.json", "w") as f:
	json.dump(list(curlLinks.keys()), f)
print("num labels: "  + str(len(list(curlLinks.keys()))))
#	curl images and randomly assign 20% to test and 80% to validation
for label in curlLinks:
	print("starting download for " + label)
	labelFolder = label + "/"
	currTestPath = IMAGES_FOLDER + TEST_FOLDER + labelFolder
	currTrainPath = IMAGES_FOLDER + TRAIN_FOLDER + labelFolder

	if not os.path.exists(currTestPath):
		os.mkdir(currTestPath)
	if not os.path.exists(currTrainPath):
		os.mkdir(currTrainPath)
	i = 0
	for imgLink in curlLinks[label]:
		imgName = label + "_" + imgLink.split("/")[1]
		if not os.path.exists(currTestPath + imgName) and not os.path.exists(currTrainPath + imgName):
			# only download images we dont already have 
			if random.random() < .2:
				# put in test folder

				subprocess.Popen("curl " + imgLink +  " > " + currTestPath + imgName, shell=True).wait()
			else:
				# put in val folder
				subprocess.Popen("curl " + imgLink +  " > " + currTrainPath + imgName, shell=True).wait()
		if i > 100:
			break
		i += 1
	print("finished download for " + label)



