#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:22:35 2020

@author: ramakrishnadevarakonda
"""

import csv
from pathlib import Path

input_file = Path('Resources','employee_data.csv')
new_date=[]
First_Name=[]
Last_Name=[]
new_ssn=[]
Emp_Id=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
new_state_cd=[]
with open(input_file,'r') as csv_file:
   csv_reader = csv.reader(csv_file,delimiter=',')
   next(csv_reader)
   data=[row for row in csv_reader]
   print(len(data))
   
   for row in data:
# Store emp id       
       Emp_Id.append(row[0])
       
# Split Name into First Name and Last Name       
       name = row[1].split(' ')
       First_Name.append(name[0])
       Last_Name.append(name[1])
       
# Split current date and format into new date        
       dob = row[2].split('-')
       new_date.append(dob[1]+'/'+dob[2]+'/'+dob[0])

# Convert Old SSN into new format
       old_ssn = (row[3]).split('-')
       new_ssn.append('***' + '-' + '**' + '-' + old_ssn[2])
# Format state code      
       state=row[4]
       if state in us_state_abbrev:
           new_state_cd.append(us_state_abbrev[state])
    


for i in range(len(data)):
    print(str(Emp_Id[i])+','+str(First_Name[i])+','+str(Last_Name[i])+','+str(new_date[i])+','+str(new_ssn[i])+','+str(new_state_cd[i]))

output_file = Path('Analysis','Employee_Summary.csv')
with open(output_file, 'w') as out_file: 
    out_file.write('Emp ID')
    out_file.write(',')
    out_file.write('First Name')
    out_file.write(',')
    out_file.write('Last Name')
    out_file.write(',')
    out_file.write('DOB')
    out_file.write(',')
    out_file.write('SSN')
    out_file.write(',')
    out_file.write('State')
    out_file.write('\n')
    for i in range(len(data)):
        out_file.write(str(Emp_Id[i]))
        out_file.write(',')
        out_file.write(str(First_Name[i]))
        out_file.write(',')
        out_file.write(str(Last_Name[i]))
        out_file.write(',')
        out_file.write(str(new_date[i]))
        out_file.write(',')
        out_file.write(str(new_ssn[i]))
        out_file.write(',')
        out_file.write(str(new_state_cd[i]))
        out_file.write('\n')