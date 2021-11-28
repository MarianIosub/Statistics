import sys


def main():
    if len(sys.argv) != 2:
        print("No csv filepath in arguments")
    else:
        text_file = sys.argv[1]


if __name__ == '__main__':
    main()
