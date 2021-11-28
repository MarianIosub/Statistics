import csv
import numpy
import statistics
from scipy.stats import pearsonr
import matplotlib.pyplot as plt


class StatisticsUtils:
    def __init__(self, filepath):
        self.header = []
        self.ages = []
        self.nationalities = []
        self.IQs = []
        self.genders = []
        self.read_csv_data(filepath)
        self.columns = [self.ages, self.genders, self.IQs, self.nationalities]

    def read_csv_data(self, filepath):
        try:
            file = open(filepath)
        except FileNotFoundError:
            print("File not found!")
            return -1
        csv_reader = csv.reader(file)
        self.header = next(csv_reader)
        for row in csv_reader:
            self.ages.append(int(row[0]))
            self.genders.append(row[1])
            self.IQs.append(int(row[2]))
            self.nationalities.append(row[3])

    def column_statistics(self, column_index):
        self.mean(column_index)
        self.median(column_index)
        self.standard_deviation(column_index)
        self.column_min(column_index)
        self.column_max(column_index)
        self.quartiles(column_index)
        self.covariance()
        self.correlation_coefficient()

    def mean(self, column_index):
        if column_index in [0, 2]:
            print("Media coloanei " + str(column_index) + " este: " + str(numpy.mean(self.columns[column_index])))
        else:
            print(f"Nu se poate printa media pentru avast coloana: {column_index}")

    def standard_deviation(self, column_index):
        if column_index in [0, 2]:
            print("Deviatia standard a coloanei " + str(column_index) + " este: " + str(
                statistics.stdev(self.columns[column_index])))
        else:
            print(f"Nu se poate printa deviatia standard pentru aceasta coloana: {column_index}")

    def median(self, column_index):
        if column_index in [0, 2]:
            print("Mediana coloanei " + str(column_index) + " este: " + str(
                statistics.median(self.columns[column_index])))
        else:
            print(f"Nu se poate printa mediana pentru aceasta coloana: {column_index}")

    def column_min(self, column_index):
        if column_index in [0, 2]:
            print("Minimul coloanei " + str(column_index) + " este: " + str(min(self.columns[column_index])))
        else:
            print(f"Nu se poate printa minimul pentru aceasta coloana: {column_index}")

    def column_max(self, column_index):
        if column_index in [0, 2]:
            print("Maximul coloanei " + str(column_index) + " este: " + str(max(self.columns[column_index])))
        else:
            print(f"Nu se poate printa maximul pentru aceasta coloana: {column_index}")

    def quartiles(self, column_index):
        if column_index in [0, 2]:
            print("Cvartilele coloanei " + str(column_index) + " sunt: " +
                  str(numpy.quantile(self.columns[column_index], .25)) + " " +
                  str(numpy.quantile(self.columns[column_index], .50)) + " " +
                  str(numpy.quantile(self.columns[column_index], .75)))
        else:
            print(f"Nu se pot printa cvartilele pentru aceasta coloana: {column_index}")

    def covariance(self):
        cov = numpy.cov(self.columns[0], self.columns[2])
        print(f"Covarianta coloanelor Varsta si IQ este: {cov[0][1]}")

    def correlation_coefficient(self):
        sorted_ages, sorted_iqs = zip(*sorted(zip(self.ages, self.IQs)))
        corr, _ = pearsonr(self.columns[0], self.columns[2])
        print(f"Coeficientul corelatiei coloanelor Varsta si IQ este: {corr}")
        plt.plot(sorted_ages, sorted_iqs)
        plt.xlabel("Varsta")
        plt.ylabel("IQ")
        plt.title("Corelatia dintre Varsta si IQ")
        plt.show()
