#!.venv/bin/python3
import argparse
import json
import time
from importlib import import_module

import requests

from util.file import readfile


def get_input_file(year: int, day: int):
    with open('/Users/chris/.httpie/sessions/adventofcode.com/aoc.json', 'r') as f:
        session_data = json.load(f)

    cookie = session_data['cookies'][0]['value']
    cookies = {"session": cookie}
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    response = requests.get(url, cookies=cookies)
    output_filename = f'{year}/day{day:02}/input.txt'
    with open(output_filename, 'w') as f:
        f.write(response.text)


curr_year = time.localtime().tm_year
curr_month = time.localtime().tm_mon
curr_day = time.localtime().tm_mday

parser = argparse.ArgumentParser()
if curr_month == 12:
    parser.add_argument('-y', '--year', type=int, default=curr_year)
    parser.add_argument('-d', '--day', type=int, default=curr_day)
else:
    parser.add_argument('-y', '--year', type=int)
    parser.add_argument('-d', '--day', type=int)

parser.add_argument('-i', '--input', action="store_true")

args = parser.parse_args()

if args.year is None:
    print('You must specify a year')
    exit(1)

if args.day is None:
    print('You must specify a day')
    exit(1)

if args.input:
    get_input_file(args.year, args.day)
    exit(0)

input_file = f'{args.year}/day{args.day:02}/input.txt'
input_lines = readfile(input_file)

module_name = f'{args.year}.day{args.day:02}.day'
module = import_module(module_name)
solve_part1 = getattr(module, 'solve_part1')
solve_part2 = getattr(module, 'solve_part2')

print(f'Part 1: {solve_part1(input_lines)}')
print(f'Part 2: {solve_part2(input_lines)}')
