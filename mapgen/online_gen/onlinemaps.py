# Generates a field map when passed an appropiate CSV with pre-filled row and range information
# slin63@illinois.edu
import csv
from sys import argv


def get_info(csvfile):
    """
    :param csvfile: A pre-formatted CSV file to extract plot_ids, rows, and ranges.
    :return: Dictionary formatted as {plot_id: (range, row)}
    """
    with open(csvfile, 'r') as csvinput:
        reader = csv.DictReader(csvinput)
        plot_dict = {}
        experiments = {}
        for row in reader:
            plot = row['Plot ID']
            experiment = row['Experiment Name']
            range_num = row['Range']
            row_num = row['Row']
            date = row['Planting Date']

            experiments[experiment] = date
            plot_dict[plot] = (int(range_num), int(row_num))

    return plot_dict, experiments


if __name__ == "__main__":
    file_name, csvfile = argv
    print get_info(csvfile)
