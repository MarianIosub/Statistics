import sys

from StatisticsUtils import StatisticsUtils


def main():
    if len(sys.argv) != 3:
        print("No correct call")
    else:
        text_file = sys.argv[1]
        stats = StatisticsUtils(text_file, sys.argv[2])
        if not stats.header:
            return
        stats.column_statistics(0)


if __name__ == '__main__':
    main()
