#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re


def is_phone_number_regex(filename):
    # creation d'une liste vide, la liste contiendra tous les numéros belges valide.
    correct_numbers = []
    with open(filename) as f:
        full_file = [line.strip() for line in f]
    for line in full_file:

        # ici on créer une regular expression qui sera utilisé pour comparer les différents strings du fichier
        # le \d signifie qu'on "laisse" passer des chiffres et donc \d{2} veut dire que on "laisse" passer deux chiffres
        # quelconque à cet endroit de l'expression.
        # le string est "raw" car sinon il faut "escape" les "\" donc "\d" serait "\\d"
        regex_expression = re.compile(r'04\d{2}/\d{2}.\d{2}.\d{2}')

        # ici le match object va être vrai ssi il a trouvé un string (dans ce ca si, un numéro de type belge)
        # qui correspond à l'expression définie juste au dessus. le mo va donc chercher l'expression dans chaque ligne
        # du fichier
        mo = regex_expression.search(line)  # match object

        # si le mo est vrai, la ligne est un numéro (ou contient un numéro mais dans ce cas la ligne est un seul numéro)
        if mo:
            correct_numbers.append(line)
        else:
            # si aucun numéro belges n'est trouvé sur la ligne, continue la boucle qui passe sur toute les lignes
            continue
    return correct_numbers


# Une version peut être plus simple à comprendre est celle ci:

def is_phone_number(filename):
    correct_numbers = []
    with open(filename) as f:
        full_file = [line.strip() for line in f]
    for line in full_file:

        # un numéro de telephone belges fais 13 caractères
        # ex: 0400/00.00.00 = 13 caractères
        if len(line) < 13:
            continue

        # Ici on vérifie que les caractères "spéciaux" sont présent
        if str(line[0:2]) != '04' or line[4] != '/' or line[7] != '.' or line[10] != '.':
            continue

        # Ici il faut vérifier que ce qui se trouve entre les caractères spéciaux sont bien des chiffres.
        elif not line[2:4].isdecimal() or not line[5:7].isdecimal() or not line[8:10].isdecimal() or not line[11:13].isdecimal():
            continue

        # si on arrive ici c'est que le numéro est valide, on l'ajoute donc à la liste
        else:
            correct_numbers.append(line)

    return correct_numbers
