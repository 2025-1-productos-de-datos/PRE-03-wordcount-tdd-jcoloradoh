# python3 -m homework --input data/input --output data/output

import sys

from homework.src._internals.parse_args import parse_args


def main():
    input_folder, output_folder = parse_args()

    # print("input foder:", input_folder)
    # print("output folder:", output_folder)
