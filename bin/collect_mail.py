import sys, getopt
import bigbang.mailman as mailman
from pprint import pprint as pp
import logging

logging.basicConfig(level=logging.DEBUG)

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"u:f:")
    except getopt.GetoptError as e:
        print 'GetoptError: %s' % (e)
        sys.exit(2)

    if len(opts) == 0:
        print 'Please include either a url of a mailman web archive'
        print 'or the path to a file with a linebreak-separated list'
        print 'of such urls.'
        print ''
        print 'For example:'
        print ''
        print 'python bin/collect_mail.py -u http://mail.scipy.org/pipermail/scipy-dev/'
        print ''
        print 'or'
        print ''
        print 'python bin/collect_mail.py -f examples/urls.txt'
        print ''

    for opt, arg in opts:
        if opt == '-u':
            mailman.collect_from_url(arg)
            sys.exit()
        elif opt == '-f':
            mailman.collect_from_file(arg)

if __name__ == "__main__":
   main(sys.argv[1:])
