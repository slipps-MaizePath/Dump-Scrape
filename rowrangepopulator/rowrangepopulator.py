# Should we always start from row 5? -- slin63
# Assuming we start from row 1 range 1 and have a maximum of 5 rows and 5 ranges
from os import getcwd
import csv
from sys import argv


def populate(csvfile, max_row=10, max_range=5, start_row=5, start_range=2):
    """
    :param csvfile: A pre-formatted CSV file needing its range and row information to be filled out.
    :param max_row: The maximum row dimension of the field.
    :param max_range: The maximum range dimension of the field.
    :param start_row: The initial row of the seed.
    :param start_range: The initial range of the seed.
    :return:
    """
    with open(csvfile, 'r') as csvinput:
        with open('OUT-' + csvfile, 'w') as csvoutput:
            reader = csv.DictReader(csvinput)
            writer = csv.DictWriter(csvoutput, fieldnames=reader.fieldnames)
            index = 0
            writer.writeheader()

            coords = generate_coords(  # Ordered (range, row)
                max_row, max_range, start_range=start_range, start_row=start_row
            )
            try:
                for row in reader:
                    writer.writerow({
                        'Row_ID': row['Row_ID'],
                        'Experiment_name': row['Experiment_name'],
                        'Source_Seed': row['Source_Seed'],
                        'Pedigree': row['Pedigree'],
                        'Field_Name': row['Field_Name'],
                        'Row_name': row['Row_name'],
                        'Range': coords[index][0],
                        'Row': coords[index][1],
                        'Block': row['Block'],
                        'Rep': row['Rep'],
                        'Kernel_Num': row['Kernel_Num'],
                        'Planting_Date': row['Planting_Date'],
                        'Harvest_Date': row['Harvest_Date'],
                        'Row_Comments': row['Row_Comments']
                    })
                    index += 1
            except IndexError:
                print '\tAllotted space too small for complete planting.\n\tRows and ranges filled where possible.'

            print 'Output at: {1}/{0}'.format('OUT-' + csvfile, getcwd())

    return 0


def generate_coords(max_row, max_range, start_range, start_row):
    """
    :return: Produces tuple containing ordered (range, row) coordinate pairs to be used in the CSV file.
    """
    coordinate_tuple = ()
    current_range = start_range
    current_row = start_row
    increment = True

    while current_range <= max_range:
        coordinate_tuple += ((current_range, current_row),)

        if increment:
            current_row += 1
        else:
            current_row -= 1

        if current_row > max_row:
            increment = False
            current_row -= 1
            current_range += 1
        if current_row < MINIMUM_ROW:
            increment = True
            current_row += 1
            current_range += 1
    print coordinate_tuple
    return coordinate_tuple


if __name__ == '__main__':
    MINIMUM_ROW = 5
    file_name, csvfile, max_row, max_range, start_row, start_range = argv
    populate(csvfile, int(max_row), int(max_range), start_row=int(start_row), start_range=int(start_range))