import sys

from StatisticsUtils import StatisticsUtils


def main():
    if len(sys.argv) != 3:
        print("No correct call")
    else:
        text_file = sys.argv[1]
        stats = StatisticsUtils(text_file)
        if not stats.header:
            return
        if sys.argv[2] not in ['0', '2']:
            print("Nu se pot calcula statisticile pentru coloana " + sys.argv[2])
            return
        stats.column_statistics(sys.argv[2])


if __name__ == '__main__':
    main()
