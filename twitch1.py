#!/usr/bin/python

import csv, sys, numpy

class Table:
    def __init__(self, tbl):
        self.tbl = tbl

    def compute(self):

        names = self.tbl.pop(0)
        values = map(list, zip(*self.tbl))

        i = 0
        for nm in names:
            values[i] = map(float, values[i])
            print nm + \
                  ": mean " + str(sum(values[i]) / len(values[i])) + \
                  ", median " + str(numpy.median(values[i])) + \
                  ", stdev " + str(numpy.std(values[i]))
            i+=1

class TableLoader:
    def __init__(self):
        pass;

    def load_file(self, filepath):
        with open(filepath, 'rb') as f:
            reader = csv.reader(f)
            data = list(reader)
        return Table(data)


# Your code must call this function
def run_test(csv_path):
    loader = TableLoader()  # implement this

    # Load a CSV file
    table = loader.load_file(csv_path)

    # Compute and print the mean, median and stdev of each series
    table.compute()

# Note:
#   mean: This is the "average" of a list of numbers. Each value contributes
#         equally to the final result.
#   median: This is the "middle" value of a list of numbers; half of the numbers
#           in the list are smaller than the median, and half are larger.
#   stdev: This is a measure of how much the numbers in the list differ from the
#          mean. For each value, take the square of the difference between the
#          value and the mean. Take the mean of the squares, and then take the
#          square root of that mean squared value.

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_test(sys.argv[1])
    else:
        print "Print usage ..."