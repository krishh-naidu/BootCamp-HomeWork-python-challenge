#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 11:34:33 2020

@author: ramakrishnadevarakonda
"""

import csv
from pathlib import Path

input_file = Path("BootCamp-HomeWork-python-challenge",'PyPoll','Resources','election_data.csv')
output_file = Path("BootCamp-HomeWork-python-challenge",'PyPoll','Analysis','Election_Result.txt')
total_no_of_votes=[];list_of_candidates=[];candidate_votes=[];names_and_votes=[]
with open(output_file, 'w') as file:
    with open(input_file,'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        next(csv_reader)
        data=[row for row in csv_reader]
    # Total number of votes
        [total_no_of_votes.append(row[0]) for row in data]
    # Capture all the candidates
        [list_of_candidates.append(row[2]) for row in data if row[2] not in list_of_candidates]
        print('Election Results')
        print('----------------')
        print('Total Votes:' +str(len(total_no_of_votes)))
        print('--------------------')
        file.write('Election Results')
        file.write('\n')
        file.write('-------------------')
        file.write('\n')
        file.write('Total Votes: {}'.format(len(total_no_of_votes)))
        file.write('\n')
        file.write('-------------------')
        file.write('\n')
    #Calculate all the votes for each candidate
        for candidate in list_of_candidates:
            for row in data:
                if row[2]==candidate:
                    candidate_votes.append(row[0])
            
            print(f"{candidate}:{(len(candidate_votes) / len(total_no_of_votes) * 100):.3f}%({len(candidate_votes)})")
            file.write(f"{candidate}:{(len(candidate_votes) / len(total_no_of_votes) * 100):.3f}%({len(candidate_votes)})")
            file.write('\n')
    #create a list with all the candidate votes
            names_and_votes.append((len(candidate_votes)))
            candidate_votes=[]
    # create a dictionary using 2 lists
        d = dict(zip(list_of_candidates,names_and_votes))
        
        winner=max(d,key=d.get)
        print('-----------------------')
        file.write('-------------------')
        file.write('\n')
        print('Winner:' + winner)
        print('-----------------')
        file.write('Winner:' +winner)
        file.write('\n')
        file.write('-----------------')
    