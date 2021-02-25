#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def is_phone_number_regex(filename):
    correct_numbers = []
    with open(filename) as f:
        full_file = [line.strip() for line in f]
    for line in full_file:
        regex_expression = re.compile(r'04\d{2}/\d{2}.\d{2}.\d{2}')
        mo = regex_expression.search(line)  # match object
        if mo:
            correct_numbers.append(line)
        else:
            continue
    return correct_numbers