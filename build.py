from argparse import ArgumentParser, RawDescriptionHelpFormatter
import textwrap
import sys

if sys.version_info > (3,):
    from urllib.parse import urlparse
    basestring = (str, bytes)
else:
    from urlparse import urlparse


def main():
    p = ArgumentParser(
        description=textwrap.dedent('''\
                example usage:
                    $ csirtg-urlsml --training data/training.csv -i http://badsite.com/1.html
                '''),
        formatter_class=RawDescriptionHelpFormatter,
        prog='csirtg-urlsml'
    )

    p.add_argument('-d', '--debug', dest='debug', action="store_true")
    p.add_argument('--good', action="store_true", default=False)

    args = p.parse_args()

    for l in sys.stdin:
        l = l.rstrip()

        if args.good:
            print('"%s",0' % (l.lower()))
        else:
            print('"%s",1' % (l.lower()))


if __name__ == '__main__':
    main()
