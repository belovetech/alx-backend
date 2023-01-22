#!/usr/bin/env python3

# x = "hello"

#if condition returns False, AssertionError is raised:
# assert x == "goodbye", "x should be 'hello'"

# assert type(x) == str, "Type of x should be 'str'"

# x  = -1
# try:
#     assert type(x) == int and x > 0
# except AssertionError:
#     print("Type of x should be int and > zero")

import csv
data = None

file = "Popular_Baby_Names.csv"
with open(file) as f:
    reader = csv.reader(f)
    dataset = [row for row in reader]
data = dataset[1:]

for i in range(5):
    print(data[i])