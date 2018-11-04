#converts a table in a csv into a single column
#each column is stacked after the preceding columns

import csv

with open('lut_input.csv', 'rb') as csvfile:
    lut_reader = csv.reader(csvfile, delimiter=',')
    
    table_buffer = []
    
    for row in lut_reader:  
        table_buffer.append(row)
        
       
    

column_count = len(table_buffer[0])
row_count = len(table_buffer)

with open('lut_single_column.csv', 'wb') as destfile:
    lut_writer = csv.writer(destfile, delimiter=',')
    
    for x in range(column_count):
        for y in range(row_count):
            lut_writer.writerow(table_buffer[y][x])
    
    
    