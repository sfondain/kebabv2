class ingredient(object):
    def __init__(self,ingId, nom, vege, pesci):
        self.ingId = ingId
        self.nom = nom
        self.vege = vege
        self.pesci = pesci

class sauce(object):
    def __init__(self,sauceId, nom):
        self.sauceId = sauceId
        self.nom = nom

ingredients = []
ingredients.append(ingredient(1,'Viande', False, False))
ingredients.append(ingredient(2,'Tomate', True, True))
ingredients.append(ingredient(3,'Oignon', True, True))
ingredients.append(ingredient(4,'Salade', True, True))
ingredients.append(ingredient(5,'Poisson', False, True))
ingredients.append(ingredient(6,'Crevette', False, True))

sauces = []
sauces.append(sauce(1,'Blanche'))
sauces.append(sauce(2,'Bechamel'))
sauces.append(sauce(3,'Algerienne'))
sauces.append(sauce(4,'Ketchup'))
sauces.append(sauce(5,'Mayonnaise'))
sauces.append(sauce(6,'Moutarde'))
sauces.append(sauce(7,'BBQ'))
sauces.append(sauce(8,'Samourai'))

kebab = []
sauceSelected = []

def afficherIngredients():
    another = True
    another2 = True
    print("-------------------------------")
    print("Ingredients")
    print("-----------")
    for item in ingredients:
        print item.ingId, "-", item.nom
    print("-------------------------------")
    while another != False:
        ing = raw_input('Entrez un ingredient a ajouter : ')
        for item in ingredients:
            if int(ing) == int(item.ingId):
                print("-------------------------------")
                kebab.append(item)
                print "Le kebab est compose de "
                for i in kebab:
                    print i.nom
                ano = raw_input('Un autre ingredient ? (oui ou non) ')
                if str(ano) == "non":
                    another = False
    print("-------------------------------")
    print("Sauces")
    print("-----------")
    for item in sauces:
        print item.sauceId, "-", item.nom
    print("-------------------------------")
    while another2 != False:
        saucesel = raw_input('Entrez une sauce a ajouter : ')
        for item in sauces:
            if int(saucesel) == int(item.sauceId):
                print("-------------------------------")
                sauceSelected.append(item)
                print "Le kebab est compose de "
                for i in kebab:
                    print i.nom
                for i in sauceSelected:
                    print "Sauce", i.nom
                ano = raw_input('Une autre sauce ? (oui ou non) ')
                if str(ano) == "non":
                    another2 = False
    isVege = True
    isPesci = True
    for item in kebab:
        if item.vege == False:
            isVege = False
        if item.pesci == False:
            isPesci = False
    print "Le kebab est compose de \nPain"
    for i in kebab:
        print i.nom
    for i in sauceSelected:
        print "Sauce" , i.nom
    if isVege == False:
        if isPesci == True:
            print "Le kebab est pescitarien mais pas vegetarien"
        else:
            print "Le kebab n'est ni vegetarien ni pescitarien"
    else:
        print "Le kebab est vegetarien et pescitarien"

# Demarrage
afficherIngredients()