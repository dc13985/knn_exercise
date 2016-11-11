from bs4 import BeautifulSoup
import urllib.request
import csv
import random

#import data from web
def soup_set(location):
    site = location
    req = urllib.request.Request(site)
    page = urllib.request.urlopen(req)
    soup_temp = BeautifulSoup(page,"lxml")
    return soup_temp


#import data from txt file
def get_data(filename, split, training_set=[],test_set= []):
    with open(filename, 'r') as iris:
        lines = csv.reader(iris)
        dataset = list(lines)       
        for x in range(len(dataset)):
            for y in range(4): # first four entires to float
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split: # split into a training & test set
                training_set.append(dataset[x])
            else:
                test_set.append(dataset[x])
