import csv

with open('lut_input.csv', 'rb') as csvfile:
    lut_reader = csv.reader(csvfile, delimiter=',')
    
    table_buffer = []
    
    for row in lut_reader:  
        table_buffer.append(row)
        
       
    

column_count = len(table_buffer[0])
row_count = len(table_buffer)

transposed_buffer = [[0 for x in range(row_count)] for y in range (column_count)]

for x in range(row_count):
    for y in range(column_count):
        transposed_buffer[y][x] = table_buffer[x][y]

        

with open('lut_transposed.csv', 'wb') as destfile:
    lut_writer = csv.writer(destfile, delimiter=',')
    
    for x in range(column_count):
            lut_writer.writerow(transposed_buffer[x])