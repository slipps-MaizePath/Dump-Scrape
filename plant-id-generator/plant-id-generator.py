from os import getcwd, system
from sys import argv
import csv
import argparse

class PlantCell(object):
    def __init__(self, experiment, plot_id, stand_count, comments, plant_id=None):
        self.experiment = experiment
        self.plot_id = plot_id
        self.stand_count = stand_count
        self.comments = comments
        self.plant_id = plant_id

    def __repr__(self):
        return self.plot_id, self.stand_count, self.plant_id


def generate_plants(csvfile):
    with open(csvfile, 'r') as csvinput:
        reader = csv.DictReader(csvinput)
        plant_list = []
        for row in reader:
            if int(row['Stand Count']) == 0:
                pass
            else:
                plant_list.append(
                    PlantCell(
                        experiment=row['Experiment'],
                        plot_id=row['Plot ID'],
                        stand_count=int(row['Stand Count']),
                        comments=row['Comments']
                    )
                )

    return plant_list


def output_plant_csv(plant_list, digits=4, output='output.csv'):
    digit_string = '0' * digits
    with open(output, 'w') as csvoutput:
        writer = csv.DictWriter(csvoutput, fieldnames=['Experiment', 'Plant ID', 'Plot ID', 'Plant Num', 'Comments'])
        writer.writeheader()
        for plant in plant_list:
            for i in xrange(1, plant.stand_count + 1):
                digits_int = len(str(i))
                if int(digits_int) > int(digits):
                    raise OverflowError('Digit argument too low to accommodate number of plants.')
                else:
                    id = digit_string[:-digits_int] +  str(i)
                    plant_id = plant.plot_id + '_' + id
                    writer.writerow({
                        'Plant ID': plant_id,
                        'Experiment': plant.experiment,
                        'Plot ID': plant.plot_id,
                        'Plant Num': '',
                        'Comments': plant.comments
                    })

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

    plant_list = generate_plants(args.csvfile)
    output_plant_csv(plant_list, args.digits, args.output)
    report_output(args.output)
    system('open {}'.format(args.output))
