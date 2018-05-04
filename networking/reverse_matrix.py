#Form_name ^, ID_form^v, Status, received files, dien files 
#Gosho_form, 456456ddas1, (o), djkslasdak.pdf, djkslasdak.pdf 
#Pesho_form, 38sadda123, [x], ashuidsajk.pdf, add_a_name.pdf
#Scholarship, 41sadasd2, [-], gosho_schol.pdf, no_document.pdf

import csv

input_data = "csv"

output_data =list()
with open('sample.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimeter=', ')
    for row in spamreader:
        print(row)
for i in range(0, len(input_data)):
    for j in range(0, len(input_data[0])):
        pass
