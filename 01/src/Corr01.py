def mois_le_plus_neigeux(file):
    """
    Détermine le mois le plus neigeux selon un fichier
    :param file: fichier qui recense toutes les chutes de neiges sur plusieurs années
    :return: un tuple de la forme (mois, année, nombre_de_cm_tombés)
    """
    with open(file, 'r') as f:
        lines = f.readlines()

    dic = {}
    for line in lines:
        cleaned_line = line.strip("\n").replace("/", " ").split()
        if len(cleaned_line) == 1:
            dic[cleaned_line[0]] = {}
            year = cleaned_line[0]
        elif len(cleaned_line) == 3:
            if not cleaned_line[0].isnumeric() or not cleaned_line[1].isnumeric() or not cleaned_line[2].isnumeric():
                pass
            elif int(cleaned_line[1]) in dic[year]:
                dic[year][int(cleaned_line[1])] += int(cleaned_line[2])
            else:
                dic[year][int(cleaned_line[1])] = int(cleaned_line[2])
    # Ici, un dictionnaire du type {2015 : {01: 34, 02: 5, ...}, ...} a été créé. On va désormais rechercher le mois où
    # la valeur est la plus élevée pour retourner le bon tuple

    maxi = (0, 0, 0)
    for y in dic.keys():
        for month in dic[y].keys():
            chutes = dic[y][month]
            if chutes > maxi[2]:
                maxi = (month, int(y), chutes)
    return maxi
