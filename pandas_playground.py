import pandas as pd
import numpy as np


"""
Series Exercise
"""

# Create create and display a one-dimensional array-like object containing an array of data using Pandas module.
 
# test_array =  pd.array([1,2,3])

# print(test_array)

# convert a Panda module Series to Python list and it's type.

# series =  pd.Series([1,2,3])

# converted = series.tolist()

# print(converted)

# to add, subtract, multiple and divide two Pandas Series.

# a = pd.Series([2, 4, 6, 8, 10])
# b = pd.Series([1, 3, 5, 7, 9])

# print(a / b)

# compare = same diff solution different operators ><= and returns Bool

# to convert a dictionary to a Pandas series

# a = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

# converted =  pd.Series(a)

# print(converted)

# to convert a NumPy array to a Pandas series.

# np_array = np.arange(10,51,10)

# print(pd.Series(np_array))

# to change the data type of given a column or a Series.

# sample = pd.Series([100,200,'python',3.12,400])

# print(pd.to_numeric(sample, errors='raise'))

# convert the first column of a DataFrame as a Series.

# df = pd.DataFrame( {'col 1' : np.arange(1,11),'col 2':np.arange(1,11)} )

# print(example_df)

# series = pd.Series(df.iloc[:,0])

# print(extracted)

# convert a given Series to an array.

# list_extracted = extracted.tolist()

# to convert Series of lists to one Series.

# back_to_series = pd.Series(list_extracted)

# to add some data to an existing Series.

# appended = pd.concat([extracted, pd.Series([1,'gosho'])] ,ignore_index=True)

#  to create a subset of a given series based on value and condition.

# s1 = series[series<=5]

# print(subset_below_five)

# to change the order of index of a given series.

# rest= subset_below_five.reindex = [1,0,2,3,4]

# print(rest)

# to create the mean and standard deviation of the data of a given Series.

# print(subset_below_five.mean(), subset_below_five.std())

#  to get the items of a given series not present in another given series.

# s2 = pd.Series([2,4,6,8,10])

# print(subset_below_five[~subset_below_five.isin(s2)])

# 17 to get the items which are not common of two given series.
# wanted output [1,3,5,6,8,10]

# iterable_uniques = pd.Series(np.union1d(subset_below_five,s2))  merge only unique vals

# iterable_commons = pd.Series(np.intersect1d(subset_below_five,s2)) merge common value

# print(iterable_uniques[~iterable_uniques.isin(iterable_commons)]) get only the unique which are not common

#18 to compute the minimum, 25th percentile, median, 75th, and maximum of a given series.

# print(df.iloc[:,0].describe().tolist())

# 19 to calculate the frequency counts of each unique value of a given series.

# random_series = pd.Series(np.random.randint(0,10,size=(40)))

# print(random_series.value_counts())
# print(random_series.groupby(random_series).count().sort_values(ascending=False))

# 20 to display most frequent value in a given series and replace everything else as 'Other' in the series.
# print(random_series)

# print(random_series.value_counts().max())

# random_series[random_series != random_series.value_counts().max()] = 'Other'

# print(random_series)


#21 to find the positions of numbers that are multiples of 5 of a given series.

# print(
# subset_below_five[subset_below_five % 5 == 0].index
# )

#22  to extract items at given positions of a given series.

# print(random_series.iloc[[0,2,4,6]])


# 23 to get the positions of items of a given series in another given series.

# 24  convert the first and last character of each word to upper case in each word of a given series.

# input = pd.Series(['php','python','Java'])

# def handle_capitalization(w):
#     w = w.capitalize()
#     w = w[:-1] + w[-1].upper()
#     return w

# res = input.apply(handle_capitalization,)

# print(res)

# 25 to compute difference of differences between consecutive numbers of a given series.

# print(s1.diff().diff().tolist())

# 27 to convert a series of date strings to a timeseries.

# input = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])

# datetime_input = input.map(lambda x:pd.to_datetime(x))

# 28  to get the day of month, day of year, week number and day of week from a given series of date strings.

# date_series = input.map(lambda x: print(dateutil.parser.parse(x)))

# 29 to convert year-month string to dates adding a specified day of the month.

# input = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])


"""
DataFrame Exercise
"""

#  to get the first 3 rows of a given DataFrame.

# exam_data = {
# 'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
# 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
# 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
# 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']



# df = pd.DataFrame(exam_data, index=labels)

# print(df[0:3])

# to select the 'name' and 'score' columns from the following DataFrame.

# print(df.iloc[:,[0,1]])


# to select the specified columns and rows from a given data frame.
# which are score and qualify

# print(df.loc[:,['score','qualify']])


# to select the rows where the number of attempts in the examination is greater than 2.

# print(df[df['attempts'] > 2])

# to count the number of rows and columns of a DataFrame.

# print(df.shape)  also len(axes[0]) -> rows & len(axes[1]) -> cols

# to select the rows where the score is missing, i.e. is NaN.

# print(df[df['score'].isna()])

# to select the rows the score is between 15 and 20 (inclusive).

# print(df[(df['score']>=15) & (df['score'] <=20)])

# to select the rows where number of attempts in the examination is less than 2 and score greater than 15.

# print(df[(df['attempts'] < 2) & (df['score'] > 15)])

#  to change the score in row 'd' to 11.5.

# df.loc['d','score'] = 11.5

# to calculate the sum of the examination attempts by the students.

# print(df.attempts.sum())

#  to calculate the mean of all students' scores. Data is stored in a dataframe.

# print(df.score.mean())

# to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.

# df.loc['k'] = ["Suresh",  15.5,  1,  "yes",]

# df = df.drop('k')

# print(df)

# to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order. 

# df = df.sort_values(['name','score'], ascending=[False, True])

# print(df)

# to replace the 'qualify' column contains the values 'yes' and 'no' with True and False.

# df['qualify'] = df['qualify'].map({'yes':True,'no':False})


# to change the name 'James' to 'Suresh' in name column of the DataFrame.

# df['name'] = df['name'].replace('James','Suresh')

# to delete the 'attempts' column from the DataFrame.

# df = df.drop(columns=['attempts'])

# to insert a new column in existing DataFrame.

# color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']

# df['color'] = color

# to iterate over rows in a DataFrame.

# for index,row in df.iterrows():
    # print(row['name'], row['score'])

#  to get list from DataFrame column headers.

# print(df.columns.tolist())

# to rename columns of a given DataFrame

# df.columns = [1,'pesho',3,4]

#  to select rows from a given DataFrame based on values in some columns.

# sample = pd.DataFrame({'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]})

# print(sample[sample['col1'] == 4])

#  to reverse the order of a DataFrame columns.

# sample.columns = sample.columns.tolist()[::-1]

#  to add one row in an existing DataFrame.

# df2 = {'col1': 10, 'col2': 11, 'col3': 12}
# sample = sample._append(df2, ignore_index=True)

# df1 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas',],
# 'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})

# print(df1.groupby('city').size().reset_index(name='number of people'))

# to delete DataFrame row(s) based on given column value.

# sample = sample[sample.col2 != 5]

# to widen output display to see more columns.

# pd.set_option('display.max_rows', 500)
# pd.set_option('display.max_columns', 500)
# pd.set_option('display.width', 1000)


#  to select a row of series/dataframe by given integer index.

# print(sample.iloc[2])

# to replace all the NaN values with Zero's in a column of a dataframe.

# df.score =  df.score.fillna(0)

# to convert index in a column of the given dataframe.

# create a col from the index
# df.reset_index(level=0, inplace=True)

#hide
# df =  df.to_string(index=False)

# to set a given value for particular cell in  DataFrame using index value.

# df.iloc[0,0] = 'pesho'


# to count the NaN values in one or more columns in DataFrame.


# print(df.isnull().values.sum())

# to drop a list of rows from a specified DataFrame.

# print(sample)

# sample.drop(labels=[2,4],inplace=True)

# print(sample)


# df.drop(index=['a','b'],inplace=True)

# df = df.reset_index()

# to combining two series into a DataFrame.

# s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
# s2 = pd.Series(['10', '20', 'php', '30.12', '40'])

# df_from_series = pd.concat([s1,s2],axis=1)

# print(df_from_series)

# to shuffle a given DataFrame rows.

# df =  df.sample(frac=1)

# sample = sample.rename(columns={'col2':'pesho'}) 


# 43. Write a Pandas program to get a list of a specified column of a DataFrame.

# print(sample.loc[:,'col2'].tolist())

# to create a DataFrame from a Numpy array and specify the index column and column headers.

# zeros = np.zeros((15,3))

# print(pd.DataFrame(zeros))

#  to find the row for where the value of a given column is maximum.

# example = pd.DataFrame({'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5]})

# print(example[example.col1 == example.col1.max()].index)


# to check whether a given column is present in a DataFrame or not.

# print('test' in df.columns)

#  to get the specified row value of a given DataFrame.

# print(example.iloc[3])


# to get the datatypes of columns of a DataFrame.


# print(example.dtypes)

# example.insert(loc=0, column='col3', value=[7, 8, 12, 1, 11])

# to convert a given list of lists into a Dataframe.

# matrix = [[2, 4], [1, 3]]

# print(pd.DataFrame(matrix))

#  to group by the first column and get second column as lists in rows

# df = pd.DataFrame( {'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]})

# c4 = df.groupby('col1')['col2'].apply(list)

# print(c4)


# 56. Write a Pandas program to get column index from column name of a given DataFrame.

# d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
# df = pd.DataFrame(data=d)

# print(df.columns.get_loc('col2'))

#  to count number of columns of a DataFrame.

# print(len(df.columns.to_list()))


# to select all columns, except one given column in a DataFrame.

# print(df.loc[:, df.columns != 'col3'])

# to get first n records of a DataFrame.

# df.head(n)

# 60. Write a Pandas program to get last n records of a DataFrame.

# df.tail(n)

# df = df.iloc[3:]

# df= df.add_prefix('1')

# df= df.add_prefix('pesho')

# reverse rows

# df = df[::-1]

"""
Index Exercises
"""

#1. Write a Pandas program to display the default index and set a column as an Index in a given dataframe.

df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id': ['t1', 't2', 't3', 't4', 't5', 't6']
    })

# print(df.head(10))

# df = df.set_index('school_code')

# print(df.head(10))

#2. Write a Pandas program to create a multi Index frame using two columns and using an Index and a column.


# df = df.set_index(['school_code','t_id'])

# df = df.set_index('t_id',append=True)


#3. Write a Pandas program to display the default index and set a column as an Index in a given dataframe and then reset the index.

# df.set_index('t_id').reset_index()

#4. Write a Pandas program to create an index labels by using 64-bit integers, using floating-point numbers in a given dataframe.


# df= df.set_index(np.random.rand(6).astype('float64'))

# 5. Write a Pandas program to create a DataFrame using intervals as an index.

# df.index = pd.IntervalIndex.from_breaks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3])

#7. Write a Pandas program to create a dataframe and set a title or name of the index column.

# df.index.name = 'pesho'

#8. Write a Pandas program to set value in a specific cell in a given dataframe using index.

# df.iloc[0,3] = 'gosho'

#9. Write a Pandas program to convert index of a given dataframe into a column.

# df.set_index('t_id', inplace=True)

# df = df.reset_index(level=0)

#10. Write a Pandas program to convert 1st and 3rd levels in the index into columns from a multiple level of index frame of a given dataframe.

# df = df.set_index(['t_id', 'school_code', 'class'])

# df.reset_index(level=['t_id','class'],inplace=True)

#11. Write a Pandas program to check if a specified value exists in single and multiple column index dataframe.

# print('c6' in df.index)
# print('t1' in df.index)

# df.set_index(['school_code','class','t_id'],append=True,inplace=True)

# print('V' in df.index.levels[2])

#15


