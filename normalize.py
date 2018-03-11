__author__ = 'pluther'
import logging
import csv
import argparse


parser = argparse.ArgumentParser(description='Normalizes data from a variety of inputs to a single output')
parser.add_argument('--debug', help='Add debug to output', action='store_true', default=False)
parser.add_argument('--input', '--input_files', help='CSV files to read input from', required=True)
parser.add_argument('--output', help='Output file for normalized data', default='./normalized_data.csv')
parser.add_argument('--append', help='Appends normalized data to existing output file. If not set, then '
                                     'script will fail if output file already exists.', action='store_true',
                    default=False)
parser.add_argument('--thesaurus', '--input-thesaurus', help='list of synonyms to be used to help data normalization, in yaml format.',
                    default='./input-thesaurus')
parser.add_argument('--format','--output_format', help='File containing output format of data',
                    default='./output-format.txt')
args = parser.parse_args()

#Set logging level:
if args.debug:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('Debug is on')
    logging.debug('Input files: ' + str(args.input))
    logging.debug('Output file: ' + args.output)
    logging.debug('Append output to existing file: ' + args.append)
    logging.debug('Read Output Format from file:' + args.format)
    logging.debug('Input Thesaurus: ' + args.thesaurus)
else:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)