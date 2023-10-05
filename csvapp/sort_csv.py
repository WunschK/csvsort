import csv
def sort_csv(input_file, output_file, column_name):
    '''this function sorts a csv according to the selected column-name and outputs the file as sorted_persons.csv'''
    #read the csv per line
    with open(input_file, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)
        # add the data to the list data
        data = [row for row in csv_reader]
    # sort data by column name
    data.sort(key=lambda x: x[column_name])

    # save the sorted file
    with open(output_file, mode='w', newline='') as file:
        fieldnames = csv_reader.fieldnames
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerows(data)
