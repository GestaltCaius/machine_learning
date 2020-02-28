"""
Calculate the Euclidean distance between our accommodation which can accommodate 3 people and the first accommodation of the dataFrame paris_listings.
Assign the result to the first_distance variable and display the result.
"""
import numpy
import pandas as pd
import functools

from pandas import Series

paris_listings = pd.read_csv('./datasets/paris_airbnb.csv')
first_accommodation: Series = paris_listings.iloc[0]
our_accommodation: Series = paris_listings.iloc[1]

print(paris_listings)
print(first_accommodation.tolist())  # index location (ligne 1)

for first_accommodation_list, our_accommodation_list in first_accommodation.tolist(), our_accommodation.tolist():
        differences = numpy.abs(theirs - ours)
squared = [difference ** 2 for difference in differences]
sum_of_squares = functools.reduce(lambda x, y: x + y, squared)
euclidean_distance = numpy.sqrt(sum_of_squares)

print(euclidean_distance)
