#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os

import CorrMatchingPhoneNumbers as correct
import MatchingPhoneNumbers as student


class TestMatchingPhoneNumber(unittest.TestCase):

    def test0_UsPhoneNumber(self):
        filename = 'phone_numbers.txt'
        try:
            student_ans = student.matching_phone_numbers(filename)
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
        answer = correct.is_phone_number_regex(filename)
        self.assertEqual(student_ans, answer, f"Votre fonction n'a pas retourné la bonne liste de numéros belge: vous avez retourné {student_ans} au lieu de {answer}")

    def test1_EmptyFile(self):
        filename = 'empty_file.txt'
        try:
            student_ans = student.matching_phone_numbers(filename)
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
        answer = correct.is_phone_number_regex(filename)
        self.assertEqual(student_ans, answer, f"Votre fonction n'a pas retourné la bonne liste de numéros belge: vous avez retourné {student_ans} au lieu de {answer}")

    def test2_OneFalseNumber(self):
        filename = 'one_false_number.txt'
        try:
            student_ans = student.matching_phone_numbers(filename)
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
        answer = correct.is_phone_number_regex(filename)
        self.assertEqual(student_ans, answer, f"Votre fonction n'a pas retourné la bonne liste de numéros belge: vous avez retourné {student_ans} au lieu de {answer}")

    def test3_OneTrueNumber(self):
        filename = 'one_true_number.txt'
        try:
            student_ans = student.matching_phone_numbers(filename)
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
        answer = correct.is_phone_number_regex(filename)
        self.assertEqual(student_ans, answer, f"Votre fonction n'a pas retourné la bonne liste de numéros belge: vous avez retourné {student_ans} au lieu de {answer}")

    def test4_TwoTrueNumber(self):
        filename = 'two_true_numbers.txt'
        try:
            student_ans = student.matching_phone_numbers(filename)
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
        answer = correct.is_phone_number_regex(filename)
        self.assertEqual(student_ans, answer, f"Votre fonction n'a pas retourné la bonne liste de numéros belge: vous avez retourné {student_ans} au lieu de {answer}")



if __name__ == '__main__':
    unittest.main()
