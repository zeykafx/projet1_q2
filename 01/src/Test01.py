#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from random import randint as r

import Corr01 as corr
import q1 as student

ans_mauvais = "Le mois le plus neigeux est {} et vous avez retourné {} avec comme argument ce fichier :\n{}\n"
ans_type =  "Votre fonction retourne un {} alors qu'elle devrait retourner un tuple avec comme argument ce fichier :\n{}\n"
ans_len = "Le tuple retourné par votre fonction est de longueur {} alors qu'il devrait être de longueur 3  avec comme " \
          "argument ce fichier :\n{}\n"
ans_instance = "L'élément {} du tuple retourné pour type {} alors qu'il devrait être {} avec comme argument ce fichier : \n{}\n"
ans_exception = "Votre fonction a provoqué l'exception {} : {} avec comme argument ce fichier : \n{}\n"


class TestMedian(unittest.TestCase):

    def setUp(self) -> None:
        self.test_files = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt', 'test6.txt']
        self.test1_str = "2015\n02/01 23\n03/01 5\n04/01 7\n18/03 6\n2016\n06/08 12"
        self.test2_str = "2015\n02/0123\n03/01 5\n04/01 7\n18/03 6\n2016\n06/08 12"
        self.test3_str = "vide"
        self.test4_str = "2015\n02/01 J\n03/01 0\n04/01 7\n18/03 6\n2016\n06/08 12"
        self.test5_str = "2015\n02/0123\n03/015\n04/017\n18/036\n2016\n06/0812"
        self.test6_str = ""

        ligne = "{}/{} {}\n"
        with open('test6.txt', 'w') as f:       # crée un fichier de manière aléatoire
            for year in range(2018, 2021):
                f.write(str(year) + "\n")
                self.test6_str += str(year) + "\n"
                for i in range(r(0, 6)):
                    to_write = ligne.format(r(0, 28), r(0, 12), r(0, 20))
                    self.test6_str += to_write
                    f.write(to_write)

        self.tests_str = [self.test1_str, self.test2_str, self.test3_str, self.test4_str, self.test5_str, self.test6_str]

    def test(self):
        for i, file in enumerate(self.test_files):
            try:
                stu_ans = student.mois_le_plus_neigeux(file)
                corr_ans = corr.mois_le_plus_neigeux(file)
                self.assertEqual(type(stu_ans), tuple, ans_type.format(type(stu_ans), self.tests_str[i]))
                self.assertEqual(len(stu_ans), 3, ans_len.format(len(stu_ans), self.tests_str[i]))
                for j in range(3):
                    self.assertIsInstance(stu_ans[j], int, ans_instance.format(i, type(stu_ans[0]), int, self.tests_str[i]))
                self.assertEqual(stu_ans, corr_ans, ans_mauvais.format(corr_ans, stu_ans, self.tests_str[i]))
            except Exception as e:
                if isinstance(e, AssertionError):
                    self.fail()
                else:
                    self.fail(ans_exception.format(type(e), e, self.tests_str[i]))


if __name__ == '__main__':
    unittest.main()
