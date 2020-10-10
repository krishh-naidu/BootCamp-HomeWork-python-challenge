#!/usr/bin/env python
# coding: utf-8

# In[85]:

import csv
from pathlib import Path

input_file = Path('Resources','budget_data.csv')
total_number_of_months=[]
profit_loss=[]
average_change=[]

with open (input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    data=[row for row in csv_reader]
    for row in data:
        total_number_of_months.append(row[0])
        profit_loss.append(int(row[1]))
    
    for i in range(len(profit_loss)-1):
        average_change.append(profit_loss[i+1] - profit_loss[i])

max_increase_month = average_change.index(max(average_change)) + 1
min_increase_month = average_change.index(min(average_change)) + 1

output_file = Path('Analysis','Financial_Analysis.txt')

with open(output_file, 'w') as file:
    file.write('Financial Analysis')
    file.write('\n')
    file.write('-------------------')
    file.write('\n')
    file.write('Total Months: {}'.format(len(total_number_of_months)))
    file.write('\n')
    file.write('Total:'+'$'+str(sum(profit_loss)))
    file.write('\n')
    file.write(f"Average Change:${round(sum(average_change)/len(average_change),2)}")
    file.write('\n')
    file.write('Greatest Increase in Profits:{} ({}{})'.format(total_number_of_months[max_increase_month],'$',max(average_change)))
    file.write('\n')
    file.write('Greatest Decrease in Profits:{} ({}{})'.format(total_number_of_months[min_increase_month],'$',min(average_change)))

# Print statements
print("Financial Analysis\n",'-'*len("Financial Analysis"))
print('Total Months: {}'.format(len(total_number_of_months)))
print('Total:'+'$'+str(sum(profit_loss)))
print(f"Average Change: {round(sum(average_change)/len(average_change),2)}")
print('Greatest Increase in Profits:{} ({}{})'.format(total_number_of_months[max_increase_month],'$',max(average_change)))
print('Greatest Decrease in Profits:{} ({}{})'.format(total_number_of_months[min_increase_month],'$',min(average_change)))

