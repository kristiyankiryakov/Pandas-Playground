import pandas as pd
import numpy as np

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



