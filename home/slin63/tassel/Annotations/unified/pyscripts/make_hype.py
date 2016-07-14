# slin63@illiois.edu
import os


def strip_extensions(file_name):
    dot_index = file_name.find('.')
    return file_name[:dot_index]


def populate_hype_list(bins):
    count = 1
    hype_list = []
    for bin in bins:
        name = "hyp_{}_kinlist.txt".format(count)
        dirs = KINSHIP_DIR + bin
        hype_list.append(HypeFile(name=name, dirs=dirs))
        count += 1

    return hype_list


def output_hype_file(hype_list):
    print "Generating hype-lists:"
    for hyp in hype_list:
        print "~~~~~~~~~~>{}".format(hyp.name)
        text = open(hyp.name, "w")
        text.write(hyp.dirs)
        text.close()
    print "Done!"


class HypeFile(object):
    def __init__(self, name, dirs):
        self.name = KINSHIP_DIR + name
        self.dirs = dirs

    def __repr__(self):
        return self.name + ' ' + self.dirs


if __name__ == '__main__':
    KINSHIP_DIR = os.path.dirname(os.path.realpath(__file__)) + '/../kinship/'
    bins = set([strip_extensions(bin) for bin in os.listdir(KINSHIP_DIR) if "kinlist.txt" not in bin])
    hype_list = populate_hype_list(bins)
    output_hype_file(hype_list)
