#this simle function generates the input coordinates of a 3d lut
#the lut size is specified at the start
#reuslt is stored in csv


#input arguments are processed through sys.argv
#sys.argv contains string

import sys
import csv

lut_size = int(sys.argv[1])

with open('lut_input.csv', 'wb') as csvfile:
    lut_writer = csv.writer(csvfile, delimiter=',')
    

    for x in range (1,lut_size+1):
        for y in range(1,lut_size+1):
            for z in range(1,lut_size+1):
                lut_writer.writerow([x,y,z])
           