from os import getcwd, system
from sys import argv
import csv


def generate_plant_dict(csvfile):
    with open(csvfile, 'r') as csvinput:
        reader = csv.DictReader(csvinput)
        plant_dict = {}
        for row in reader:
            plant_dict[row['Plot ID']] = int(row['Stand Count'])

    return plant_dict


def output_plant_dict(plant_dict, digits=4, output='output.csv'):
    digit_string = '0' * int(digits)
    with open(output, 'w') as csvoutput:
        writer = csv.DictWriter(csvoutput, fieldnames=['Plant ID'])
        writer.writeheader()
        for plot_id in plant_dict:
            for i in xrange(1, plant_dict[plot_id] + 1):
                digits_int = len(str(i))
                print digits_int, digits
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
    script, csvfile, digits, output = argv
    plant_dict = generate_plant_dict(csvfile)
    output_plant_dict(plant_dict, digits, output)
    report_output(output)
    system('open {}'.format(output))
