from os import getcwd, system
import csv
import argparse

class PlotCell(object):
    def __init__(self, experiment, plot_id, comments, num_row, num_range):
        self.experiment = experiment
        self.plot_id = plot_id
        self.comments = comments
        self.num_row = num_row
        self.num_range = num_range

    def __repr__(self):
        return self.plot_id


def generate_plots(csvfile):
    plot_list = []
    with open(csvfile, 'r') as csvinput:
        reader = csv.DictReader(csvinput)
        for row in reader:
            plot_list.append(
                PlotCell(
                    experiment=row['Experiment'],
                    plot_id=row['Plot ID'],
                    num_row=row['Row'],
                    num_range=row['Range'],
                    comments=row['Comments']
                )
            )

    return plot_list


def output_plant_csv(plot_list, output='output.csv'):
    with open(output, 'w') as csvoutput:
        writer = csv.DictWriter(
            csvoutput, fieldnames=['Experiment', 'Plot ID', 'Row', 'Range', 'Comments']
        )
        writer.writeheader()
        for plot in plot_list:
            for i in xrange(1, 3):
                split_id = plot.plot_id + '.' + str(i)
                writer.writerow({
                    'Experiment': plot.experiment,
                    'Plot ID': split_id,
                    'Comments': plot.comments,
                    'Row': plot.num_row,
                    'Range': plot.num_range
                })

    return 0


def report_output(output):
    print 'Output at: {0}/{1}'.format(getcwd(), output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processes a CSV File with Plot ID and split Plot IDs '
                                     'into two x.1 x.2 formatted rows.')
    parser.add_argument('csvfile', metavar='csvfile', type=str, help='Name of csvfile to be processed')
    parser.add_argument('-output', default='output.csv', help='Name given to output csvfile')
    parser.add_argument('-delimiter', default='_', type=str, help='Delimiter')
    args = parser.parse_args()

    plot_list = generate_plots(args.csvfile)
    output_plant_csv(plot_list, args.output)
    report_output(args.output)
    system('open {}'.format(args.output))
