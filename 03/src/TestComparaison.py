#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os

import CorrComparaison as correct
import Comparaison as student

class vehicule: #on crée une classe vehicule qui est définie par 1 attribut à savoir MARQUE (make).
    def __init__(self, make=0,):      
        self.make = make
class camion(vehicule):  # par héritage, possède les mêmes attributs que la classe-mère
    def __init__(self, make, color):
        super().__init__(make, color)  # rappelle de la génération  précédente

class TestComparaison(unittest.TestCase):

    def setUp(self):
        self.camion_test_1 = correct.camion("Ford","Grey")
        self.camion_test_2 = correct.camion("Opel","Red")
        self.camion_test_3 = correct.camion("Ford","Grey")
        self.camion_test_4 = correct.camion("Renault","Black")
        self.camion_test_5 = correct.camion("Peugeot","Red")
    
    def test_0(self):
        try:
            student_ans = student.camion("Ford", "Grey")
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
       
        self.assertEqual(student_ans, self.camion_test_1,"Les 2 attributs sont identiques")
    
    
    def test_1(self):
        try:
            student_ans = student.camion("Opel", "Grey") # tu creer un camion diff de celui de test et tu compare la non egalité
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
       
        self.assertNotEqual(student_ans, self.camion_test_2 ,"La couleur est différente deux sur les camions")
    
     
    def test_2(self):
        try:
            student_ans = student.camion("Opel", "Grey") 
        except Exception as e:
            self.fail(f"Votre fonction a provoqué l'exception {type(e)}: {e} avec comme argument {filename}")
       
        self.assertNotEqual(student_ans, self.camion_test_3 ,"La marque est différente sur les deux camions")
        
    
        
 