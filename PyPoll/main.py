#this is my placeholder
import csv
import os
from collections import defaultdict
from collections import Counter

#create file extension numbers, need to read through two csv files
fileextension = ['1', '2']

#file path to the raw data
for filenumber in fileextension:
    
    file = os.path.join('raw_data', 'election_data_' + str(filenumber) + '.csv')

#define lists       
    totalvotes = []
    candidatename = []
    win = []
    winPercentage = []
    count = []

#command to open and read csv file

    with open(file, 'r') as csvfile:
        csvread = csv.reader(csvfile)
    
        next(csvread, None)
            
        for row in csvread:
            totalvotes.append(row[2])

#create dictionary and for loop to calc total votes
    dictionary = {}
    for w in totalvotes:
        if w in dictionary:
            dictionary[w]+=1
        else:
            dictionary[w]=0
    for key, value in dictionary.items():
        candidatename.append(key)
        win.append(value)

    for ky in range(len(win)):
        vl = int(win[ky])/int((len(totalvotes)))
        winPercentage.append(vl)

    maxvotes = max(dictionary,key=dictionary.get)

#Zip the Candidate results

    zipped=zip(candidatename, winPercentage, win)    

#create output file
    output_dest = os.path.join('Output','pypoll_output_' + str(filenumber) + '.txt')
#I am trying to keep the notation for the output file similar to the way the raw data file path is created

#print output to output file
    with open(output_dest, 'w') as writefile:
        writefile.writelines('Election Results' + '\n')
        writefile.writelines('----------------------------------------------------------------' + '\n')
        writefile.writelines('Total Votes: ' + str(totalvotes) + '\n')
        writefile.writelines('----------------------------------------------------------------' + '\n')
        writefile.writelines('Winner: ' + str(maxvotes) + '\n')

#print output to terminal 
    print('Election Results')
    print('----------------------------------------------------------------')
    print('Total Votes: ' + str(totalvotes))
    print('----------------------------------------------------------------')
    for candidatename, winPercentage, win in zipped:
        print(candidatename, (round(winPercentage, 2)*100), win)
    print('----------------------------------------------------------------')
    print('Winner: ' + maxvotes)
   
