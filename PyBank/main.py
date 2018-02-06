#this is my placeholder
import os
import csv

#create file extension numbers, need to read through two csv files
fileextension = ['1', '2']

#file path to the raw data
for filenumber in fileextension:
    
    file = os.path.join('raw_data', 'budget_data_' + str(filenumber) + '.csv')

#define lists
    months = []
    revenue = []

#command to read csv file
    with open(file, 'r') as csvfile:
        csvread = csv.reader(csvfile)
    
        next(csvread, None)

        for row in csvread:
            months.append(row[0])
            revenue.append(int(row[1]))

    totmonths = len(months)

#Define the following variables: greatest increase, greatest decrease and total revenue
    greatestinc = revenue[0]
    greatestdec = revenue[0]
    totalrevenue = 0


    for r in range(len(revenue)):
        if revenue[r] >= greatestinc:
            greatestinc = revenue[r]
            greatestincmonth = months[r] #id the month for greatest inc
        elif revenue[r] <= greatestdec:
            greatestdec = revenue[r]
            greatestdecmonth = months[r] #id month for greatest dec
        totalrevenue = totalrevenue + revenue[r]

#define the variable for average change and do the calc for avg change
    avgchange = round(totalrevenue/totmonths, 2)

#create output file
    output_dest = os.path.join('Output','pybank_output_' + str(filenumber) + '.txt')
#I am trying to keep the notation for the output file similar to the way the raw data file path is created

#print output to output file
    with open(output_dest, 'w') as writefile:
        writefile.writelines('Financial Analysis' + '\n')
        writefile.writelines('Total Months: ' + str(totmonths) + '\n')
        writefile.writelines('Total Revenue: $' + str(totalrevenue) + '\n')
        writefile.writelines('Average Revenue Change: $' + str(avgchange) + '\n')
        writefile.writelines('Greatest Increase in Revenue: ' + greatestincmonth + ' $' + str(greatestinc) + '\n')
        writefile.writelines('Greatest Decrease in Revenue: ' + greatestdecmonth + ' $' + str(greatestdec) + '\n')

#print output to terminal 
    print('Financial Analysis')
    print('----------------------------------------------------------------')
    print('Total Months: ' + str(totmonths))
    print('Total Revenue: $' + str(totalrevenue))
    print('Average Revenue Change: $' + str(avgchange))
    print('Greatest Increase in Revenue: ' + greatestincmonth + ' $' + str(greatestinc))
    print('Greatest Decrease in Revenue: ' + greatestdecmonth + ' $' + str(greatestdec))