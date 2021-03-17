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
CSV_FILE_NAME = "open-images-dataset-validation.tsv"

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
	images = csv.reader(csvFile, delimiter="\t", quotechar='"')
	next(images)
	labelFolder = "not-a-meme/"
	currTestPath = IMAGES_FOLDER + TEST_FOLDER + labelFolder
	currTrainPath = IMAGES_FOLDER + TRAIN_FOLDER + labelFolder
	if not os.path.exists(currTestPath):
		os.mkdir(currTestPath)
	if not os.path.exists(currTrainPath):
		os.mkdir(currTrainPath)
	if not images is None:
		i = 0
		for line in images:
			if random.random() > .5:
				if random.random() < .2:
					# put in test folder
					subprocess.Popen("curl " + line[0] +  " > " + currTestPath + str(i) + ".jpg", shell=True).wait()
				else:
					# put in val folder
					subprocess.Popen("curl " + line[0] +  " > " + currTrainPath + str(i) + ".jpg", shell=True).wait()

				if i > 300:
					break
				i += 1
	else:
		print("Error: " + CSV_FILE_NAME + " file not found")



