# import argparse


# parser = argparse.ArgumentParser()
# parser.add_argument('mode', action='store', type=str, help='')
# parser.add_argument('integers', action='store', nargs='*', type=int, help='additional variables')
# args = parser.parse_args()


# if args.mode == 'doc':
#     if args.var[0] == 1:
#         print('additional var 1')
#     print('doc')
#     exit()

# print('mode error')

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))