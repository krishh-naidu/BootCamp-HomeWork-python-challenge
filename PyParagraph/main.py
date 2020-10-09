#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:38:54 2020

@author: ramakrishnadevarakonda
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:22:35 2020

@author: ramakrishnadevarakonda
"""

from pathlib import Path
word_count=[]
input_file = Path('Resources','paragraph_3.txt')
with open(input_file,'r') as txt_file:
   txt_reader = txt_file.read()
   words = len([word for word in txt_reader.split(" ")])
   sentences = len([word for word in txt_reader if word in(".",'?','!')])
   print('Paragraph Analysis')
   print('-------------------')
   print('Approximate Word Count:', words)
   print('Approximate Word Count:', sentences)
   print(f'Average Letter Count: {len([c for c in txt_reader if c.isalpha()])/words:.2f}')
   print(f'Average Sentence Length: {(words/sentences):.2f}')
   

   
output_file = Path('Analysis','Paragraph Analysis_3.txt')
with open(output_file,'w') as out_file:
    out_file.write('Paragraph Analysis')
    out_file.write('\n')
    out_file.write('-------------------')
    out_file.write('\n')
    out_file.write(f'Approximate Word Count:{words}')
    out_file.write('\n')
    out_file.write(f'Approximate Sentence Count: {sentences}')
    out_file.write('\n')
    out_file.write(f'Average Letter Count: {len([c for c in txt_reader if c.isalpha()])/words:.2f}')
    out_file.write('\n')
    out_file.write(f'Average Sentence Length: {(words/sentences):.2f}')