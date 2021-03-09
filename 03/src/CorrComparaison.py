class vehicule:  # on crée une classe vehicule qui est définie par 2 attributs à savoir MARQUE (make) & COULEUR (color)
    def __init__(self, make=0):
        self.make = make


    # valeur des deux attributs
    # make = ["Ford", "Renault", "Peugeot", "Volkswagen", "Opel"]
    # color = ["Black", "Blue", "Grey", "Red", "Tan"]


# Ceci est à réaliser par l'étudiant

class camion(vehicule):  # par héritage, possède les mêmes attributs que la classe-mère
    def __init__(self, make, color):
        super().__init__(make)  # rappelle de la génération  précédente
        self.color = color

    def __eq__(self, other):
        if self.make == other.make and self.color == other.color:
            return True

        elif self.make == other.make and self.color != other.color:
            return False

        elif self.make != other.make and self.color == other.color:
            return False

        elif self.make != other.make and self.color != other.color:
            return False
