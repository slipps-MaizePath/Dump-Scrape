# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
# slin63@illinois.edu
import pandas
from sys import argv
from os import getcwd
import csv


def generate_map(key_csv, rows=150):
    """
    :param key_csv: A pre-formatted CSV containing field and stock information.
    :return: CSV formatted field maps representing the lay out of the intended plots as well as their contents.
    """
    dborow = pandas.read_csv(key_csv, delimiter=',')
    field_set = set(dborow.get(key='Field_Name'))  # field_set contains all Field_Names listed in the passed CSV

    for field in field_set:
        query_string = 'Field_Name == "{0}"'.format(field)
        file_string = 'fieldmap[{0}].csv'.format(field)

        field_df = dborow.query(query_string)  # Subsetting data
        field_df = field_df.pivot(index='Row', columns='Range', values='Row_ID')  # Making the map
        field_df.to_csv(file_string, sep=',')  # Outputting data
        add_rows(file_string, rows)  # Adding row and pass data to csv

        print('{2}\nGenerated map for field: {0}\nOutput at: {1}/{0}'.format(
            'processed-' + file_string, getcwd(), '-' * 20
        ))

    return 0


def add_rows(raw_csv, rows):
    """
    :param raw_csv: CSV processed by generate_map but without row and pass information.
    :param rows: Number of rows in the plot. It's fine to overshoot.
    :return: CSV with row and pass information.
    """
    passes = generate_passes(rows)
    pass_index = 0
    range_list = list(range(2,150))

    with open(raw_csv, 'r') as csvinput:
        with open('processed-' + raw_csv , 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            for row in csv.reader(csvinput):
                if row[0] == 'Row':
                    writer.writerow(['Row'] + range_list[0:len(row)-1] + ['Row', 'Pass'])
                else:
                    writer.writerow(row + [row[0], passes[pass_index]])
                    pass_index += 1

    return 0


def generate_passes(rows):
    """
    :param rows: Number of rows in the field.
    :return: Tuple containing an appropriate length set of paired (row, pass) indices.
    """
    digit_a = 1
    digit_b = 1
    passes = ()
    increment = True

    while len(passes) < rows:
        passes += ("{0}.{1}".format(digit_a, digit_b),)

        if increment:
            digit_b += 1
        else:
            digit_b -= 1

        if digit_b > 4:
            increment = False
            digit_b -= 1
            digit_a += 1
        if digit_b < 1:
            increment = True
            digit_b += 1
            digit_a += 1

    return passes


if __name__ == "__main__":
    file_name, key_csv = argv
    generate_map(key_csv)
    # print(generate_passes(200))
