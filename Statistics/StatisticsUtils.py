import csv


class StatisticsUtils:
    def __init__(self, filepath, chosen_column_index):
        self.chosen_column_index = chosen_column_index
        self.header = []
        self.rows = []
        self.read_csv_data(filepath)

    def read_csv_data(self, filepath):
        file = open(filepath)
        csv_reader = csv.reader(file)
        pass

    def mean(self, column_index):
        pass

    def standard_deviation(self, column_index):
        pass

    def median(self, column_index):
        pass

    def column_min(self, column_index):
        pass

    def column_max(self, column_index):
        pass

    def quartiles(self, column_index):
        pass

    def covariance(self):
        pass

    def correlation_coefficient(self):
        pass