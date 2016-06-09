from os import getcwd, system
from sys import argv
import csv
import argparse

def generate_plant_dict(csvfile):
    with open(csvfile, 'r') as csvinput:
        reader = csv.DictReader(csvinput)
        plant_dict = {}
        for row in reader:
            plant_dict[row['Plot ID']] = int(row['Stand Count'])

    return plant_dict


def output_plant_dict(plant_dict, digits=4, output='output.csv'):
    digit_string = '0' * digits
    with open(output, 'w') as csvoutput:
        writer = csv.DictWriter(csvoutput, fieldnames=['Plant ID'])
        writer.writeheader()
        for plot_id in plant_dict:
            for i in xrange(1, plant_dict[plot_id] + 1):
                digits_int = len(str(i))
                if int(digits_int) > int(digits):
                    raise OverflowError('Digit argument too low to accomodate number of plants.')
                else:
                    id = digit_string[:-digits_int] + str(i)
                    plant_id = plot_id + id
                    writer.writerow({'Plant ID':plant_id})

    return 0


def report_output(output):
    print 'Output at: {0}/{1}'.format(getcwd(), output)


if __name__ == '__main__':
    """
    ::csvfile:: Name of the csv file you're trying to process
    ::digits:: Number of trailing digits you want in the plant_id
    ::output:: Name of the output file
    """
    parser = argparse.ArgumentParser(description='Process a CSV File with Plot ID and stand count columns into a '
                                                 'new CSV with generated Plant IDs.')
    parser.add_argument('csvfile', metavar='csvfile', type=str, help='Name of csvfile to be processed')
    parser.add_argument('-output', default='output.csv', help='Name given to output csvfile')
    parser.add_argument('-digits', default=4, type=int, help='Number of trailing digits in the plant id')
    args = parser.parse_args()

    plant_dict = generate_plant_dict(args.csvfile)
    output_plant_dict(plant_dict, args.digits, args.output)
    report_output(args.output)
    system('open {}'.format(args.output))
