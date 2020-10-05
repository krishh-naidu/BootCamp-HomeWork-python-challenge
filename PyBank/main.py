#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
path = '/Users/ramakrishnadevarakonda/Desktop/python-challenge/BootCamp-HomeWork-python-challenge/Resources/budget_data.csv'
total_number_of_months=[]
profit_loss=[]
average_change=[]
with open (path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    data=[row for row in csv_reader]
    for row in data:
        total_number_of_months.append(row[0])
        profit_loss.append(int(row[1]))

for i in range(len(total_profit)-1):
    monthly_profit_change.append(total_profit[i+1] - total_profit[i])

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
min_increase_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
print("Financial Analysis")
print('-' * len("Financial Analysis"))
print('Total Months: {}'.format(len(total_number_of_months)))
print('Total:'+'$'+str(sum(profit_loss)))
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print('Greatest Increase in Profits:{} ({}{})'.format(total_number_of_months[max_increase_month],'$',max(monthly_profit_change)))
print('Greatest Decrease in Profits:{} ({}{})'.format(total_number_of_months[min_increase_month],'$',min(monthly_profit_change)))

