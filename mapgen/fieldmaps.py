# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
# slin63@illinois.edu
import pandas
from sys import argv
from os import getcwd

key_csv = argv

def generate_map(key_csv):
    dborow = pandas.read_csv(key_csv, delimiter=',')
    field_set = set(dborow.get(key='Field_Name'))  # field_set contains all Field_Names listed in the passed CSV

    for field in field_set:
        query_string = 'Field_Name == "{0}"'.format(field)
        file_string = 'fieldmap[{0}].csv'.format(field)

        field_df = dborow.query(query_string)  # Subsetting data
        field_df = field_df.pivot(index='Row', columns='Range', values='Row_ID')  # Making the map
        # field_df_passes = pandas.concat([field_df, passes], axis=1)  # Appending pass axes
        field_df.to_csv(file_string, sep=',')  # Outputting data

        print('{2}\nGenerating map for field: {0}\nOutput at: {1}{0}'.format(
            file_string, getcwd(), '-'*20
        ))
'dogs'

if __name__ == "__main__":
    # generate_map(key_csv='dbo_row_sl_revision5-23-2016.csv')
    generate_map(key_csv=str(key_csv))

