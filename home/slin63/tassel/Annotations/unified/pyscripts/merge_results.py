# slin63@illinois.edu
import datetime
import os


def get_base_name(file_name):
    while file_name.find('/') != -1:
        slash_index = file_name.find('/')
        file_name = file_name[slash_index + 1:]
    return file_name


def read_bins_to_string(bins):
    bin_str = 'LDAK RESULTS: GENERATED {}\n{}\n'.format(datetime.datetime.now(), '-' * 20)
    for bin in bins:
        with open(bin, "r") as remlfile:
            string_list = [get_base_name(bin) + '\n'] + remlfile.readlines() + ['-' * 20 + '\n']
            data_string = ''.join(string_list)
            bin_str += data_string

    return bin_str


def output_cat(bin_str):
    file_name = RESULTS_DIR + 'summary/LDAK_results:{}.txt'.format(datetime.datetime.now())
    with open(file_name, "w") as outfile:
        outfile.write(bin_str)

if __name__ == '__main__':
    RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../phenotypes/results/'
    if 'summary' not in os.listdir(RESULTS_DIR):
        os.system('mkdir {}/summary'.format(RESULTS_DIR))
    bins = set([RESULTS_DIR + bin for bin in os.listdir(RESULTS_DIR) if ".reml" in bin])
    bin_str = read_bins_to_string(bins)
    output_cat(bin_str)

    print "-" * 30
    print "Merging {} results to \n~~~~~~~~~~>{}Done!".format(len(bins), os.popen("cd {} && pwd".format(RESULTS_DIR)).read())
