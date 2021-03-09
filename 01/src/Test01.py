#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from random import randint as r
import Corr01 as corr
import q1 as student


# Messages d'erreur à renvoyer en fonction des erreurs
ans_mauvais = "Le mois le plus neigeux est {} et vous avez retourné {} avec comme argument ce fichier :\n{}\n"
ans_type =  "Votre fonction retourne un {} alors qu'elle devrait retourner un tuple avec comme argument ce fichier :\n{}\n"
ans_len = "Le tuple retourné par votre fonction est de longueur {} alors qu'il devrait être de longueur 3  avec comme " \
          "argument ce fichier :\n{}\n"
ans_instance = "L'élément {} du tuple retourné pour type {} alors qu'il devrait être {} avec comme argument ce fichier : \n{}\n"
ans_exception = "Votre fonction a provoqué l'exception {} : {} avec comme argument ce fichier : \n{}\n"


class TestSnow(unittest.TestCase):

    def setUp(self) -> None:
        """
        Crée une liste avec les clés de tous les fichiers ainsi qu'une liste avec la notation en str de tous les
        fichiers. Cette notation en str de chaque fichier est utile pour le ressortir en message d'erreur afin de
        permettre à l'étudiant de bien comprendre quel test a posé problème.

        Cette fonction crée également un fichier (test6.txt) de manière aléatoire afin d'éviter qu'une solution ne
        puisse être hardcodée.
        """
        self.test_files = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt', 'test5.txt', 'test6.txt']

        self.test1_str = "2015\n02/01 23\n03/01 5\n04/01 7\n18/03 6\n2016\n06/08 12"
        self.test2_str = "2015\n02/0123\n03/01 5\n04/01 7\n18/03 6\n2016\n06/08 12"
        self.test3_str = "vide"
        self.test4_str = "2015\n02/01 J\n03/01 0\n04/01 7\n18/03 6\n2016\n06/08 12"
        self.test5_str = "2015\n02/0123\n03/015\n04/017\n18/036\n2016\n06/0812"
        self.test6_str = ""

        ligne = "{}/{} {}\n"
        with open('test6.txt', 'w') as f:       # crée un fichier de manière aléatoire et ajoute son str dans test6_str
            for year in range(2018, 2021):
                f.write(str(year) + "\n")
                self.test6_str += str(year) + "\n"
                for i in range(r(0, 6)):
                    to_write = ligne.format(r(1, 28), r(1, 12), r(1, 20))
                    self.test6_str += to_write
                    f.write(to_write)

        self.tests_str = [self.test1_str, self.test2_str, self.test3_str, self.test4_str, self.test5_str, self.test6_str]

    def test(self):
        """
        Effectue tous les tests sur la solution de l'étudiant. Pour chaque fichier de test, on évalue (dans l'ordre) :
            -   Si le type retourné est bien un tuple
            -   S'il est de longueur 3
            -   Si chacun de ses éléments est un int
            -   Si la réponse est bonne

        Les tests visés par chaque fichiers sont :
            -   test1.txt: Réponse correcte sur fichier correct
            -   test2.txt: Manque un espace entre la date et le relevé des chutes de neige, vérifie que la solution de
                           l'étudiant skip la ligne
            -   test3.txt: Fichier vide, doit retourner (0, 0, 0)
            -   test4.txt: Lettre à la place d'un nombre pour le relevé des chutes de neige, vérifie qu'il skip la ligne
            -   test5.txt: Fichier où toutes les lignes sont incorrectes, doit retourner (0, 0, 0)
            -   test6.txt: Fichier aléatoire pour prévenir un harcode de la solution
        """
        for i, file in enumerate(self.test_files):
            try:
                stu_ans = student.mois_le_plus_neigeux(file)
                corr_ans = corr.mois_le_plus_neigeux(file)
                # Test du type retourné
                self.assertEqual(type(stu_ans), tuple, ans_type.format(type(stu_ans), self.tests_str[i]))
                # Test de la longueur du tuple retourné
                self.assertEqual(len(stu_ans), 3, ans_len.format(len(stu_ans), self.tests_str[i]))
                for j in range(3):    # Test du fait que les trois éléments du tuple retourné soient des int
                    self.assertIsInstance(stu_ans[j], int, ans_instance.format(i, type(stu_ans[0]), int, self.tests_str[i]))
                # Test pour voir si c'est la bonne réponse
                self.assertEqual(stu_ans, corr_ans, ans_mauvais.format(corr_ans, stu_ans, self.tests_str[i]))
            except Exception as e:
                if isinstance(e, AssertionError):       # Pour pas avoir un message d'erreur trop long
                    self.fail()
                else:
                    # Pour les erreurs qui ont pu être causées par la solution de l'étudiant
                    self.fail(ans_exception.format(type(e), e, self.tests_str[i]))


if __name__ == '__main__':
    unittest.main()
