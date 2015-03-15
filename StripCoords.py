# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:50:47 2015

@author: Duncan Parkes

A script for stripping the coordinates out of csv versions of wikipedia tables

"""



import numpy
import re
import csv

# Load in the table of locations
# Tell it that " are comments so we don't get in trouble with commas in text
# Name;Location;Coordinates;Notes
data = numpy.genfromtxt('./SouthEastPacific.csv', delimiter = '\t', skip_header=3, dtype=None )
#print data
coords = []
# Data[i][2] contains the string on which we will run our regular expression
for i in range(len(data)):
    line = data[i][2]
#    print line
    x = re.search( r'(?<=/\s)-?\d+\.\d*', line, re.M|re.I)
    if x:
       print "First coordinate: : ", x.group()
    else:
       print "No match!!"
    y = re.search( r'(?<=;\s)-?\d+\.\d*', line, re.M|re.I)
    if y:
       print "Second coordinate : ", y.group()
    else:
       print "No match!!"
#    data[i][1] = data[i][1].replace(",", "")
    info = (data[i][0],data[i][1],x.group(),y.group())
    coords.append(info)
    
# save this list of coordinate pairs as a csv file
with open("SouthEastPacificOut.txt", 'wb') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["Name", "Location", "lat", "lon"])
    writer.writerows(coords)

