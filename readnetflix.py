import os
import csv

csvpath=os.path.join("..","Resources",'netflix_ratings.csv')

pelicula=input("which movie do you whant? ")

fount= False

with open(csvpath,'r') as csv_file:

    csvreader=csv.reader(csv_file,delimiter=',')


    for row in csvreader:

        if row[0] == video:

            print(row[0]+" is rated "+ row[1]+ 'with a rating of'+row[5])

            

 

  






