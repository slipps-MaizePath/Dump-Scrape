# slin63@illinois.edu
import os
import datetime
import csv


def write_to_csv(remls):
    header = ['Trait', 'Her_K1']
    output_list = []
    file_name = RESULTS_DIR + 'summary/Her_K_results:{}.csv'.format(datetime.datetime.now())
    with open(file_name, 'w') as csvfile:
        for reml in remls:
            if len(reml.get_header()) > len(header):
                header = reml.get_header()

            output_dict = {'Trait': reml.name}
            for i in xrange(len(reml.trait_dict)):
                current_her = 'Her_K{}'.format(i + 1)
                output_dict[current_her] = reml.trait_dict[current_her]

            output_list.append(output_dict)

        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        [writer.writerow(row) for row in output_list]

    return 0


def load_remls(bins):
    reml_list = []
    for bin in bins:
        with open(bin, "r") as remlfile:
            reml_list.append(RemlFile(name=get_base_name(bin), trait_dict=access_reml_member(remlfile, "Her_")))

    return reml_list


def access_reml_member(rfile, member):
    reml_info = rfile.readlines()
    trait_dict = {}
    for value in reml_info:
        if member in value:
            split_value = value.split(' ')
            trait_dict[split_value[0]] = split_value[1]

    return trait_dict


def get_base_name(file_name):
    while file_name.find('/') != -1:
        slash_index = file_name.find('/')
        file_name = file_name[slash_index + 1:]
    return file_name


class RemlFile(object):
    def __init__(self, name, trait_dict):
        self.name = name
        self.trait_dict = trait_dict

    def get_header(self):
        trait_headers = self.trait_dict.keys()
        return ['Trait'] + sorted(trait_headers)

    def __repr__(self):
        return self.name + ' - {}'.format(self.trait_dict)


if __name__ == '__main__':
    RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../phenotypes/results/'
    if 'summary' not in os.listdir(RESULTS_DIR):
        os.system('mkdir {}/summary'.format(RESULTS_DIR))
    bins = set([RESULTS_DIR + bin for bin in os.listdir(RESULTS_DIR) if ".reml" in bin])
    remls = load_remls(bins)
    write_to_csv(remls)

    print "-" * 30
    print "Outputting {} CSVs to \n~~~~~~~~~~>{}Done!".format(len(bins), os.popen("cd {} && pwd".format(RESULTS_DIR)).read())

