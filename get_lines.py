import argparse


def count_lines(path):
    try:
        with open(path) as in_file:
            return len(in_file.readlines())
    except Exception:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    my_args = parser.parse_args()
    print(count_lines(my_args.file))
