from argparse import ArgumentParser, RawDescriptionHelpFormatter
import textwrap
import sys


def main():
    p = ArgumentParser(
        description=textwrap.dedent('''\
                example usage:
                    $ cat data/whitelist.txt | python build.py --good > good.csv
                    $ cat data/blacklist.txt | python build.py > bad.csv
                    $ cat good.csv bad.csv | gshuf > training.csv
                '''),
        formatter_class=RawDescriptionHelpFormatter,
    )

    p.add_argument('-d', '--debug', dest='debug', action="store_true")
    p.add_argument('--good', action="store_true", default=False)

    args = p.parse_args()

    for l in sys.stdin:
        l = l.rstrip()

        if args.good:
            print('"%s",0' % (l.lower()))
            print('"www.%s",0' % (l.lower()))
        else:
            print('"%s",1' % (l.lower()))


if __name__ == '__main__':
    main()
