import pandas

#import data
dborow = pandas.read_csv('dbo_row_sl_revision5-23-2016.csv', delimiter=',')
print(dborow.columns)
passes=pandas.read_csv('pass.csv', delimiter=',')

#subset data by field
sf541=dborow.query('Field_Name == "541-49"')
cfar600=dborow.query('Field_Name == "CFAR600"')

#make map
fieldmapsf541=sf541.pivot(index='Row', columns='Range', values='Row_ID')
fieldmapcfar600=cfar600.pivot(index='Row', columns='Range', values='Row_ID')

#to count number of ranges: sf541numranges=sf541['Range'].value_counts()

fieldmapsf541pass=pandas.concat([fieldmapsf541, passes], axis=1)
fieldmapcfar600pass=pandas.concat([fieldmapcfar600, passes], axis=1)

fieldmapsf541pass.to_csv('fieldmapsf541.csv', sep=',')
fieldmapcfar600pass.to_csv('fieldmapcfar600.csv', sep=',')
